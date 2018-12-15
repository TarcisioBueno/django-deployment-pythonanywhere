from django.db import models

class Course(models.Model):
	course_title = models.CharField(max_length=300)
	link = models.SlugField(max_length=500)
	status = models.CharField(max_length=200)
	image = models.URLField(max_length=500)

	def __str__(self):
		return self.course_title

class Category(models.Model):
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	category_title = models.CharField(max_length=300)
	category_number = models.IntegerField()

	def __str__(self):
		return self.category_title

class Topic(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	topic_title = models.CharField(max_length=500)
	link = models.SlugField(max_length=500)
	content = models.TextField()

	def __str__(self):
		return self.topic_title

class Question(models.Model):
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	question_number = models.IntegerField()
	question_text = models.CharField(max_length=500)
	right_option = models.CharField(max_length=500)
	option1 = models.CharField(max_length=500)
	option2 = models.CharField(max_length=500)
	option3 = models.CharField(max_length=500)
	option4 = models.CharField(max_length=500)
	option5 = models.CharField(max_length=500)

	def __str__(self):
		return self.topic.topic_title + " - " + self.question_text

class Word_list(models.Model):
	list_name = models.CharField(max_length=200)
	list_date = models.DateField()
	list_content = models.TextField()

	def __str__(self):
		return self.list_name




