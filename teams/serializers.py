from rest_framework import serializers
from teams import models

class TeamSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('id', 'name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'
