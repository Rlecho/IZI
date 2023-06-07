from django.db import models
from accounts.models import User
from apps.objects.models import *
# Create your models here.

class Commentaire(models.Model):
    user = models.ForeignKey(
        User, 
        related_name="comments",
        verbose_name="user",
        on_delete=models.CASCADE
    )
    
    text = models.TextField(verbose_name="Commentaire")
    
    objet = models.ForeignKey(
        Objet,
        on_delete=models.CASCADE,
        related_name="object",
        verbose_name = "Objet"
    )
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ="Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return str(self.user)
