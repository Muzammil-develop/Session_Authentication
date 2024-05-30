from rest_framework import serializers
from home.models import Workshop

class WorkshopSerializer (serializers.ModelSerializer):
    class Meta :
        model = Workshop
        fields = '__all__'