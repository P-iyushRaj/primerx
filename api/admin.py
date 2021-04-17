from django.contrib import admin

# Register your models here.
from .models import primerx_field_model

@admin.register(primerx_field_model)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'prime_first_name']