from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=20, min_length=8, write_only=True)
    confirm_password = serializers.CharField(
        max_length=20, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255, min_length=4)
   
    class Meta:
        model = User

        fields = ['username', 'email','password','confirm_password']
        
        
    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ("The Email already exist")})
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
              raise serializers.ValidationError({'email':('password does not match')})

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class Loginserializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=4)
    password = serializers.CharField(
        max_length=20, min_length=8, write_only=True)
    
   
    
    class Mata:
        model = User
        fields = ['username', 'password']