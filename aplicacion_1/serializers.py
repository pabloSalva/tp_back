from rest_framework import serializers

from aplicacion_1.models import Evento, Persona, PersonaEP


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido', 'sexo', 'telefono']


class PersonaEPSerializer(serializers.ModelSerializer):
    # tiene_referente = PersonaSerializer()

    class Meta:
        model = PersonaEP
        fields = [
            'id',
            'nombre',
            'apellido',
            'sexo',
            'telefono',
            'escolaridad_completa',
            'fecha_nacimiento',
            'maxima_escolaridad_alcanzada',
            'tiene_acompaniante',
            'tiene_cuidador',
            'vive_solo',
            'referente',

        ]


class EventoSerializer(serializers.ModelSerializer):
    persona_ep = PersonaEPSerializer()

    class Meta:
        model = Evento
        fields = ['id', 'fecha', 'motivo', 'persona_ep']
