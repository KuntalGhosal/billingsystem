from django.urls import path

from billingInfo.views import BillingInfoView





urlpatterns = [
    path('',BillingInfoView.as_view()),
    path('<int:id>',BillingInfoView.as_view()),
]