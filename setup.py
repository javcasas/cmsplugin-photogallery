import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cmsplugin-photogallery',
    url='https://github.com/javcasas/cmsplugin-photogallery',
    version='0.0.2',
    description='A simple app to create DjangoCMS photo galleries.',
    long_description=README,
    install_requires=[
        'django-cms>=2.4.3',
        'cmsplugin-filer>=0.9.5',
        'django-ordered-model>=0.1.5',
    ],
    dependency_links=[
        'git+https://github.com/bfirsh/django-ordered-model.git@1.1.0#egg=django-orderedmodel-1.1.0',
    ],
    packages=find_packages(),
    package_data={'': ['license.txt']},
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
