from django.contrib import admin
from django.urls import path
from core.views import index_view, experiences_view, avatar_view, dashboard_view, education_view
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),

    # Index
    path('', index_view.index),

    # Menu
    path('experiences/', experiences_view.list_experiences),
    path('experiences/<id>/', experiences_view.item_experience),

    # Avatar
    path('signin_page/', avatar_view.signin_page),
    path('signin', avatar_view.signin),
    path('signout/', avatar_view.signout),

    # Dashboard
    path('dashboard/', dashboard_view.dashboard),

    # Education
    path('education/', education_view.education),
    path('education/courses/', education_view.courses)


    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
