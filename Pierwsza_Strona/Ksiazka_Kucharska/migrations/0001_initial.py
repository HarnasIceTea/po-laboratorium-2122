# Generated by Django 4.0.3 on 2022-05-12 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Typ_nadwozia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Samochod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('opis', models.CharField(max_length=600, null=True)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ksiazka_Kucharska.model')),
                ('typ', models.ManyToManyField(to='Ksiazka_Kucharska.typ_nadwozia')),
            ],
        ),
    ]
