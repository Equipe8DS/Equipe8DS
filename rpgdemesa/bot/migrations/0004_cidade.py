# Generated by Django 3.2.6 on 2021-09-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20210901_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tesouro', models.FloatField(max_length=100)),
                ('nome_cidade', models.CharField(max_length=100)),
            ],
        ),
    ]
