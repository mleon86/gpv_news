from django.urls import path

from rest_framework import routers

from .viewsets import PostViewSet, AuthorViewSet

router = routers.SimpleRouter() #define las rutas para nuestros modeloes, la ruta get, post, patch y delete, entre otras
router.register('post', PostViewSet)
router.register('author', AuthorViewSet)

urlpatterns = router.urls
