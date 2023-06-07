from django import forms

from IZIFIND.accounts.models import User
from IZIFIND.apps.mycountry.models import Adresse
from .models import CategoryObjet, GammeObjet, Statut, TitreObjet, TypeObjet

class DeclarationForm(forms.Form):
    reference = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50, verbose_name = 'Description')
    date = forms.DateTimeField(auto_now_add=True)
    date_action = forms.DateTimeField(auto_now_add=True, verbose_name = 'Date perte/retrouvé')
    is_public = forms.BooleanField(default=True)
    is_person = forms.BooleanField(default=True)
    worth = forms.IntegerField(verbose_name="La valeur en FCFA", blank=True)
    name = forms.CharField(max_length=200, verbose_name="Tous les noms", blank=True)
    langue = forms.CharField(max_length=200, verbose_name="Toutes les langues", blank=True)
    teint = forms.CharField(max_length=20, verbose_name="Le teint", blank=True)
    

    gamme = forms.ModelChoiceField(queryset=GammeObjet.objects.all())
    
    type = forms.ModelChoiceField(queryset=TypeObjet.objects.none())
        
    creator = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Créateur de l'objet",
        empty_label=None,
        required=False,
    )
    
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Créateur de l'objet",
        empty_label=None,
        required=False,
    )
    
    category = forms.ModelChoiceField(
    queryset=CategoryObjet.objects.all(),
    label="Créateur de l'objet",
    empty_label=None,
    required=False,
     )

    title = forms.ModelChoiceField(
        queryset=TitreObjet.objects.all(),
        label="Désignation de l'objet",
        empty_label=None  # Pour empêcher la sélection d'une option vide
    )
    
    last_address = forms.ModelChoiceField(
        queryset=Adresse.objects.all(),
        label="Désignation de l'objet",
        empty_label=None  # Pour empêcher la sélection d'une option vide
    )
    
    Statut = forms.ModelChoiceField(
        queryset=Statut.objects.all(),
        label="Désignation de l'objet",
        empty_label=None  # Pour empêcher la sélection d'une option vide
    )