from rest_framework import serializers
from accounts.api.serializers import UserPublicDisplaySerializer
from pages.models import Candidate


class CandidateModelSerializer(serializers.ModelSerializer):
    userId = UserPublicDisplaySerializer(read_only=True) #it is also possible when needed to include write_only

    # date_display =serializers.SerializerMethodField()
    class Meta:
        model = Candidate
        fields = [
            'userId',
            'id_candidate',  
            'name_candidate', 
            'summary', 
            'descriptions'
        ]

#  a module - make sure to write it as get_field_name for example
    # def get_date_display