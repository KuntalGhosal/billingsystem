from django.urls import path

from shops.views import ShopView




urlpatterns = [
    path('',ShopView.as_view()),
    path('<int:id>',ShopView.as_view()),
    path('<str:name>',ShopView.as_view()),
]