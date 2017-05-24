from django.contrib import admin
from projects.models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic info', {'fields': ['name', 'logo_url', 'URL']}),
        ('Date', {'fields': ['start_date', 'finish']}),
        ('Specific info', {'fields': ['language', 'technologies', 'device',
                                      'description']})
    ]

admin.site.register(Projects, ProjectsAdmin)
