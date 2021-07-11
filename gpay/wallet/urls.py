from django.urls import path
from .views import create_wallet,transaction_deposit,transaction_withdraw,transaction_transfer

app_name = 'wallet'

urlpatterns = [
     path('create/',create_wallet.as_view(),name="create_wallet"),
     path('deposit/',transaction_deposit.as_view(),name="deposit"),
     path('withdraw/',transaction_withdraw.as_view(),name="withdraw"),
     path('transfer/',transaction_transfer.as_view(),name="transfer")




]