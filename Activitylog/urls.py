from django.urls import path
from Activitylog import views

urlpatterns = [
    path('',views.save_activities, name="activity-home"),
    path('view_activities/',views.view_activities,name="view-activity"),
    path('add_activities/',views.add_activities,name="add-activity"),
    path('update_activities/',views.update_activity,name="update-activities"),
]