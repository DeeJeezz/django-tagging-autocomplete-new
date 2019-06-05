import os
from setuptools import find_packages, setup
from readme_renderer import markdown

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tagging-autocomplete-new',
    version='0.6.1',
    description="Autocompletion for django-tagging. Rebuild for Django 2.2. Original by Ludwik Trammer.",
    long_description=markdown.clean(README),
    long_description_content_type="text/markdown",
    author='GrobIvanovich',
    author_email='killmaster00431@gmail.com',
    url='https://github.com/GrobIvanovich/django-tagging-autocomplete-new/',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 2.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'Django',
        'Tags autocompletion',
    ],
)
