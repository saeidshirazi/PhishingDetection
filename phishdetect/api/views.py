# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from rest_framework import viewsets,permissions,status,mixins,generics
from rest_framework.views import exception_handler,APIView
from .serializers import *
from rest_framework.exceptions import APIException
import django_filters
from django_filters import rest_framework as filters
import django_filters.rest_framework
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import WhiteListFilter
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    HTTP_200_OK
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListCreateAPIView
from django.views.decorators.http import require_http_methods,require_GET

#####################
# Whilelist View
#####################

class WhiteListViewSet(viewsets.ModelViewSet):
    queryset = WhiteList.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = WhiteListSerializer
    http_method_names = ['get',]    
    filter_class = WhiteListFilter




#####################
# BlackList View
#####################

class BlackListViewSet(viewsets.ModelViewSet):
    queryset = BlackList.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = BlackListSerializer
    http_method_names = ['post',]

#####################
# CONTACTUS View
#####################

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    http_method_names = ['get',]    
   