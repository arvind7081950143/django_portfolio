from django.contrib import admin
from skill.models import skill
class skilladmin(admin.ModelAdmin):
    list_display=['skill_img']
admin.site.register(skill,skilladmin)

# Register your models here.
