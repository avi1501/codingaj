from django.db import models
from taggit.managers import TaggableManager


# Create your models here.


class dataType(models.Model):
    
    heading = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.heading

class QuestionDifficulty(models.Model):
    difficultylevel = models.CharField(max_length=100)

    def __str__(self):
        return self.difficultylevel


class questionModel(models.Model):
    problemstmt = models.CharField(max_length=100)
    description = models.TextField()
    datastructure = models.ForeignKey(dataType, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(QuestionDifficulty, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    tags = TaggableManager()

    def __str__(self):
        return self.problemstmt

    class Meta:
        ordering = ['created_on']

