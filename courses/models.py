from django.db import models

# Create your models here.




class Question(models.Model):
    text = models.CharField(max_length=255)
    hint = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='modules', default=1)

    def __str__(self):
        return self.text

