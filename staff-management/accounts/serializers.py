
from rest_framework import serializers

from fileupload.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)



    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}



    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(username=validated_data['username'])
        user.set_password(password)
        user.save()
        return user
