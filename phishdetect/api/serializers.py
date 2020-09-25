from .models import *
from rest_framework import serializers
import datetime
from django.contrib.auth.models import User

#####################
# Whitelist Serializer
#####################

class WhiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteList
        fields = ('id','Name','Url')

#####################
# BlackList Serializer
#####################

class BlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackList
        fields = ('id','Url')     

#####################
# contactus Serializer
#####################
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields = ("__all__")           