from django.shortcuts import render
from django.http import *
from django.shortcuts import *
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
from .serializers import *
from .models import *
import datetime
class UserApiSignUpView(APIView):
    def get(self,req,name,passcode):
        if not users.objects.filter(name=name):
         user=users()
         user.name=name
         user.passcode=passcode
         book=bookings()
         book.user=name
         user.save()
         book.save()
        user=users.objects.filter(name=name)
        serial=userApi(user,many=True)
        return Response(serial.data)
class bookingApiView(APIView):
    def get(self,req,name,location,A,B):



        if users.objects.filter(name=name):
            book=bookings.objects.filter(user=name)[0]
            book.Aloc=A
            book.Bloc=B
            book.location=location
            book.set_time(str(datetime.datetime.now()))
            book.set_pastbook('from '+A+' to '+B)
            book.set_near('delhi')
            book.set_near('nodia')
            book.save()
            bookSer=bookingApi(book)
            return Response(bookSer.data)
        else:
         return HttpResponse('User Not Found')