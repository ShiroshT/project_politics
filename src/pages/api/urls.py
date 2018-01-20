from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CandidateCreateAPIView,
    CandidateListAPIView
    # CandidateDeleteView,
    # CandidateListView, 
    # CandidateDetailView, 
    # CandidateCreateView,
    # CandidateUpdateView
)


urlpatterns = [
     url(r'^create/$',CandidateCreateAPIView.as_view(), name='candidatelist'), # /api/candidates
     url(r'^$', CandidateListAPIView.as_view(), name='candidatelist'), # /api/candidates
    #  url(r'^$', RedirectView.as_view(url='/')), 
    #  url(r'^search/$', CandidateListView.as_view(), name='candidatelist'), 
    #  url(r'^create/$', CandidateCreateView.as_view(), name='createcandiate'), 
    #  url(r'^(?P<pk>\d+)/edit/$', CandidateUpdateView.as_view(), name='updatecandaite'), 
    #  url(r'^(?P<pk>\d+)/delete/$', CandidateDeleteView.as_view(), name='deletecandaite'), 
    #  url(r'^(?P<pk>\d+)/$', CandidateDetailView.as_view(), name='detailcandidate'), 

]



