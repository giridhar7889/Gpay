from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Wallet
from rest_framework.response import Response
from rest_framework import status, request

#
# # from .serializers import CreateWallet
# from .models import Wallet, Transaction
#
#
# class create_wallet(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         user = request.user
#
#         create_wallet_serializer = CreateWallet(data=request.data)
#         print(request.data)
#         if create_wallet_serializer.is_valid():
#             new_wallet = create_wallet_serializer.save()
#             print(new_wallet)
#             if new_wallet:
#                 return Response(status=status.HTTP_201_CREATED)
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# # class transaction(APIView):
# #     permission_classes = [AllowAny]
# #
# #     def get(self, request):
# #         print(request.query_params)
# #         print(request.auth)
# #         user = Wallet.objects.get(user="giridhar@gmail.com")
# #         print(user)
# #
# #         python_data = {'user': 'giridhar@gmail.com', 'current_balance': 2399.0}
# #         de_serializer = CreateWallet(user,data=python_data)
#
#         print(de_serializer.is_valid())
#         print(de_serializer.validated_data)
#         new_wallet = de_serializer.save()
#         print(new_wallet)
#
#
#
#
#        # balance = {"balance": user.current_balance}
#
#         return Response( status=status.HTTP_200_OK)
