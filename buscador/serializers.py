
from  rest_framework import serializers
from buscador.models import Institucion


class InstitutoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Institucion
        fields = '__all__'
