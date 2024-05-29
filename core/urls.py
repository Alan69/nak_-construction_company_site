from django.urls import path
from .views import index, about, service, blog, contact, blog_single, project, contact_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('project/', project, name='project'),
    path('blog_single/<int:id>/', blog_single, name='blog_single'),
    path('contact/', contact_view, name='contact'),
]