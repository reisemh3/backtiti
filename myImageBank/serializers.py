from rest_framework.serializers import ModelSerializer
from myImageBank.models import ImageRandom


class ImageRandomSerializer(ModelSerializer):
    class Meta:
        model = ImageRandom
        fields = ('id', 'tigID')
