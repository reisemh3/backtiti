from django.core.management.base import BaseCommand, CommandError
from myImageBank.models import ImageRandom
from myImageBank.serializers import ImageRandomSerializer
from myImageBank.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'myImage/random/')
        jsondata = response.json()
        ImageRandom.objects.all().delete()
        for product in jsondata:
            if product['id']:
                serializer = ImageRandomSerializer(data={'tigID':str(product['id'])})
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')
