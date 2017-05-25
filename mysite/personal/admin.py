from django.contrib import admin
from personal.models import WelcomeText
from personal.models import Academics
from personal.models import BasicInfo
from personal.models import Experience
from personal.models import Projects
from personal.models import Skills



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

        ('Websites', {'fields': ['github', 'keybase', 'url_3', 'pdf_url']})
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


