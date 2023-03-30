from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Creates a Superuser for Admin at worksnet'

    def handle(self, *args, **options):
        try:
            get_user_model().objects.get(username='admin@example.com')
            self.stdout.write(self.style.WARNING('User Exist.'))
        except get_user_model().DoesNotExist:
            get_user_model()(username='admin@example.com', email='admin@example.com', password=make_password("hello"),
                is_superuser=True, is_staff=True, first_name='Admin', last_name='User').save()
            self.stdout.write(self.style.SUCCESS('User Created Successfully.'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'Something Went Wrong. Error : {err}'))
