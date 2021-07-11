from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Wallet
from rest_framework.response import Response
from rest_framework import status, request
from users.models import NewUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .errors import InsufficientBalance

from .serializers import CreateWallet, CreateTransaction
from .models import Wallet, Transaction


class create_wallet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data['user']
        qs = NewUser.objects.get(email=user).id
        request.data["user"] = qs

        create_wallet_serializer = CreateWallet(data=request.data)
        print(create_wallet_serializer.is_valid())

        if create_wallet_serializer.is_valid():
            new_wallet = create_wallet_serializer.save()
            print(new_wallet)
            if new_wallet:
                return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class transaction_deposit(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.data['user']
        id_pk_user = NewUser.objects.get(email=user).id
        print(id_pk_user)

        wallet_name = request.data['wallet_name']
        id_pk_wallet = Wallet.objects.get(wallet_name=wallet_name).id
        wallet_instance = Wallet.objects.get(id=id_pk_wallet)
        print(wallet_instance)
        print(id_pk_wallet)

        # TRANSACTION CREATION FOR THAT DEPOSIT
        Transaction_data = {
            'wallet': id_pk_wallet,
            'value': request.data['deposit'],
            'running_balance': wallet_instance.current_balance
        }

        # WALLET UPDATE AFTER TRANSACTION
        wallet_data = {
            'user': id_pk_user,
            'wallet_name': request.data['wallet_name'],
            'current_balance': wallet_instance.current_balance + request.data['deposit']
        }
        transaction_serializer = CreateTransaction(data=Transaction_data)
        wallet_serializer = CreateWallet(wallet_instance, data=wallet_data)
        if transaction_serializer.is_valid():
            transaction = transaction_serializer.save()
            print(transaction)
            if wallet_serializer.is_valid():
                wallet_updated = wallet_serializer.save()
                print(wallet_updated)
                return Response(status=status.HTTP_201_CREATED, data=wallet_data)

        return Response(status=status.HTTP_201_CREATED, data={"key": "key"})


class transaction_withdraw(APIView):
    permission_classes = [IsAuthenticated]

    # def withdraw(self, value):
    #     if value > self.current_balance:
    #         raise InsufficientBalance("This wallet has insufficient balance ")
    #
    #     self.transaction_set.create(
    #         value=value,
    #         running_balance=self.current_balance - value
    #     )
    #     self.current_balance -= value
    #     self.save()
    #
    def post(self, request, *args, **kwargs):
        user = request.data['user']
        id_pk_user = NewUser.objects.get(email=user).id
        print(id_pk_user)

        wallet_name = request.data['wallet_name']
        id_pk_wallet = Wallet.objects.get(wallet_name=wallet_name).id
        wallet_instance = Wallet.objects.get(id=id_pk_wallet)
        print(wallet_instance)
        print(id_pk_wallet)
        if request.data['withdraw'] > wallet_instance.current_balance:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"key": "This wallet has insufficient balance "})

        # TRANSACTION CREATION FOR THAT WITHDRAWN AMOUNT
        Transaction_data = {
            'wallet': id_pk_wallet,
            'value': request.data['withdraw'],
            'running_balance': wallet_instance.current_balance
        }

        # WALLET UPDATE AFTER TRANSACTION
        wallet_data = {
            'user': id_pk_user,
            'wallet_name': request.data['wallet_name'],
            'current_balance': wallet_instance.current_balance - request.data['withdraw']
        }
        transaction_serializer = CreateTransaction(data=Transaction_data)
        wallet_serializer = CreateWallet(wallet_instance, data=wallet_data)
        if transaction_serializer.is_valid():
            transaction = transaction_serializer.save()
            print(transaction)
            if wallet_serializer.is_valid():
                wallet_updated = wallet_serializer.save()
                print(wallet_updated)
                return Response(status=status.HTTP_201_CREATED, data=wallet_data)

        return Response(status=status.HTTP_201_CREATED, data={"key": "key"})


class transaction_transfer(APIView):
    permission_classes = [IsAuthenticated]

    # def transfer(self,wallet,value):
    #     self.withdraw(wallet,value)
    #     wallet.deposit(value)

    def post(self, request, *args, **kwargs):
        request.data['withdraw'] = request.data['amount']
        withdraw_data = transaction_withdraw.post(request)
        request.data['deposit'] = request.data['amount']
        deposit_data = transaction_deposit.post(request)

        print(withdraw_data)
        print(deposit_data)
        return Response(status=status.HTTP_201_CREATED, data={"key": "key"})
