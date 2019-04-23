from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Syscoffe Api",
        default_version='v1',
        description="API REST DEL PROYECTO SYSCOFFE DEL CURSO",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jose@upcodemy.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)