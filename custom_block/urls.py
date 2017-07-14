from django.conf.urls import url
from views import CustomImageList, CustomImageCreate, CustomImageUpdate, CustomImageDelete

urlpatterns = [
    url(r'^$', CustomImageList.as_view(), name='custom-image-list'),
    url(r'^add/$', CustomImageCreate.as_view(), name='custom-image-add'),
    url(r'^(?P<pk>[0-9]+)/$', CustomImageUpdate.as_view(), name='custom-image-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', CustomImageDelete.as_view(), name='custom-image-delete'),
]