from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from pages import views

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^$', views.home, name='home'), # /api/tweet/s
    url(r'^candidate/(?P<candidate_name_slug>[\w\-]+)/$', views.candidate, name='candidate'), # New!
]

# url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)  # 
