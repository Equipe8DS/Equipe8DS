from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext as _
from rest_framework.reverse import reverse
from rest_framework import permissions

class CategoriaItens:
    CATEGORIA = [
        (None, '<selecione>'),
        ('alimentos', 'Alimentos'),
        ('transporte', 'Transporte'),
        ('academico', 'Acadêmico'),
        ('agricultura', 'Agricultura'),
        ('casa', 'Casa'),
        ('equipamento', 'Equipamento'),
        ('luxo', 'Luxo')
    ]


class Item(models.Model):
    QUALIDADE = [
        (None, '<selecione>'),
        ('ruim', 'Ruim'),
        ('pobre', 'Pobre'),
        ('medio', 'Médio'),
        ('bom', 'Bom'),
        ('excelente', 'Excelente')
    ]
    CATEGORIA = CategoriaItens.CATEGORIA

    nome = models.CharField(max_length=100, blank=False, )
    preco_sugerido = models.FloatField(
        max_length=100, null=False, verbose_name='Preço Sugerido')
    qualidade = models.CharField(max_length=100, choices=QUALIDADE, null=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIA, null=False)
    descricao = models.CharField(
        max_length=100, blank=False, verbose_name='Descrição')
    ativo = models.BooleanField(editable=False, default=True)

    def isOuro(self):
        return self.nome == 'Ouro'

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("itens")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})


class EstiloVida(models.Model):
    nome = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = _("estilovida")
        verbose_name_plural = _("estilosdevida")

    def __str__(self):
        return self.nome


class GastosSemanais(models.Model):
    CATEGORIA = CategoriaItens.CATEGORIA

    estiloVida = models.ForeignKey(EstiloVida, on_delete=models.DO_NOTHING, null=False)
    tipo = models.CharField(max_length=30, null=False, choices=CATEGORIA)
    gastoPercentual = models.FloatField(null=False)

    class Meta:
        verbose_name = _("gastossemanais")
        verbose_name_plural = _("gastossemanais")


class Personagem(models.Model):
    RACAS = [
        (None, '<selecione>'),
        ('humano', 'Humano'),
        ('anão', 'Anão'),
        ('dahllan', 'Dahllan'),
        ('elfo', 'Elfo'),
        ('goblin', 'Goblin'),
        ('lefou', 'Lefou'),
        ('minotauro', 'Minotauro'),
        ('qareen', 'Qareen'),
        ('golem', 'Golem'),
        ('hynne', 'Hynne'),
        ('kliren', 'Kliren'),
        ('medusa', 'Medusa'),
        ('osteon', 'Osteon'),
        ('sereia/tritao', 'Sereia/Tritão'),
        ('silfide', 'Silfide'),
        ('aggelos', 'Aggelos'),
        ('sufulre', 'Sufulre'),
        ('trog', 'Trog')
    ]
    CLASSE = [
        (None, '<selecione>'),
        ('mago', 'Mago'),
        ('bruxo', 'Bruxo'),
        ('feiticeiro', 'Feiticeiro'),
        ('barbaro', 'Bárbaro'),
        ('bardo', 'Bardo'),
        ('cacador', 'Caçador'),
        ('cavaleiro', 'Cavaleiro'),
        ('clerigo', 'Clérigo'),
        ('druida', 'Druída'),
        ('guerreiro', 'Guerreiro'),
        ('inventor', 'Inventor'),
        ('ladino', 'Ladino'),
        ('lutador', 'Lutador'),
        ('nobre', 'Nobre'),
        ('paladino', 'Paladino')
    ]
    nome = models.CharField(max_length=100, blank=False, )
    raca = models.CharField(max_length=100, choices=RACAS,
                            null=False, verbose_name='Raça')
    classe = models.CharField(max_length=100, choices=CLASSE, null=False)
    tipo = models.CharField(max_length=100, editable=False, default='Jogador',
                            choices=[('jogador', 'Jogador'), ('npc', 'NPC')])
    ativo = models.BooleanField(editable=False, default=True)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    inventario = models.ManyToManyField(Item, through='ItemPersonagem')
    estiloVida = models.ForeignKey(EstiloVida, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = _("personagem")
        verbose_name_plural = _("personagens")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("personagem_detail", kwargs={"pk": self.pk})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.dono.is_staff):
            self.tipo = 'npc'
        super(Personagem, self).save()

    def add_item_inventario(self, item, quantidade):
        try:
            inventario = self.itempersonagem_set.get(item=item)
            inventario.quantidade += quantidade
            inventario.save()
        except ObjectDoesNotExist:
            self.itempersonagem_set.create(item_id=item, quantidade=quantidade)
            self.save()

        historico = Historico(personagem_id=self.id, item_id=item, quantidade=quantidade, tipo='inclusao')
        historico.save()
        return 'Item adicionado ao inventário'


    def remove_item_inventario(self, id_item, quantidade):
        inventario = self.itempersonagem_set.get(item=id_item)
        nova_quantidade = inventario.quantidade - quantidade

        if nova_quantidade < 0:
            raise Exception(f'Não é possível remover {quantidade} {inventario.item.nome}(s).')

        elif nova_quantidade == 0 and not inventario.item.isOuro():
            inventario.delete()

        else:
            inventario.quantidade = nova_quantidade
            inventario.save()

        historico = Historico(personagem_id=self.id, item_id=id_item, quantidade=quantidade, tipo='remocao')
        historico.save()
        return 'Item removido do inventário'

    def remove_ouro(self, quantidade):
        ouro = Item.objects.get(nome='Ouro')
        return self.remove_item_inventario(id_item=ouro.id, quantidade=quantidade)

    def getOuro(self):
        try:
            item = self.inventario.get(nome='Ouro')
            return ItemPersonagem.objects.get(item=item, personagem=self).quantidade
        except ObjectDoesNotExist as e:
            print(self.nome)
            print(e)
            return 0


