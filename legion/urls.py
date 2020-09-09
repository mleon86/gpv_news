from rest_framework import routers

from .viewsets import OrganizacionViewSet, PersonaViewSet

router = routers.SimpleRouter() #define las rutas para nuestros modeloes, la ruta get, post, patch y delete, entre otras
router.register('organizaciones', OrganizacionViewSet)
router.register('personas', PersonaViewSet)

urlpatterns = router.urls
