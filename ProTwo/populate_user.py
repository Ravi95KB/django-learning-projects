import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=10):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email_id = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email_id)[0]

if __name__ == "__main__":
    print("Populating fake users")
    populate(30)
    print("Populated fake users!")
