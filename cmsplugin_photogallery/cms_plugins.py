from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from ordered_model.admin import OrderedTabularInline

from .models import GalleryPlugin, GalleryPicture


class PictureInline(OrderedTabularInline):
    model = GalleryPicture
    extra = 1
    fields = ('image',
              'alt_tag',
              # 'text',
              'move_up_down_links',
              )
    readonly_fields = ('move_up_down_links', )

    def move_up_down_links(self, obj):
        if obj.id:
            return render_to_string("ordered_model/admin/order_controls.html", {
                'urls': {
                    'up': reverse("admin:move", args=[obj.id, 'up']),
                    'down': reverse("admin:move", args=[obj.id, 'down']),
                },
                'query_string': self.request_query_string
            })
        else:
            return ''
    move_up_down_links.allow_tags = True
    move_up_down_links.short_description = _(u'Move')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, models.TextField):
            modified_text_field = db_field.formfield()
            modified_text_field.widget = forms.Textarea(attrs={'cols': 30, 'rows': 3})
            return modified_text_field
        return super(PictureInline, self).formfield_for_dbfield(db_field, **kwargs)


class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _("Gallery")
    module = _("Gallery")
    render_template = "cmsplugin_gallery/gallery.html"

    inlines = [PictureInline]

    def get_plugin_urls(self):
        urlpatterns = [
            url(r'^move_ordered/(?P<ob_id>[0-9]+)/(?P<direction>up|down)/$', self.move, name='move'),
        ]
        return urlpatterns

    def move(self, request, ob_id, direction):
        if not request.user.is_staff:
            return HttpResponseForbidden("not enough privileges")
        ob = GalleryPicture.objects.get(id=ob_id)
        if direction == 'up':
            ob.up()
        else:
            ob.down()
        return redirect(ob.plugin.get_edit_url())

    def render(self, context, instance, placeholder):
        context.update({
            'auto_id': 'gallery_{}'.format(instance.pk),
            'row_class': instance.row_class,
            'cell_class': instance.cell_class,
            'img_class': instance.img_class,
            'items_per_row': instance.items_per_row,
            'objects_list': instance.pictures.select_related('image'),
            'show_on_popup': True,
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
