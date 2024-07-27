from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', ),
    path('orders/', ),
    path('addorders/', ),
    path('orderslist/', ),
    path('exit/', ),
    path('registrations/', ),
]
