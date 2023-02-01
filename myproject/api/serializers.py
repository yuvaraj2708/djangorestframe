from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Id")
    title=serializers.CharField(label="Enter Title")
    author=serializers.CharField(label="Enter Names")