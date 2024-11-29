from django.urls import path,include
from.import views



urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("navbar/",views.navbar,name="navbar"),
    path("footer/",views.footer,name="footer"),
    path("about/",views.about,name="about"),
    path("iphone16/",views.iphone16,name="iphone16"),
    path("iphone16pro/",views.iphone16pro,name="iphone16pro"),
    path("register/",views.register,name="register"),
    path("iphone15/",views.iphone15,name="iphone15"),
    path("iphone14/",views.iphone14,name="iphone14"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("addtocart/",views.add_to_cart,name="addtocart"),
    path("payment/",views.payment,name="payment"),
]