from django.contrib import admin
from .models import Certif

class CertifAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Certif, CertifAdmin)
