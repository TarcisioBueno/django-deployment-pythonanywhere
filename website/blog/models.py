from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=500)
    accesses_number = models.IntegerField(default=0)
    seo_url_do_post = models.SlugField(max_length=500)
    img_post = models.URLField()
    thumbnail_post = models.TextField()
    keywords = models.CharField(max_length=1000)
    content = models.TextField()
    pub_date = models.DateField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Email(models.Model):
    email = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.email

