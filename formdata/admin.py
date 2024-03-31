from django.contrib import admin
from formdata.models import formdata
class formAdmit(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(formdata,formAdmit)

# Register your models here.
