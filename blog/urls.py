from django.urls import path
from .views import blog, contact, index, projects


urlpatterns = [
    path('blog/', blog , name = 'blog'),
    path('contact/', contact , name = 'contact'),
    path('', index , name = 'index'),
    path('projects/', projects, name= 'projects')
]
