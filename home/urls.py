from django.contrib import admin
from django.urls import path

from home import views
urlpatterns = [
    path("", views.index,name="home"),
    path("home",views.index,name="home"),
    path("upload", views.upload,name="upload"),
    path("upload/", views.upload_receipt, name="upload"),
    path('upload-receipt/', views.upload_receipt, name='upload_receipt'),
    path("login", views.login, name="login"),   # ✅ fixed
    path('logout',views.logout,name="logout"),
    path("send-otp/", views.send_otp, name="send_otp"),
    # path("send-otp", views.send_otp_view, name="send_otp"),
    path("send-otp", views.send_otp, name="send_otp"),
    path("register/", views.register, name="register"),

    # path(signup='signup', view=views.index, name='signup'),
    path("services", views.services,name="services"),
    path("contact", views.contact,name="contact"),
    
        # Assuming the same view handles both
]
