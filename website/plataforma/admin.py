from django.contrib import admin
from .models import Course,Category,Topic,Question,Word_list

class TopicInline(admin.StackedInline):
	model = Topic
	extra = 2

class CategoryInline(admin.StackedInline):
	model = Category
	extra = 2

class QuestionInline(admin.StackedInline):
	model = Question
	extra = 2


class CourseAdmin(admin.ModelAdmin):
	fieldsets = [

		('Course', {'fields':['course_title','link','status','image']}),

	]
	inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [

		('Category', {'fields':['category_title','category_number'],'classes':['collapse']}),

	]
	inlines = [TopicInline]
	

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [

		('Topic', {'fields':['topic_title','link','content'],'classes':['collapse']}),

	]
	inlines = [QuestionInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Word_list)
