from aplicacion_1.views import EventoViewSet, PersonaEPViewSet, PersonaViewSet
from rest_framework.routers import DefaultRouter

app_name = 'aplicacion_1'
router = DefaultRouter()

router.register(
    r'personas',
    PersonaViewSet,
    basename='personas'
)
router.register(
    r'personas-ep',
    PersonaEPViewSet,
    basename='personas-ep'
)
router.register(
    r'eventos',
    EventoViewSet,
    basename='eventos'
)

urlpatterns = [
]

urlpatterns += router.urls
