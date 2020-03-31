import json
import time
from Activitylog import models

obj_user=models.ActivityPeriod.objects.all()
for r in obj_user:
	print(r.user.user_name,r.start_date,r.end_date)