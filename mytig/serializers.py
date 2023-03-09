from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion, ProduitDisponible, PoissonListe, CoquillageListe, CrustaceListe


class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')

class ProduitDisponibleSerializer(ModelSerializer):
    class Meta:
        model = ProduitDisponible
        fields = ('id', 'tigID')


class PoissonSerializer(ModelSerializer):
    class Meta:
        model = PoissonListe
        fields = ('id', 'tigID')


class CoquillageSerializer(ModelSerializer):
    class Meta:
        model = CoquillageListe
        fields = ('id', 'tigID')


class CrustaceSerializer(ModelSerializer):
    class Meta:
        model = CrustaceListe
        fields = ('id', 'tigID')
