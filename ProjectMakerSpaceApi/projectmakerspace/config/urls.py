"""
URL configuration for the ProjectMakerSpace API.

Resource routes are added here as controllers are created, under the /api/ prefix.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
