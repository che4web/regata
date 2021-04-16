from rest_framework import serializers
from competitionsapp.models import Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields= ['team']

    def create(self,validate_data):
        instance =  super().create(validate_data)
        instance.team = self.context['request'].user.team
        instance.save()
        return instance


