# Generated by Django 3.2.6 on 2021-09-12 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20210911_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='responsavel',
            field=models.ForeignKey(limit_choices_to={'ativo': True}, on_delete=django.db.models.deletion.CASCADE, to='bot.personagem', verbose_name='Responsável'),
        ),
    ]