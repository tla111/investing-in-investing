from rest_framework import serializers
from realestate.models import KitchenRoom


class KitchenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KitchenRoom
        fields = [
            'id', 'counter_top', 'room_shape', 'refrigerator_style'
        ]
