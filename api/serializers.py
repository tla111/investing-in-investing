from rest_framework import serializers
from realestate.models import KitchenRoom, LivingRoom


class KitchenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KitchenRoom
        fields = [
            'id', 'counter_top', 'room_shape', 'refrigerator_style'
        ]


class LivingRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LivingRoom
        fields = [
            'id', 'sofas', 'televisions', 'chairs'
        ]
