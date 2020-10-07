from django.urls import path

from rest_framework import routers

from .viewsets import PostViewSet, AuthorViewSet

from .views import home, noticias, eventos, legion, recursos, contacto, detallePost, Inicio

urlpatterns = [
	
	path('', Inicio.as_view(), name = 'index'),
    path('noticias/', noticias, name = 'noticias'),
    path('eventos/', eventos, name = 'eventos'),
    path('legion/', legion, name = 'legion'),
    path('recursos/', recursos, name = 'recursos'),
    path('contacto/', contacto, name = 'contacto'),

    path('<slug:slug>/',detallePost, name = 'detalle_post'),

]

#router = routers.SimpleRouter() #define las rutas para nuestros modeloes, la ruta get, post, patch y delete, entre otras
#router.register('post', PostViewSet)
#router.register('author', AuthorViewSet)

#urlpatterns = router.urls
