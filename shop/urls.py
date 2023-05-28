from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.loginhome, name = 'login'),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact, name = 'ContactUs'),
    path('tracker/', views.tracker, name = 'TrackingStatus'),
    path('search/', views.search, name = 'Search'),
    path('products/<int:myid>', views.products, name = 'products'),
    path('checkout/', views.checkout, name = 'Checkout'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('signup/', views.handlesignup, name="handlesignup"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('logout/', views.handleLogout, name="handleLogout"),

]