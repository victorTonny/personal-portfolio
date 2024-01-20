from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.detail_page, name='detail_page'),
    path('contact/', views.contact_form, name='contact_form'),
    path('demo/', views.demo, name='demo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)