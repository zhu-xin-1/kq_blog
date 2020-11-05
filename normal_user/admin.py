from django.contrib import admin
from normal_user.models import normal_user,Authority,Student_detail,Sudent_class
# Register your models here.
admin.site.register(normal_user)
admin.site.register(Authority)
admin.site.register(Student_detail)
admin.site.register(Sudent_class)