from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import renderers
from django.http import JsonResponse
from django.http import Http404
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from myImageBank.config import baseUrl
from myImageBank.config import randomImageUrl

import json
from rest_framework.reverse import reverse

from mytig.views import JPEGRenderer


# Create your views here.


class RandomImage(APIView):
    renderer_classes = [JPEGRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, format=None):
        try:
            # response = requests.get(secrets.choice(randomImageUrl))
            projectUrl = reverse('projectRoot',request=request, format=format)
            response = requests.get(json.loads(requests.get(projectUrl+'myImage/random/').text)['url'])
            return Response(response)
        except:
            raise Http404

class Image(APIView):
    renderer_classes = [JPEGRenderer]
    # renderer_classes = [JPEGRenderer,renderers.JSONRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, image_id, format=None):
        # if image_id<0 or image_id>len(randomImageUrl):
        #     return Response({'detail': 'Not found.'}, content_type='application/json')
        # try:
        #     response = requests.get(randomImageUrl[image_id])
        try:
            projectUrl = reverse('projectRoot',request=request, format=format)
            response = requests.get(json.loads(requests.get(projectUrl+'myImage/'+str(image_id)+'/').text)['url'])
            return Response(response)
        except:
            raise Http404
        
#...end of TME2...#
###################