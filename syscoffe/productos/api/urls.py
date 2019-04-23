from rest_framework.routers import DefaultRouter
from .views import CategoriaApiView, CategoriaDosApiView

router = DefaultRouter()
router.register(r'', CategoriaApiView, base_name="categoria")
router.register(r'', CategoriaDosApiView, base_name="categoria-dos")
urlpatterns = router.urls