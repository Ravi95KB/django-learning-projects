from django.db import models

# Create your models here.
class Topic(models.Model):  #Kind of a template for database table
    top_name = models.CharField(max_length=264,unique=True) #Defining a character field for topic name

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #Getting the key of Topic model.
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
