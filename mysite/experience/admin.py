from django.contrib import admin
from experience.models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company info', {'fields': ['company_name', 'logo_url']}),

        ('Date', {'fields': ['start_date', 'end_date']}),

        ('Info', {'fields': ['position', 'responsibilities']})
    ]

admin.site.register(Experience, ExperienceAdmin)
