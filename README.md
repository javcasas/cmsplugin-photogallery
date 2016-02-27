# DjangoCMS Photo Gallery

This app needs:
- [django-cms](https://github.com/divio/django-cms) (obviously)
- [cmsplugin-filer](https://github.com/stefanfoulis/cmsplugin-filer)
- [django-orderedmodel](https://github.com/bfirsh/django-orderedmodel)



## SetUp

    pip install git+git://github.com/javcasas/cmsplugin-photogallery.git


You should have these in installed apps:

    INSTALLED_APPS = (
        .....
        'easy_thumbnails',
        .....
        'filer',
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        .....
        'ordered_model',
        'cmsplugin_gallery',
    )

And these in THUMBNAIL\_PROCESSORS

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

Run the migrations

    python manage.py migrate filer
    python manage.py migrate cmsplugin_gallery
