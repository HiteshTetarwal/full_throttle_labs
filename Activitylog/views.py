import json
from Activitylog import models
from datetime import datetime
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def view_activities(request):
	# obj_user=models.ActivityPeriod.objects.all()
	# activities=[]
	# for r in obj_user:
	# 	activities.append([r.user.user_id,r.user.user_name,r.user.user_location,r.start_date,r.end_date])

	activities={
		"activities":models.ActivityPeriod.objects.all()
	}

	return render(request, 'Activitylog/view_activities.html', activities)


@csrf_exempt
def update_activity(request):
	status=True
	# status=False
	user_id				=	request.POST.get('id')
	user_name			=	request.POST.get('real_name')
	user_location		=	request.POST.get('location')
	start_date			=	request.POST.get('start_date')
	end_date			=	request.POST.get('end_date')
	print("============================",start_date,user_id,user_name,end_date,user_location)
	#add user to database
	user_ob               = models.Users()
	user_ob.user_name     = user_name
	user_ob.user_id       = user_id
	user_ob.user_location = user_location
	user_ob.save()

	#make activity record now
	activity = models.ActivityPeriod()
	#convert below dates to datetime instance in python using strptime
	activity.start_date = datetime.strptime(start_date,'%m/%d/%Y')
	activity.end_date   = datetime.strptime(end_date,'%m/%d/%Y')
	activity.user = user_ob
	activity.save()

	print("added successfully")
	alert_status={
		"status" : status,
	}

	return	render(request,'Activitylog/add_activity.html',alert_status)



@csrf_exempt
def add_activities(request):

	return render(request, 'Activitylog/add_activity.html')


def do_it():
	with open('Test_JSON.json') as f:
		data=json.load(f)

	for member in data['members']:
		count=0
		member_id = member['id']

		user_ob = models.Users.objects.filter(user_id=member_id)

		if user_ob.count() > 0:
			#already in table
			user_ob = user_ob.first()
		else:
			#does not exists in database
			user_ob               = models.Users()
			user_ob.user_name     = member['real_name']
			user_ob.user_id       = member['id']
			user_ob.user_location = member['tz']
			user_ob.save()

			#make activity record now

			for acts in member['activity_periods']:
				activity = models.ActivityPeriod()
				#convert below dates to datetime instance in python using strptime
				activity.start_date = datetime.strptime(acts['start_time'],'%b %d %Y %H:%M%p')
				activity.end_date   = datetime.strptime(acts['end_time'],'%b %d %Y %H:%M%p')
				activity.user = user_ob
				activity.save()



def save_activities(request):
	do_it()
	return render(request, 'Activitylog/home.html')