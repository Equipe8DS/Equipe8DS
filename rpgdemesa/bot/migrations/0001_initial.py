# Generated by Django 3.2.6 on 2021-10-20 23:39

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('uid_telegram', models.CharField(max_length=100, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'jogador',
                'verbose_name_plural': 'jogadores',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tesouro', models.FloatField(max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name': 'cidade',
                'verbose_name_plural': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='EstiloVida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'estilovida',
                'verbose_name_plural': 'estilosdevida',
            },
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_item', models.IntegerField(verbose_name='Quantidade de Itens')),
                ('preco_item', models.FloatField(verbose_name='Preço do Item')),
            ],
            options={
                'verbose_name': 'estoque',
                'verbose_name_plural': 'estoques',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco_sugerido', models.FloatField(max_length=100, verbose_name='Preço Sugerido')),
                ('qualidade', models.CharField(choices=[(None, '<selecione>'), ('ruim', 'Ruim'), ('pobre', 'Pobre'), ('medio', 'Médio'), ('bom', 'Bom'), ('excelente', 'Excelente')], max_length=100)),
                ('categoria', models.CharField(choices=[(None, '<selecione>'), ('alimentos', 'Alimentos'), ('transporte', 'Transporte'), ('academico', 'Acadêmico'), ('agricultura', 'Agricultura'), ('casa', 'Casa'), ('equipamento', 'Equipamento'), ('luxo', 'Luxo')], max_length=100)),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.CreateModel(
            name='ItemPersonagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.item')),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
            },
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(choices=[(None, '<selecione>'), ('humano', 'Humano'), ('anão', 'Anão'), ('dahllan', 'Dahllan'), ('elfo', 'Elfo'), ('goblin', 'Goblin'), ('lefou', 'Lefou'), ('minotauro', 'Minotauro'), ('qareen', 'Qareen'), ('golem', 'Golem'), ('hynne', 'Hynne'), ('kliren', 'Kliren'), ('medusa', 'Medusa'), ('osteon', 'Osteon'), ('sereia/tritao', 'Sereia/Tritão'), ('silfide', 'Silfide'), ('aggelos', 'Aggelos'), ('sufulre', 'Sufulre'), ('trog', 'Trog')], max_length=100, verbose_name='Raça')),
                ('classe', models.CharField(choices=[(None, '<selecione>'), ('mago', 'Mago'), ('bruxo', 'Bruxo'), ('feiticeiro', 'Feiticeiro'), ('barbaro', 'Bárbaro'), ('bardo', 'Bardo'), ('cacador', 'Caçador'), ('cavaleiro', 'Cavaleiro'), ('clerigo', 'Clérigo'), ('druida', 'Druída'), ('guerreiro', 'Guerreiro'), ('inventor', 'Inventor'), ('ladino', 'Ladino'), ('lutador', 'Lutador'), ('nobre', 'Nobre'), ('paladino', 'Paladino')], max_length=100)),
                ('tipo', models.CharField(choices=[('jogador', 'Jogador'), ('npc', 'NPC')], default='Jogador', editable=False, max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estiloVida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.estilovida')),
                ('inventario', models.ManyToManyField(through='bot.ItemPersonagem', to='bot.Item')),
            ],
            options={
                'verbose_name': 'personagem',
                'verbose_name_plural': 'personagens',
            },
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Loja')),
                ('caixa', models.FloatField(max_length=100, verbose_name='Caixa')),
                ('ativo', models.BooleanField(default=True, editable=False)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.cidade')),
                ('estok', models.ManyToManyField(through='bot.Estoque', to='bot.Item')),
                ('responsavel', models.ForeignKey(limit_choices_to={'ativo': True}, on_delete=django.db.models.deletion.CASCADE, to='bot.personagem', verbose_name='Responsável')),
            ],
            options={
                'verbose_name': 'loja',
                'verbose_name_plural': 'lojas',
            },
        ),
        migrations.AddField(
            model_name='itempersonagem',
            name='personagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.personagem'),
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(choices=[(None, '<selecione>'), ('retirada', 'Retirada'), ('inclusao', 'Inclusão'), ('compra', 'Compra')], max_length=10)),
                ('preco', models.FloatField(null=True)),
                ('data', models.DateTimeField(default=datetime.datetime(2021, 10, 20, 20, 39, 31, 357117))),
                ('descricao', models.CharField(max_length=500)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bot.item')),
                ('loja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.loja')),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bot.personagem')),
            ],
            options={
                'verbose_name': 'historico',
                'verbose_name_plural': 'historicos',
            },
        ),
        migrations.CreateModel(
            name='GastosSemanais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[(None, '<selecione>'), ('alimentos', 'Alimentos'), ('transporte', 'Transporte'), ('academico', 'Acadêmico'), ('agricultura', 'Agricultura'), ('casa', 'Casa'), ('equipamento', 'Equipamento'), ('luxo', 'Luxo')], max_length=30)),
                ('gastoPercentual', models.FloatField()),
                ('estiloVida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bot.estilovida')),
            ],
            options={
                'verbose_name': 'gastossemanais',
                'verbose_name_plural': 'gastossemanais',
            },
        ),
        migrations.AddField(
            model_name='estoque',
            name='item',
            field=models.ForeignKey(limit_choices_to={'ativo': True}, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.item'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='loja',
            field=models.ForeignKey(limit_choices_to={'ativo': True}, on_delete=django.db.models.deletion.CASCADE, to='bot.loja'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='governante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.personagem'),
        ),
        migrations.AddConstraint(
            model_name='itempersonagem',
            constraint=models.UniqueConstraint(fields=('personagem', 'item'), name='itempersonagem_constraint'),
        ),
        migrations.AddConstraint(
            model_name='estoque',
            constraint=models.UniqueConstraint(fields=('loja', 'item'), name='unique constraints'),
        ),
    ]
