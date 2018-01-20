
from django.db.models import Q
from rest_framework import generics

from pages.models import Candidate
from .serializers import CandidateModelSerializer

class  CandidateListAPIView(generics.ListAPIView):
    serializer_class = CandidateModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Candidate.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            query = query.strip()
            qs = qs.filter(
                Q(name_candidate__icontains=query) |
                Q(userId__username__icontains=query) |
                Q(summary__icontains=query)|
                Q(descriptions__icontains=query)
            )
        return qs 

    # def get_queryset(self):
    #     return Candidate.objects.all()



