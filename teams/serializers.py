from rest_framework import serializers
from teams import models

class ContestantSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contestant
        fields = ('id', 'name')


class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contestant
        fields = '__all__'
