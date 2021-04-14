from rest_framework import serializers
from exerciseapp.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    get_preview = serializers.CharField(read_only=True)
    class Meta:
        model = Exercise
        fields = "__all__"

