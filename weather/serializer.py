from rest_framework import fields, serializers

# Simple serializer with the required fields.
class ResultsSerializer(serializers.Serializer):
    maximum = serializers.FloatField()
    minimum = serializers.FloatField()
    average = serializers.FloatField()
    median = serializers.FloatField()