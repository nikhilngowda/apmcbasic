from django.urls import path
from . import views

urlpatterns = [
    path('sales', views.sales, name="sales"),
    path('add-sale', views.add_sale, name="add-sale"),
    path('add-profile', views.accountSettings, name="add-profile"),

    path('profile', views.accindex, name="profile"),
    path('edit-profile', views.EditAcc, name="edit-profile"),
]