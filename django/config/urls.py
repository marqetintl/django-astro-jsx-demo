"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView


DEBUG = getattr(settings, 'DEBUG', False)


class IndexView(TemplateView):
    template_name = 'astro/index.html'


class AboutView(TemplateView):
    template_name = 'astro/about.html'


class BlogsView(TemplateView):
    template_name = 'astro/blog.html'


class BlogView(TemplateView):
    def get_template_names(self):
        return [f'astro/blog/{self.kwargs["slug"]}.html', 'astro/404.html']


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<slug:slug>/', BlogView.as_view(), name='blog'),
    path('blog/', BlogsView.as_view(), name='blogs'),
    path('about/', AboutView.as_view(), name='about'),
    path('', IndexView.as_view(), name='index'),
]

if DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
