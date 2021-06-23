from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker", views.tracker, name="Tracker"),
    path("search", views.search, name="Search"),

    path('product/<int:myid>', views.prodView, name="prodview"),
    path("checkout", views.checkout, name="Checkout"),
    path("add_in_cart/", views.add_in_cart, name="add_in_cart"),
    path("popover/", views.popover, name="popover"),
]