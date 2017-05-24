from django.contrib import admin
from basic_info.models import BasicInfo


class BasicInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['first_name', 'last_name',
                                     'birth_date', 'city', 'photo_url', 'text']}),

        ('Contact info', {'fields': ['email', 'phone_number']}),

        ('Websites', {'fields': ['url_1', 'url_2', 'url_3']})
    ]

admin.site.register(BasicInfo, BasicInfoAdmin)
