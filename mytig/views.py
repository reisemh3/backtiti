from mytig.models import CoquillageListe, CrustaceListe, PoissonListe, ProduitEnPromotion
from django.http import JsonResponse
from django.http import Http404
from mytig.serializers import CoquillageSerializer, CrustaceSerializer, ProduitEnPromotionSerializer, PoissonSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.config import randomImageUrl
# from myImageBank.config import randomImageUrl

# Create your views here.


class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


class RedirectionDetailProduit(APIView):
    def get(self, pk):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        response = requests.get(baseUrl+'product/'+str(pk)+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

###################
#...TME2 starts...#
from rest_framework import renderers
from django.http import Http404

class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

import secrets
import json
from rest_framework.reverse import reverse

class ProduitImageRandom(APIView):
    renderer_classes = [JPEGRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, format=None):
        try:
            response = requests.get(secrets.choice(randomImageUrl))
            return Response(response)
        except:
            raise Http404

class ProduitImage(APIView):
    renderer_classes = [JPEGRenderer,renderers.JSONRenderer]
#Uncomment if images may iclude PNG
#    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, image_id, format=None):
        if image_id<0 or image_id>len(randomImageUrl):
            return Response({'detail': 'Not found.'}, content_type='application/json')
        try:
            response = requests.get(randomImageUrl[image_id])
            return Response(response)
        except:
            raise Http404
#...end of TME2...#
###################


###################
#...TME1 starts...#

# EXO 2


class RedirectionListeDeShipPoints(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


class RedirectionDetailShipPoint(APIView):
    def get(self, pk):
        try:
            response = requests.get(baseUrl+'shipPoint/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        response = requests.get(baseUrl+'shipPoint/'+str(pk)+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
# FIN EXO 2

# EXO 5


class ListeDePoissons(APIView):
    def get(self, request, format=None):
        res = []
        for prod in PoissonListe.objects.all():
            serializer = PoissonSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


# class RedirectionListeDePoisson(APIView):
#     def get_object(self, pk):
#         try:
#             return PoissonEnPromotion.objects.get(pk=pk)
#         except PoissonEnPromotion.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         prod = self.get_object(pk)
#         serializer = PoissonSerializer(prod)
#         response = requests.get(
#             baseUrl+'poisson/'+str(serializer.data['tigID'])+'/')
#         jsondata = response.json()
#         return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


class ListeDeCoquillages(APIView):
    def get(self, request, format=None):
        res = []
        for prod in CoquillageListe.objects.all():
            serializer = CoquillageSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


# class RedirectionListeDeCoquillage(APIView):
#     def get_object(self, pk):
#         try:
#             return CoquillageEnPromotion.objects.get(pk=pk)
#         except CoquillageEnPromotion.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         prod = self.get_object(pk)
#         serializer = CoquillageSerializer(prod)
#         response = requests.get(
#             baseUrl+'coquillage/'+str(serializer.data['tigID'])+'/')
#         jsondata = response.json()
#         return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


class ListeDeCrustaces(APIView):
    def get(self, request, format=None):
        res = []
        for prod in CrustaceListe.objects.all():
            serializer = CrustaceSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


# class RedirectionListeDeCrustace(APIView):
#     def get_object(self, pk):
#         try:
#             return CrustaceEnPromotion.objects.get(pk=pk)
#         except CrustaceEnPromotion.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         prod = self.get_object(pk)
#         serializer = CrustaceSerializer(prod)
#         response = requests.get(
#             baseUrl+'crustaces/'+str(serializer.data['tigID'])+'/')
#         jsondata = response.json()
#         return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
# FIN EXO 5

#...end of TME1...#
###################

from mytig.models import ProduitEnPromotion, ProduitDisponible
from mytig.serializers import ProduitEnPromotionSerializer, ProduitDisponibleSerializer

class AvailableList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitDisponible.objects.all():
            serializer = ProduitDisponibleSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


class AvailableDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitDisponible.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitDisponibleSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
    
class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"


class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
