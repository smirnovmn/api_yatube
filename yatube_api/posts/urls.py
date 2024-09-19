from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from api.views import PostViewSet, CommentViewSet, GroupViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register('group', GroupViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
