from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    thumbnail=models.ImageField(upload_to='blogapp/images')
    publish_date=models.DateField(auto_now_add=True)
