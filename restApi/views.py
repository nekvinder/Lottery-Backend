from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import lobby, lottery, user
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class LobbyViewSet(viewsets.ModelViewSet):
    # queryset = lobby.objects.all().order_by("ifsc")
    queryset = lobby.objects.all()
    serializer_class = LobbySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['^branch']


class LotteryViewSet(viewsets.ModelViewSet):
    # queryset = lottery.objects.all().order_by("ifsc")
    queryset = lottery.objects.all().order_by("-created_at")
    serializer_class = LotterySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_fields = ["lobby"]
    # filterset_fields = ["city"]
    # search_fields = ['^ifsc', '^branch', '^address',
    #                  '^city', '^district', '^state', ]
