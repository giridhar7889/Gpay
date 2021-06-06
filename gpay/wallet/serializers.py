from rest_framework import serializers
from .models import Wallet
from users.models import NewUser


# class CreateWallet(serializers.ModelSerializer):
#     class Meta:
#         model = Wallet
#         fields = ('user', 'current_balance', 'created_at')
#
#     # def validate_user(self, data):
#     #     print(NewUser.objects.all())
#     #     # if data not in NewUser.objects.all():
#     #
#     # def create(self, validated_data):
#     #     return Wallet.objects.create(**validated_data)
#     #
#     # def update(self, instance, validated_data):
#     #     self.validate_user(validated_data.get('user', instance.user))
#     #
#     #     instance.current_balance = validated_data.get('current_balance', instance.current_balance)
#     #     instance.save()
#     #     return instance
