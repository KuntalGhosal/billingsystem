from django.urls import path
from sellingitems.views import SellingItemsView




urlpatterns = [
    path('',SellingItemsView.as_view()),
    path('<int:id>',SellingItemsView.as_view()),
]