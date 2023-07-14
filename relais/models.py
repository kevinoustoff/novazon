import uuid
from django.db import models
import random
import string

class PointRelais(models.Model):
   # key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
   # key = models.CharField(max_length=10, default=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), unique=True)

   
    key = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relay_name = models.CharField(max_length=100)
    quartier = models.CharField(max_length=300)
    numero_telephone= models.CharField(max_length=8)
    latitude = models.DecimalField(max_digits=100, decimal_places=20)
    longitude = models.DecimalField(max_digits=100, decimal_places=20)
    gmanager_signature = models.BooleanField(default=False)

    def generate_key(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(10))

    def save(self, *args, **kwargs):
        if not self.key:  # Génère une nouvelle clé uniquement si elle n'est pas définie
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.relay_name} {self.numero_telephone} {self.quartier}"
