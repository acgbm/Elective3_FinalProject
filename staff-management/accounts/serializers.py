
from rest_framework import serializers
from fileupload.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    photo = serializers.ImageField(required=False, allow_null=True)


    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'photo']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_photo(self, photo):
        if photo:
            if photo.size > 2 * 1024 * 1024:
                raise serializers.ValidationError("Image size should not exceed 2MB.")
            if not photo.content_type in ['image/jpeg', 'image/png', 'image/webp']:
                raise serializers.ValidationError("Only JPEG, PNG, and WebP images are allowed.")
        return photo

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
