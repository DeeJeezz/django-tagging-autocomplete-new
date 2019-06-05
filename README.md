# django-tagging-autocomplete-new

![pypi](https://img.shields.io/pypi/v/django-tagging-autocomplete-new.svg)
![github_version](https://img.shields.io/github/release/grobivanovich/django-tagging-autocomplete-new.svg)
![license](https://img.shields.io/github/license/GrobIvanovich/django-tagging-autocomplete-new.svg)
![wheel](https://img.shields.io/pypi/wheel/django-tagging-autocomplete-new.svg)
![python](https://img.shields.io/pypi/pyversions/django-tagging-autocomplete-new.svg)

django-tagging-autocomplete-new is a jquery based autocomplete solution for
django-tagging.

This is fixed version of [django-tagging-autocomplete](https://github.com/ludwiktrammer/django-tagging-autocomplete) by @ludwiktrammer for Django 2.2.

### Requirements

```python
django-tagging
```

### Setup

1. Install package from PyPI:
```python
pip install django-tagging-autocomplete-new
```
2. Add `tagging` and `tagging-autocomplete-new` to installed apps in your's project's settings:
```python
INSTALLED_APPS = [
    ...
    'tagging',
    'tagging_autocomplete',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    ...
]
```
3. Add route to your project's `urls.py` file:
```python
path('tagging_autocomplete/', include('tagging_autocomplete.urls'))
```

### Usage

#### The Model Field

You can use `TagAutocompleteField()` to enable autocompletion right in your
`models.py`. In most cases this is the easiest solution:
```python
    from django.db import models
    from tagging_autocomplete.models import TagAutocompleteField

    class SomeModel(models.Model):
            tags = TagAutocompleteField()
```

#### The Form Widget

Alternatively you can use the `TagAutocomplete()` form widget while creating
your form:
```python
    from django import forms
    from tagging.forms import TagField
    from tagging_autocomplete.widgets import TagAutocomplete

    class SomeForm(forms.Form):
        tags = TagField(widget=TagAutocomplete())
```

#### Optional settings

By default the maximum number of results suggested by the autocompletion is 100.
You can modify this number by adding to your `settings.py` project file
the `TAGGING_AUTOCOMPLETE_MAX_RESULTS` constant.
For example:
```python
    TAGGING_AUTOCOMPLETE_MAX_RESULTS = 5
```

By default autocompletion suggests tags that *start with* a given term.
In case you need to show ones that *contain* the given term,
set `TAGGING_AUTOCOMPLETE_SEARCH_CONTAINS` to `True`.
For example:
```python
    TAGGING_AUTOCOMPLETE_SEARCH_CONTAINS = True
```
By default suggestions are shown right after you enter first character.
You can configure this behaviour using `TAGGING_AUTOCOMPLETE_MIN_LENGTH`.
For example:
```python
    TAGGING_AUTOCOMPLETE_MIN_LENGTH = 3
```
