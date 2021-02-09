from django.conf.urls import url
from .views import mubi_view

urlpatterns = [url('', mubi_view),]
