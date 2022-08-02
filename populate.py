import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'pro_two.settings')

import random
from faker import Faker

import django
django.setup()

from app_two.models import Topic, Webpage, AccessRecord

fakeGen = Faker()


def add_topic():
    topics = ['Search', 'Social', 'Maths']
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        name = fakeGen.company()
        url = fakeGen.url()
        date = fakeGen.date()

        webpg = Webpage.objects.get_or_create(topic=top, name=name, url=url)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=date)[0]


if __name__ == '__main__':
    print("populating...")
    populate()
    print("populated!")
