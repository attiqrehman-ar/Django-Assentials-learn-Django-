from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


class MyNotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.MyNotes, MyNotesAdmin)