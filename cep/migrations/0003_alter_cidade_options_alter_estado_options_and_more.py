# Generated by Django 5.0 on 2024-03-04 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0002_alter_cidade_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises'},
        ),
    ]
