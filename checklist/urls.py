
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version="v1",
        description="API for all things ...",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('accounts.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    # path('openapi/', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),

    # path('', TemplateView.as_view(
    #     template_name='doc.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='api_doc'),
]
