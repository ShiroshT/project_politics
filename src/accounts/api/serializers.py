from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

from rest_framework import serializers

User = get_user_model()
class UserPublicDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]