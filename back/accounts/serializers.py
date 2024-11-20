# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser  # CustomUser 모델 사용



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # 비밀번호는 선택적으로 입력 가능하게

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'subscribed_products']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            subscribed_products=validated_data.get('subscribed_products', '')
        )
        return user

    def update(self, instance, validated_data):
        # 사용자의 정보를 업데이트
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # 비밀번호가 있으면 set_password로 암호화하여 저장
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
    