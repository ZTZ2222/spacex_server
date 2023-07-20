from rest_framework import serializers

from .models import MenuItem, StatsItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class StatsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsItem
        fields = '__all__'
