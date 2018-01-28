from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from pages.models import Candidate

from .pagination import StandardResultsPagination
from .serializers import CandidateModelSerializer



class CandidateCreateAPIView(generics.CreateAPIView):
    serializer_class = CandidateModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)


class  CandidateListAPIView(generics.ListAPIView):
    serializer_class = CandidateModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):    
        im_following=self.request.user.profile.get_following()
        qs1 = Candidate.objects.filter(userId__in=im_following).order_by('-pk')
        qs2 = Candidate.objects.filter(userId=self.request.user)
        qs = (qs1|qs2).distinct().order_by("-timestamp")
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
