from django.contrib import admin
from django.urls import path
from core.views import index_view, experience_view, avatar_view, dashboard_view, education_view, contact_view
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),

    # Index
    path('', index_view.index),

    # Menu
    path('experiences/', experience_view.list_experiences),
    path('experiences/<id>/', experience_view.experience_item),

    # Avatar
    path('signin_page/', avatar_view.signin_page),
    path('signin', avatar_view.signin),
    path('signout/', avatar_view.signout),

    # Dashboard
    path('dashboard/', dashboard_view.dashboard),

    # Education
    path('education/', education_view.education),
    path('education/courses/', education_view.courses),
    path('education/courses/<id>/', education_view.course_item),


    # Contacts
    path('contacts/', contact_view.contact),
    path('contacts/send', contact_view.contact_send)

    

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
