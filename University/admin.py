from django.contrib import admin
from .models import UniversityModel
# Register your models here.

class UniverAdmin(admin.ModelAdmin):

    list_display = ('name','when_created','Who_created','photo','university_bio','location','contact_with_admin')
    search_fields = ['name','university_bio',]

admin.site.register(UniversityModel,UniverAdmin)
