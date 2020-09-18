from rest_framework import routers

from .viewsets import CursoViewSet, LeccionViewSet

router = routers.SimpleRouter() #define las rutas para nuestros modeloes, la ruta get, post, patch y delete, entre otras
router.register('curso', CursoViewSet)
router.register('leccion', LeccionViewSet)

urlpatterns = router.urls