
from django.contrib import admin
from django.urls import path, include
from .views import pagina2, pagina1, home  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pagina1/', pagina1, name = 'pagina1'),
    path('pagina2/', pagina2, name='pagina2'),
    path('home/', home, name='home'),
    
   
]
