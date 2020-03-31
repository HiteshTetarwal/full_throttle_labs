from django.core.management.base import BaseCommand, CommandError
from Activitylog import views

class Command(BaseCommand):
    help = 'Saves all the activities in the database'

    def handle(self, *args, **options):
        print("Saving Activities for users.....")
        try:
            views.do_it()
        except RuntimeWarning:
        	print('----')
        print("Activities Saved")