from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Keyword, SearchResult

admin.site.register(Keyword) #admin access to add or remove keywords
