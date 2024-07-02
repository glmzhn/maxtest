from django.contrib import admin
from .models import Query, ExternalServerResponse

admin.site.register(Query)
admin.site.register(ExternalServerResponse)
