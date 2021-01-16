from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Exfd(models.Model):
	g =[('M','Male'),('FM','FeMale'),('Others','Others')]
	clg = [('IIIT','IIIT Nuzvid'),('IIIT',"IIIT Basara"),('IIIT',"IIIT Ongole")]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(choices=g,max_length=10)
	rollno = models.CharField(max_length=10)
	collegename = models.CharField( max_length= 7,choices=clg)
	impf = models.ImageField(upload_to="Profile/",default="background1.jpg")


@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class South(models.Model):
	g = [('al','Vada'),('ab','Wheat upma')]
	item= models.CharField(max_length=200,choices=g)
	price= models.IntegerField(null=True)
	quantity = models.IntegerField(null=True)
	category = models.CharField(max_length=10)




class Work(models.Model):
	wks = [('yes','completed'),('no','Not completed')]
	date = models.DateField()
	description = models.TextField()
	workstatus = models.CharField(max_length=5,choices=wks)
	m= models.ForeignKey(User,on_delete=models.CASCADE)




