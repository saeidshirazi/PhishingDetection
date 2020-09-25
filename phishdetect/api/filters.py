from .models import *
import django_filters
from django_filters import rest_framework as filters




#####################
# workstation filter
#####################

class WhiteListFilter(filters.FilterSet):
    
    class Meta:
        model = WhiteList
        fields = ['Url']
