from django.db import models

# Create your models here.
class AppDetails(models.Model):
	userId = models.CharField(max_length=50)
	app = models.CharField(max_length=30)
	timestamp = models.CharField(max_length=50)

	def __str__(self):
		return self.userId



class UserDetails(models.Model):
	userId = models.CharField(max_length=50)
	app_launched = models.IntegerField(null=True,blank=True)
	most_active_day_last_7_days = models.CharField(max_length=15)
	number_of_days_active_last_7_days = models.IntegerField(null=True,blank=True)
	most_launched_app_last_7_days = models.CharField(max_length=30)

	def __str__(self):
		return self.userId