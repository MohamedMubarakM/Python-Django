from django.conf.urls import url
from .views import mubi_view1
from .views import mubi_view2
urlpatterns = [url('^one$', mubi_view1),
               url('^two$', mubi_view2),]
