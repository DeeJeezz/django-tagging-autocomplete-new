import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as lic:
    LICENSE = lic.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tagging-autocomplete-new',
    version='0.6',
    description='Autocompletion for django-tagging. Rebuild for Django 2.2. Original by Ludwik Trammer.',
    long_description=README,
    author='GrobIvanovich',
    author_email='killmaster00431@gmail.com',
    url='https://github.com/GrobIvanovich/django-tagging-autocomplete-new/',
    packages=find_packages(),
    include_package_data=True,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords=['Django',
              'Tags autocompletion',
    ],
)
