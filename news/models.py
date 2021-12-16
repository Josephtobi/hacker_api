from django.db import models

# Create your models here.

class News(models.Model):
  id1=models.IntegerField(primary_key=True)
  title=models.CharField(max_length=256,null=True)
  type1=models.CharField(max_length=256)
  url=models.CharField(max_length=256,null=True,blank=True)
  by=models.CharField(max_length=256)
  api=models.BooleanField(default=True)


class Comment(models.Model):
  id1=models.IntegerField(primary_key=True)
  text=models.CharField(max_length=256,null=True,blank=True)
  type1=models.CharField(max_length=256,null=True,blank=True)
  news=models.ForeignKey(to=News, on_delete=models.CASCADE)
  by=models.CharField(max_length=256,null=True,blank=True)

class SubComment(models.Model):
  id1=models.IntegerField()
  text=models.CharField(max_length=256,null=True,blank=True)
  type1=models.CharField(max_length=256,null=True,blank=True)
  comment=models.ForeignKey(to=Comment, on_delete=models.CASCADE)
  by=models.CharField(max_length=256,null=True,blank=True)



