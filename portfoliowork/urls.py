"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from portfolio.settings import STATIC_ROOT, STATIC_URL
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('Hire', views.Hire, name='Hire'),
    path('Contact', views.contact, name='Contact'),
    path('MoreSkills', views.moreSkills, name='MoreSkills'),
    path('certifications', views.certifications, name='certifications'),
    path('<str:Certificate_name>/certificationsDescription', views.certificationsDescription, name='certificationsDescription'),
    path('Experiences', views.Experiences, name='Experiences'),
    path('<str:Experience_name>/ExperiencesDescription', views.ExperiencesDescription, name='ExperiencesDescription'),
    path('Projects', views.Projects, name='Projects'),
    path('<str:Project_name>/ProjectsDescription', views.ProjectsDescription, name='ProjectsDescription'),
]


if settings.DEBUG:
    urlpatterns  +=  static(STATIC_URL, document_root=STATIC_ROOT)
