from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.backends import BaseBackend
import jwt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from accounts.models import User, Token
from django.db.models import Q
from twilio.rest import Client
from rest_framework import status
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.tokens import default_token_generatorc
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from .models import Token
import random




from django.contrib.auth.models import BaseUserManager



# Create your views here.
def inscription(request):
    return render(request, 'account/inscription.html')

def connexion(request):
    return render(request, 'account/connexion.html')

def change_password(request):
    return render(request, 'account/change_password.html')

def reset_password(request):
    return render(request, 'account/reset_password.html')

# @api_view(['POST'])

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Le nom d'utilisateur est requis.")
        if not email:
            raise ValueError("L'adresse e-mail est requise.")

        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class RegisterView(APIView):
    def post(self, request):
        # Obtenir les données de la requête POST
       if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        # address = request.POST.get('address')
        # country_code = request.POST.get('country_code')
        phone_number = request.POST.get('tel')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    

        # Effectuez ici les validations nécessaires
        errors = {}

        # Vérification du mot de passe
        if password != confirm_password:
            errors['confirm_password'] = "Les mots de passe ne correspondent pas."

        # Autres validations...

        # S'il y a des erreurs, renvoyer une réponse avec les erreurs
        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        # Si les validations sont réussies, créez l'utilisateur
        # et effectuez les opérations supplémentaires si nécessaire

        # Exemple de création d'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)
        # user.address = address
        # user.country_code = country_code
        user.tel = phone_number
        user.save()
        # Autres opérations...
        # Génération du token
        # token, created = Token.objects.get_or_create(user=user)
        # token = Token.objects.create(user=user)
        # generated_key = random.randint(1000, 9999)
        # token = Token.objects.create(user=user, key=str(generated_key))
        token_payload = {'user_id': user.id}
        token = jwt.encode(token_payload, 'your-secret-key', algorithm='HS256')

        #return redirect('/account/connexion.html')
        return Response({'message': "L'utilisateur a été enregistré avec succès.", 'token': token}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_data = []
        for user in users:
            user_data.append({
                'username': user.username,
                'email': user.email,
                'phone_number': user.tel,
                'password': user.password,
                # 'address': user.address,
                # 'country_code': user.country_code,
                
            })
        return Response(user_data, status=status.HTTP_200_OK)

UserModel = get_user_model()

class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': "Connexion réussie."}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "Identifiant ou mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Effectuez les validations nécessaires pour l'e-mail
        
        # Envoyer l'e-mail de réinitialisation du mot de passe
        send_mail(
            subject='Password Reset',
            message='Please follow the instructions in the email to reset your password.',
            from_email='elechoserge@gmail.com',  # Adresse e-mail de l'expéditeur
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({'message': "Un e-mail de réinitialisation du mot de passe a été envoyé."},
                        status=status.HTTP_200_OK)

@api_view(['POST'])
def password_change_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Vérifiez que l'ancien mot de passe est correct
        user = User.objects.get(username=request.user.username)
        if not check_password(old_password, user.password):
            return Response({'errors': {'old_password': "Ancien mot de passe incorrect."}},
                            status=status.HTTP_400_BAD_REQUEST)

        # Effectuez les validations nécessaires pour les nouveaux mots de passe
        errors = {}

        if new_password1 != new_password2:
            errors['new_password2'] = "Les nouveaux mots de passe ne correspondent pas."

        # Autres validations...

        # S'il y a des erreurs, renvoyer une réponse avec les erreurs
        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        # Si les validations sont réussies, mettez à jour le mot de passe de l'utilisateur
        user.set_password(new_password1)
        user.save()

        # Assurez-vous que l'utilisateur reste connecté après le changement de mot de passe
        update_session_auth_hash(request, user)

        return Response({'message': "Le mot de passe a été modifié avec succès."},
                        status=status.HTTP_200_OK)


# account_sid = "AC499b5baed918d00fe32ddf9f3f27ac15"
# auth_token = "3bece352df58f743185b6728cdeb6fb2"
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+16205318707',
#          to='+22998964647'
#      )

# print(message.sid)






# def register(request):
#      if request.method == 'POST':
#          form = RegisterForm(request.POST)
#          if form.is_valid():
#              user = form.save()
#              phone_number = form.cleaned_data.get('phone_number')
#              user.profile.phone_number = phone_number
#              user.save()
#              username = form.cleaned_data.get('username')
#              raw_password = form.cleaned_data.get('password1')
#              user = authenticate(username=username, password=raw_password)
#              login(request, user)
#              return redirect('home')
#      else:
#          form = RegisterForm()
#      return render(request, 'account/inscription.html', {'form': form})

