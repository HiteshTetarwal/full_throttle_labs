from django.db import models

# Create your models here.
class Users(models.Model):
	user_name=models.CharField(max_length=30,null=True)
	user_location=models.CharField(max_length=30,null=True)
	user_id=models.CharField(max_length=9,null=True)

class ActivityPeriod(models.Model):
	start_date=models.DateTimeField(null=True)
	end_date=models.DateTimeField(null=True)
	user=models.ForeignKey(Users, on_delete=models.CASCADE)