class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    tesouro = models.FloatField(max_length=100, null=False)
    governante = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    ativo = models.BooleanField(editable=False, default=True)

    class Meta:
        verbose_name = _("cidade")
        verbose_name_plural = _("cidades")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("cidade", kwargs={"pk": self.pk})


class Jogador(AbstractUser):
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(editable=False, default=True)
    email = models.CharField(unique=True, max_length=100, null=True)
    username = models.CharField(unique=True, max_length=15)
    uid_telegram = models.CharField(unique=True, max_length=100, null=True)

    # perfil = models.CharField (editable = False, default = 'jogador')

    class Meta:
        verbose_name = _("jogador")
        verbose_name_plural = _("jogadores")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("jogador", kwargs={"pk": self.pk})


class ItemPersonagem(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)

    class Meta:
        verbose_name = _("inventario")
        verbose_name_plural = _("inventarios")
        constraints = [models.UniqueConstraint(
            fields=['personagem', 'item'], name='itempersonagem_constraint')]


class Loja(models.Model):
    nome = models.CharField(max_length=100, blank=False,
                            verbose_name='Nome da Loja')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    caixa = models.FloatField(max_length=100, null=False, verbose_name='Caixa')
    responsavel = models.ForeignKey(Personagem, on_delete=models.CASCADE,
                                    verbose_name='Responsável', limit_choices_to={'ativo': True}, )
    estok = models.ManyToManyField(Item, through='Estoque')
    ativo = models.BooleanField(editable=False, default=True)

    def remove_item(self, id_item, quantidade):
        estoque = self.estoque_set.get(item=id_item)
        nova_quantidade = estoque.quantidade_item - quantidade

        if nova_quantidade < 0:
            raise Exception(f'Não é possível remover {quantidade} itens, '
                            f'essa loja possui apenas {estoque.quantidade_item}.')

        elif nova_quantidade == 0 and not estoque.item.isOuro():
            estoque.delete()

        else:
            estoque.quantidade_item = nova_quantidade
            estoque.save()

        return 'Item removido do estoque.'

    def add_item(self, id_item, quantidade, preco=None):
        try:
            estoque = self.estoque_set.get(item_id=id_item)
            estoque.quantidade_item += quantidade
            estoque.save()
        except ObjectDoesNotExist:
            item = Item.objects.get(id=id_item)
            preco = preco if not None else item.preco_sugerido
            self.estoque_set.create(item_id=item, quantidade_item=quantidade, preco_item=preco)

        self.save()
        return 'Item adicionado ao estoque.'

    def add_ouro(self, quantidade):
        ouro = Item.objects.get(nome='Ouro')
        self.add_item(id_item=ouro.id, quantidade=quantidade)

    class Meta:
        verbose_name = _("loja")
        verbose_name_plural = _("lojas")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("loja", kwargs={"pk": self.pk})


class Estoque(models.Model):
    quantidade_item = models.IntegerField(
        null=False, verbose_name='Quantidade de Itens')
    preco_item = models.FloatField(null=False, verbose_name='Preço do Item')
    loja = models.ForeignKey(
        Loja, on_delete=models.CASCADE, limit_choices_to={'ativo': True}, )
    item = models.ForeignKey(
        Item, on_delete=models.DO_NOTHING, limit_choices_to={'ativo': True}, )

    class Meta:
        verbose_name = _("estoque")
        verbose_name_plural = _("estoques")
        constraints = [models.UniqueConstraint(
            fields=['loja', 'item'], name='unique constraints')]


class Historico(models.Model):
    TIPO = [
        (None, '<selecione>'),
        ('retirada', 'Retirada'),
        ('inclusao', 'Inclusão'),
        ('compra', 'Compra'),
    ]

    loja = models.ForeignKey(Loja, on_delete=models.DO_NOTHING, null=True)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=False)
    personagem = models.ForeignKey(
        Personagem, on_delete=models.DO_NOTHING, null=False)
    quantidade = models.IntegerField(null=False)
    tipo = models.CharField(max_length=10, null=False, choices=TIPO)
    preco = models.FloatField(null=True)
    data = models.DateTimeField(default=datetime.now(), null=False)
    descricao = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("historico")
        verbose_name_plural = _("historicos")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        data = datetime.now()
        data = data.strftime("%d/%m/%y às %H:%M:%S")
        if hasattr(self, 'loja') and self.loja is not None:
            self.descricao = f'{self.personagem} fez {self.tipo} de {self.quantidade} {self.item} em {data}' \
                             f' na {self.loja} por {self.preco}.'
        else:
            self.descricao = f'{self.personagem} fez {self.tipo} de {self.quantidade} {self.item} em {data}.'

        super(Historico, self).save()

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("historico", kwargs={"pk": self.pk})