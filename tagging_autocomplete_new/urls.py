from django.urls import path
from .views import list_tags
urlpatterns = [
    path('list/', list_tags, name='tagging_autocomplete_new-list'),
]

