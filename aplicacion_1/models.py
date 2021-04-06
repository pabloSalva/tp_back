from django.db import models


class Persona(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro")
    ]

    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, default="M")
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


class PersonaEP(Persona):
    TIPO_ESCOLARIDAD = [
        ('SIN_ESCOLARIDAD', 'Sin Escolaridad'),
        ('PRIMARIO', 'Primario'),
        ('SECUNDARIO', 'Secundario'),
        ('TERCIARIO', 'Terciario'),
        ('UNIVERSITARIO', 'Universitario'),
    ]

    escolaridad_completa = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField(null=False)
    maxima_escolaridad_alcanzada = models.CharField(max_length=16,
                                                    choices=TIPO_ESCOLARIDAD, default='SIN_ESCOLARIDAD')
    tiene_acompaniante = models.BooleanField(default=False)
    tiene_cuidador = models.BooleanField(default=False)
    vive_solo = models.BooleanField(default=False)

    referente = models.ForeignKey(
        Persona, related_name='tiene_referente', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return super().nombre


class Evento(models.Model):
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)

    persona_ep = models.ForeignKey(
        PersonaEP, on_delete=models.PROTECT, null=True, blank=True)
