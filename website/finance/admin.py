from django.contrib import admin
from accounts.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	fieldsets = [

		('Teacher', {'fields':['name','description','img']}),

	]


admin.site.register(Teacher, TeacherAdmin)