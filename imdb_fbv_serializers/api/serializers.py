from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    desc=serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.desc=validated_data.get("desc",instance.desc)
        
        instance.save()
        return instance
    
    def validate(self, data):
        name=data['name']
        desc=data['desc']
        
        if name==desc:
            print("same")
            raise serializers.ValidationError("both name and desc can not be same")
        return data