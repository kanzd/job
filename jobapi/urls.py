from django.contrib import admin
from django.urls import path,include
from . import views
app_name='jobapi'
urlpatterns = [

    path('<slug:name>/<slug:passcode>/',views.UserApiSignUpView.as_view(),name='userSignup'),
    path('<slug:name>/<slug:location>/<slug:A>/<slug:B>',views.bookingApiView.as_view(),name='booking')
]
