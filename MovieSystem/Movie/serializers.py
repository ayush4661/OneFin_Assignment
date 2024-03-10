from rest_framework import serializers
from .models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
        
    #     # Remove 'user' and 'uuid' fields from the response
    #     data.pop('user', None)
    #     data.pop('uuid', None)

    #     return data
