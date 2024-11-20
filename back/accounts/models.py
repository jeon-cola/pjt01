# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    subscribed_products = models.TextField(blank=True, null=True)  # 가입한 상품 목록 (쉼표로 구분된 문자열)

    def __str__(self):
        return self.username