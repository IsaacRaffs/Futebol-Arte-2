# Generated by Django 5.0 on 2024-03-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_time_jogador_time_time_estado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competição',
            options={'verbose_name_plural': 'Competições'},
        ),
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='titulos',
            options={'verbose_name_plural': 'Titulos'},
        ),
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
