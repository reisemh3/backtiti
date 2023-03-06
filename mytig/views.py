from mytig.models import CoquillageListe, CrustaceListe, PoissonListe, ProduitEnPromotion
from django.http import JsonResponse
from django.http import Http404
from mytig.serializers import CoquillageSerializer, CrustaceSerializer, ProduitEnPromotionSerializer, PoissonSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl

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


class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(
                baseUrl+'product/'+str(serializer.data['tigID'])+'/')
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
        response = requests.get(
            baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"
