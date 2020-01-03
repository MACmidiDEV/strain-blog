from django.conf.urls import url, include
from .views import all_strains

urlpatterns = [
    url(r'^$', all_strains, name='strains'),
]