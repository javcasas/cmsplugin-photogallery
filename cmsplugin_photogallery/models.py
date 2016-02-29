from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField

from filer.fields.image import FilerImageField
from ordered_model.models import OrderedModel


class GalleryPlugin(CMSPlugin):
    row_class = models.CharField(_('Row CSS Class'), max_length=255, default='col-xs-12', blank=True)
    cell_class = models.CharField(_('Cell CSS Class'), max_length=255, default='col-xs-12 col-sm-6 col-lg-4', blank=True)
    img_class = models.CharField(_('Img CSS Class'), max_length=255, default='col-xs-12', blank=True)
    items_per_row = models.PositiveIntegerField(_('Images per row'), default=3)

    def __unicode__(self):
        return unicode(self.pk)

    def copy_relations(self, oldinstance):
        super(GalleryPlugin, self).copy_relations(oldinstance)
        for picture in oldinstance.pictures.all().iterator():
            picture.pk = None
            picture.plugin = self
            picture.save()


class GalleryPicture(OrderedModel):
    plugin = models.ForeignKey(GalleryPlugin, related_name='pictures')
    image = FilerImageField(verbose_name=_('Image'), related_name='+')
    alt_tag = models.CharField(_('Alt tag'), max_length=255, blank=True)
    text = models.TextField(verbose_name=_('Descriptive text'), blank=True)

    def __unicode__(self):
        return unicode(self.alt_tag)

    class Meta(OrderedModel.Meta):
        pass
