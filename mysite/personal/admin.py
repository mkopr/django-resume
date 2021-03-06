from django.contrib import admin
from .models import WelcomeText, Academics, BasicInfo, Experience, Projects, \
    Skills




class AcademicsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('School info', {'fields': ['school_name', 'department', 'faculty',
                                    'logo_url']}),

        ('Date', {'fields': ['start_date', 'end_date']}),

        ('Info', {'fields': ['description']})
    ]


class BasicInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['first_name', 'last_name',
                                     'birth_date', 'city', 'photo_url', 'text']}),

        ('Contact info', {'fields': ['email', 'phone_number']}),

        ('Websites', {'fields': ['github_login', 'keybase_login', 'url_3',
                                 'pdf_url']})
    ]


class ExperienceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company info', {'fields': ['company_name', 'logo_url']}),

        ('Date', {'fields': ['start_date', 'end_date']}),

        ('Info', {'fields': ['position', 'responsibilities']})
    ]


class ProjectsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic info', {'fields': ['name', 'logo_url', 'URL']}),
        ('Date', {'fields': ['start_date', 'finish']}),
        ('Specific info', {'fields': ['language', 'technologies', 'device',
                                      'description']})
    ]

admin.site.register(WelcomeText)
admin.site.register(Academics, AcademicsAdmin)
admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skills)


