from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Id")
    title=serializers.CharField(label="Enter Patientname")
    author=serializers.CharField(label="Enter Test")
    phonenumber=serializers.CharField(label="Enter phonenumber")
    address=serializers.CharField(label="Enter address")
    status=serializers.CharField(label="Enter status")

