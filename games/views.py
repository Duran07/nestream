from django.shortcuts import render
from django.http import JsonResponse
from .models import Game, Studio
from .serializers import GameSerializer, StudioSerializer



def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializer(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def studio_list(request):
    studios = Studio.objects.all()
    serializer = StudioSerializer(studios, many=True)
    return JsonResponse(data, safe=False)