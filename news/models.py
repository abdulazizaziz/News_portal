from django.db import models
from admin_panel.models import Users

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_post = models.IntegerField()

    def __str__(self):
        return self.category_name + " - " + str(self.category_post)
    
    class Meta:
        db_table = 'Category'
        ordering = ['id']
  

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    img = models.ImageField(upload_to="images", blank=True, null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title + " - " + self.category.category_name

    class Meta:
        db_table = 'Post'
        ordering = ['-post_date']