
from django.urls import path, re_path
from .views import (
    PostListApiView,
)

urlpatterns = [
    path('', PostListApiView.as_view(), name='post-list'),
    re_path(r'^(?P<pk>\d+)/$', PostListApiView.as_view(), name='post-detail'),
]