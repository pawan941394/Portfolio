from django.contrib import admin

from .models import Experience,  Certificate, Contact, Hiring, Mycv, Project,abousUs,Skill, service_name
# Register your models here.

admin.site.register(abousUs)
admin.site.register(Skill)
admin.site.register(service_name)
admin.site.register(Hiring)
admin.site.register(Mycv)
admin.site.register(Contact)
@admin.register(Project)

class Project(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
@admin.register(Certificate)

class Project(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
@admin.register(Experience)

class Experience(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)