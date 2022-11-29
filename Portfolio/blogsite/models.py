from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse



# Create your models here.
class About(models.Model):
    heading=models.CharField(max_length=50)
    career=models.CharField(max_length=55)
    description=models.TextField(blank=False)
    profile_img=models.ImageField(upload_to='static/img')
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about=models.ForeignKey(About, on_delete=models.CASCADE)
    social_name=models.CharField(max_length=30)
    link=models.URLField(max_length=200)



#blogs_post
class blog_post(models.Model):
    title=models.CharField(max_length=100, blank=False)
    slug=models.SlugField(max_length=100)
    author=models.CharField(max_length=50)
    image=ResizedImageField(size=[500, 300], crop=['middle', 'center'], upload_to='static/img')
    description=models.TextField()
    post_time=models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    category_name=models.CharField(max_length=50, blank=False)
    category_slug=models.SlugField(max_length=30, unique=True)

    def get_url(self):
        return reverse("image_by_category", args=[self.category_slug])
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image_name=models.CharField(max_length=100, blank=False)
    image_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image_slug=models.SlugField(max_length=30)
    image_size=ResizedImageField(size=[500, 300], crop=['middle', 'center'], upload_to='static/img')


class Contact(models.Model):
    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    email=models.EmailField()
    message=models.TextField()
    