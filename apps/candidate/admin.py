from django.contrib import admin

from .models import Party, Candidate

admin.site.register([Party, Candidate])
