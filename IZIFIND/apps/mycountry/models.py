from django.db import models

# Create your models here.

class Departement(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Nom')
    description = models.TextField(null=True, verbose_name='Description')

    class Meta:
        verbose_name = "Departement"
        verbose_name_plural = "Departements"

    def __str__(self):
        return self.name
    
    
class Arrondissement(models.Model):
    
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, verbose_name = "Département")
    name = models.CharField(max_length=200, verbose_name='Nom')
    description = models.TextField(null=True, verbose_name='Description')

    class Meta:
        verbose_name = "Arrondissement"
        verbose_name_plural = "Arrondissements"

    def __str__(self):
        return self.name


class Ville(models.Model):
    
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE, verbose_name = "Arrondissement")
    name = models.CharField(max_length=200, verbose_name='Nom')
    description = models.TextField(null=True, verbose_name='Description')

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Villes"

    def __str__(self):
        return self.name

class Quartier(models.Model):

    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, verbose_name = "Ville")
    name = models.CharField(max_length=200, verbose_name='Nom')
    description = models.TextField(null=True, verbose_name='Description')

    class Meta:
        verbose_name = "Quartier"
        verbose_name_plural = "Quartiers"

    def __str__(self):
        return self.name



class Adresse(models.Model):
    
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, verbose_name="Département")
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE, verbose_name="Arrondissement")
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, verbose_name="Ville")
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE, verbose_name="Quartier")

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def __str__(self):
        return "Adresse-" + self