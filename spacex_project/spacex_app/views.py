from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import MenuItem, StatsItem
from .serializers import MenuItemSerializer, StatsItemSerializer

# Create your views here.


@api_view(['GET'])
def get_menu_content(request: Request) -> Response:
    menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_stats_content(request: Request) -> Response:
    stats_items = StatsItem.objects.all()
    serializer = StatsItemSerializer(stats_items, many=True)
    return Response(serializer.data)
