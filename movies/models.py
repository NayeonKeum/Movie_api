from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    genre=models.CharField(max_length=15)
    year=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, help_text="post created date")
    updated_at = models.DateTimeField(auto_now=True, help_text="post updated date")

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-updated_at']
