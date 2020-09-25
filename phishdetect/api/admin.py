# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ExportActionMixin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

admin.site.site_header = "PhishGaurd Admin"
admin.site.site_title = "PhishGaurd Admin Portal"


MyModels=[WhiteList,BlackList,ContactUs]
admin.site.register(MyModels)