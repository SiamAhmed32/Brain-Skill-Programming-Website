from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    course_categories = models.CharField(max_length=255)
    class Meta:
        ordering = ('course_categories',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.course_categories

class Item(models.Model):
    course_categories = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 255)
    description = models.TextField(blank=True, null= True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name= 'items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('course_categories',)

    def __str__(self):
        return self.course_name