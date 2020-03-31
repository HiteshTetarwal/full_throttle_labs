import json
import time
from Activitylog import models
from django.core.management.base import BaseCommand, CommandError
from Activitylog.activity_save import activity_save

class Command(BaseCommand):
    help = 'Saves all the activities in the database'

    def handle(self, *args, **options):
        obj_user=models.ActivityPeriod.objects.all()
        print("UserID                        Name                  Location                        Activity_Start_Date                        Activity_End_Date")
        for r in obj_user:
            print(r.user.user_id,"            ",r.user.user_name,"            ",r.user.user_location,"            ",r.start_date,"            ",r.end_date)
