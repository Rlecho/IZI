from django.db import models
from accounts.models import User
from apps.mycountry.models import *
# Create your models here.

class CategoryObjet(models.Model):
    
    #Objets volés, perdus, retrouvés
    #Ajouter les types d'objets 
    
    name = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", null = True, blank=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class GammeObjet(models.Model):

    #Gammes d'objet
    #On distigue:
    # - l'électronique,
    # - Article d'enfant,
    # - Bijoux, ...

    name = models.CharField(max_length=200, verbose_name="Gamme")
    description = models.TextField(verbose_name="Description", null = True, blank = True)

    class Meta:
        verbose_name = "GammeObjet"
        verbose_name_plural = "GammeObjets"

    def __str__(self):
        return self.name

class TypeObjet(models.Model):

    #Pour une gamme, on distigue plusieurs type d'objet:
    # Ex: Electronique
    # - Téléphone portable, 
    # - IPhone
    # - Mac
    # - Ordinateur Portatif
    # - Tablette
    # - Ordinateur bureautique, 
    # - Clé ....

    gamme = models.ForeignKey(
        GammeObjet,
        on_delete = models.CASCADE,
        verbose_name = 'Gamme d\'objet',
    )
    name = models.CharField(max_length=200, verbose_name="Genre d'objets")
    description = models.TextField(verbose_name="Description", null = True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class AttributObjet(models.Model):

    #Lorqu'on prend un type d'objet, plusieurs attribut lui sont relié
    #Ex: Pour un téléphone on a:
    # - La marque
    # - Le model
    # - Le code IMEI
    # - La couleur, etc

    type = models.ForeignKey(
        TypeObjet,
        on_delete = models.CASCADE,
        verbose_name = 'Type'
    )

    name = models.CharField(max_length=100, verbose_name="Nom")
    code = models.CharField(max_length=100, verbose_name="Code de l'attribut")
    class Meta:
        verbose_name = "Attribut"
        verbose_name_plural = "Attributs"

    def __str__(self):
        return self.name


class Statut(models.Model):
    
    #Statut de l'objet
    #Recherche; Vérification, Rendu, Achivé
    
    code = models.CharField(max_length=20, verbose_name="Code")
    name = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", null = True)

    class Meta:
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"

    def __str__(self):
        return self.name

class TitreObjet(models.Model):

    type = models.ForeignKey(
        TypeObjet, 
        on_delete = models.CASCADE,
        verbose_name = 'Type associé',
        )
    name = models.CharField(max_length=200, verbose_name="Désigantion")
    description = models.TextField(verbose_name="Description", null = True, blank = True)


    class Meta:
        verbose_name = "TitreObjet"
        verbose_name_plural = "TitreObjets"

    def __str__(self):
        return self.name


class Objet(models.Model):
    
    # Tous les objets (retrouvés, perdus, volés)
    
    creator = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        verbose_name="Créateur de l'objet",
        related_name = 'createur',
        null = True,
        blank = True
        )
    
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name ='auteur',
        verbose_name="Propio de l'objet",
    )
    
    title = models.ForeignKey(
        TitreObjet,
        on_delete=models.CASCADE,
        verbose_name= "Désignation de l'objet",
    )
    
    reference = models.CharField(max_length=50, verbose_name= "Reference Objet")
    
    category = models.ForeignKey(
        CategoryObjet, 
        on_delete = models.CASCADE, 
        related_name = 'categorie',
        verbose_name = "Categorie d'objet"
        )

    gamme = models.ForeignKey(
        GammeObjet,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'gamme'
    )

    type = models.ForeignKey(
        TypeObjet,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        verbose_name = 'Type'
    )

    statut = models.ForeignKey(
        Statut,
        on_delete = models.CASCADE,
        verbose_name = "Statut"
    )
    
    description = models.TextField(verbose_name="Description")
    
    last_address = models.ForeignKey(
        Adresse, 
        verbose_name="Dernière Adresse",
        on_delete=models.CASCADE
        )
    
    date = models.DateTimeField(auto_now_add=True)

    date_action = models.DateField(verbose_name='Date perte/retrouvé')
    
    # Pour gérer les suppressions. On ne supprime jamais les données d'une BD
    
    is_public = models.BooleanField(default=True)

    # Mes ajouts à moi ***************************************************************************************************

    worth = models.IntegerField(verbose_name="La valeur en FCFA",default=10, blank=True)

    is_person = models.BooleanField(default=True)

    name = models.CharField(max_length=200, verbose_name="Tous les noms", blank=True)

    langue = models.CharField(max_length=200, verbose_name="Toutes les langues", blank=True)

    teint = models.CharField(max_length=20, verbose_name="Le teint", blank=True)

    sexe = models.CharField(max_length=20, verbose_name="Le sexe", blank=True)

    age = models.IntegerField(verbose_name="L'âge", default=1, blank=True)

    taille = models.IntegerField(verbose_name="La taille", default=2, blank=True)

    adresse = models.CharField(max_length=100, verbose_name="Lieu de perte/disparition", blank=True)

    description_person = models.TextField(verbose_name="Autres précisions nécessaires", null = True, blank=True)

    #proprio de l'objet


    # **********************************************************************************************************************

    class Meta:
        verbose_name = "Objet"
        verbose_name_plural = "Objets"

    def __str__(self):
        return self.title

class DetailAttributObjet(models.Model):

    objet = models.ForeignKey(
        Objet,
        verbose_name = 'Objet',
        on_delete = models.CASCADE
    )
    
    attribut = models.ForeignKey(
        AttributObjet,
        verbose_name = 'Attribut',
        on_delete = models.CASCADE,
    )

    valeur = models.CharField(max_length=254, verbose_name="Valeur de l'attribut")

    class Meta:
        verbose_name = "DetailObjet"
        verbose_name_plural = "DetailObjets"

    def __str__(self):
        return str(str(self.objet) + ' ' + str(self.attibut))


class ModifierObjet(models.Model):

    objet = models.ForeignKey(
        Objet,
        verbose_name='Objet',
        on_delete = models.CASCADE
        )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name = "Administrateur"
    )

    change = models.TextField(verbose_name = 'Changement effetué')

    confirm = models.BooleanField(default = False, verbose_name='Modification Confirmer')

    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "ModifierObjet"
        verbose_name_plural = "ModeifierObjets"

    def __str__(self):
        return str(self.objet)


class ImageObjet(models.Model):
    
    object = models.ForeignKey(
        Objet,
        on_delete = models.CASCADE,
        verbose_name = "Objet",
        )
    name = models.CharField(max_length=100, verbose_name = "Titre de l'image")
    image = models.ImageField(upload_to = "objet/")
    caption = models.TextField(verbose_name = "Caption", null = True, blank = True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name