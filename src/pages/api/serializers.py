from rest_framework import serializers
from accounts.api.serializers import UserPublicDisplaySerializer
from pages.models import Candidate


class CandidateModelSerializer(serializers.ModelSerializer):
    userId = UserPublicDisplaySerializer()
    class Meta:
        model = Candidate
        fields = [
            'userId',
            'id_candidate',  
            'name_candidate', 
            'summary', 
            'descriptions'
        ]