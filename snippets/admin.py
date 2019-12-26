from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.snippets)
class snippetsAdmin(admin.ModelAdmin):
    pass
