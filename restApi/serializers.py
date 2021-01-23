from .models import lobby, lottery, user
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username', 'url', 'id', 'balance', ]


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = lobby
        fields = ['url', 'id', 'name', 'capacity',
                  'entryFee', 'created_at', 'finished', ]


class LotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = lottery
        fields = ['url', 'id', 'lobby',
                  'houseChargeAmount', 'participants', 'winner', 'created_at', ]
