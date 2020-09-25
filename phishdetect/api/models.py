# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

######################
# Whitelist CLASS
###################### 
class WhiteList(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    Name =  models.CharField(max_length=100, default='')
    Url =  models.URLField(default="https://shaparak.ir/", max_length=200,blank=False,null=False)
    def __str__(self):
        return self.Name


######################
# Blacklist CLASS
###################### 
class BlackList(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    Url =  models.URLField(default="https://shaparak.ir/", max_length=200,blank=False,null=False)
    def __str__(self):
        return self.Url

######################
# CONTATCT US CLASS
######################        
class ContactUs(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    contact_name=models.CharField(max_length=100, default='')
    url_tel =  models.URLField(default="https://t.me/mahana_app", max_length=200)
    url_ins =  models.URLField(default="www.instagram.com/ego_official2018", max_length=200)
    url_site = models.URLField(default="https://www.danapco.com/", max_length=200)
    phone_number = PhoneNumberField(default='+989010979406')


    class Meta:
        ordering = ('-created',)
        verbose_name=('Contact Us')
        verbose_name_plural=('Contact Us')

    def __str__(self):
        return str(self.contact_name) 