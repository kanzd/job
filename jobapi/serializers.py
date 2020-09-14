from . import models
from rest_framework import serializers


class userApi(serializers.ModelSerializer):
    class Meta:
        model=models.users
        fields='__all__'

class bookingApi(serializers.ModelSerializer):
    class Meta:
        model=models.bookings
        fields='__all__'

