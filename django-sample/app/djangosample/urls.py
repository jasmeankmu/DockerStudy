from django.contrib import admin
from django.urls import path

from api.views import api, database, message

urlpatterns = [
    path('api/database/', database),
    path('api/message/', message),
    path('api/other/', api),
    path('admin/', admin.site.urls),
]
