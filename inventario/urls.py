from django.contrib import admin
from django.urls import path , include
import producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('producto.urls')),

]
