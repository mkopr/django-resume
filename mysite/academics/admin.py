from django.contrib import admin
from academics.models import Academics


class AcademicsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('School info', {'fields': ['school_name', 'department', 'faculty',
                                    'logo_url']}),

        ('Date', {'fields': ['start_date', 'end_date']}),

        ('Info', {'fields': ['description']})
    ]

admin.site.register(Academics, AcademicsAdmin)
