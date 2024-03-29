# Generated by Django 3.2.13 on 2022-07-03 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mycountry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('code', models.CharField(max_length=100, verbose_name="Code de l'attribut")),
            ],
            options={
                'verbose_name': 'Attribut',
                'verbose_name_plural': 'Attributs',
            },
        ),
        migrations.CreateModel(
            name='CategoryObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='GammeObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Gamme')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'GammeObjet',
                'verbose_name_plural': 'GammeObjets',
            },
        ),
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Statut',
                'verbose_name_plural': 'Statuts',
            },
        ),
        migrations.CreateModel(
            name='TypeObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Genre d'objets")),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('gamme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.gammeobjet', verbose_name="Gamme d'objet")),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='TitreObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Désigantion')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.typeobjet', verbose_name='Type associé')),
            ],
            options={
                'verbose_name': 'TitreObjet',
                'verbose_name_plural': 'TitreObjets',
            },
        ),
        migrations.CreateModel(
            name='Objet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, verbose_name='Reference Objet')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_action', models.DateField(verbose_name='Date perte/retrouvé')),
                ('is_public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to=settings.AUTH_USER_MODEL, verbose_name="Propio de l'objet")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='objects.categoryobjet', verbose_name="Categorie d'objet")),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createur', to=settings.AUTH_USER_MODEL, verbose_name="Créateur de l'objet")),
                ('gamme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gamme', to='objects.gammeobjet')),
                ('last_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycountry.adresse', verbose_name='Dernière Adresse')),
                ('statut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.statut', verbose_name='Statut')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.titreobjet', verbose_name="Désignation de l'objet")),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='objects.typeobjet', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Objet',
                'verbose_name_plural': 'Objets',
            },
        ),
        migrations.CreateModel(
            name='ModifierObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.TextField(verbose_name='Changement effetué')),
                ('confirm', models.BooleanField(default=False, verbose_name='Modification Confirmer')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('objet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.objet', verbose_name='Objet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Administrateur')),
            ],
            options={
                'verbose_name': 'ModifierObjet',
                'verbose_name_plural': 'ModeifierObjets',
            },
        ),
        migrations.CreateModel(
            name='ImageObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Titre de l'image")),
                ('image', models.ImageField(upload_to='objet/')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.objet', verbose_name='Objet')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='DetailAttributObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(max_length=254, verbose_name="Valeur de l'attribut")),
                ('attribut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.attributobjet', verbose_name='Attribut')),
                ('objet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.objet', verbose_name='Objet')),
            ],
            options={
                'verbose_name': 'DetailObjet',
                'verbose_name_plural': 'DetailObjets',
            },
        ),
        migrations.AddField(
            model_name='attributobjet',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.typeobjet', verbose_name='Type'),
        ),
    ]
