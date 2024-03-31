from django.contrib import admin
from projects.models import projects
class projectAdmin(admin.ModelAdmin):
    list_display=('project_name','project_link')
admin.site.register(projects,projectAdmin)



# Register your models here.
