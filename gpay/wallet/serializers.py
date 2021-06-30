from rest_framework import serializers
from .models import Wallet,Transaction
from users.models import NewUser



class CreateWallet(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('wallet_name', 'current_balance', 'created_at', 'user')

    # def create(self, validated_data):
    #     return Wallet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     # self.validate_user(validated_data.get('user', instance.user))
    #
    #     instance.current_balance = validated_data.get('current_balance', instance.current_balance)
    #     instance.save()
    #     return instance


class CreateTransaction(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=('wallet','value','running_balance','created_at')

