from django.db import models

# Create your models here.
#backede 



class Room(models.Model):
	image=models.ImageField(null=True, blank=True, upload_to="rooms_images/")
	availibility = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	rent = models.CharField(max_length=30)
	owner_number = models.CharField(max_length=30)
	owner_name = models.CharField(max_length=30)


	def __str__(self):
		return self.location