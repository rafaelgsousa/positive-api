from rest_framework import serializers

from ..models import WheelUserAnalysis


class WheelUserAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = WheelUserAnalysis
        fields = '__all__'