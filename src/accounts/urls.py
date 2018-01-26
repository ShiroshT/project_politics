from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    UserDetailView
)


urlpatterns = [
    #  url(r'^$', RedirectView.as_view(url='/')), 
    #  url(r'^search/$', CandidateListView.as_view(), name='candidatelist'), 
    #  url(r'^create/$', CandidateCreateView.as_view(), name='createcandiate'), 
    #  url(r'^(?P<pk>\d+)/edit/$', CandidateUpdateView.as_view(), name='updatecandaite'), 
    #  url(r'^(?P<pk>\d+)/delete/$', CandidateDeleteView.as_view(), name='deletecandaite'), 
     url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detailcandidate'), 
#     # url(r'^$', RedirectView.as_view(url="/")), 
#     # url(r'^$', RedirectView.as_view(url="/")), 
#     url(r'^$', views.home, name='home'), # /api/tweet/s
#     # url(r'^add_candidate/$', views.add_candidate, name='add_candidate'), # NEW MAPPING!
#     # url(r'^candidate/(?P<candidate_name_slug>[\w\-]+)/$', views.candidate, name='candidate'), # New!
#     # url(r'^results/$', views.candiate_search, name='results'), # New!
#     # url(r'^test/$', views.CandidateList.as_view(), name='test'), # New!
]

# url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)  # 
