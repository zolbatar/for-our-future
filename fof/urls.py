from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('broker.urls', namespace='broker')),
    path('admin/', admin.site.urls),
]
