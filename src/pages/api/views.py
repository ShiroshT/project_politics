from rest_framework import generics

from pages.models import Candidate
from .serializers import CandidateModelSerializer

class  CandidateListAPIView(generics.ListAPIView):
    serializer_class = CandidateModelSerializer


    def get_queryset(self):
        return Candidate.objects.all()
