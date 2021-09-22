from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


class Personagem (models.Model): 
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
        ('sereia/tritão', 'Sereia/Tritão'),
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
        ('bárbaro', 'Bárbaro'),
        ('bardo', 'Bardo'),
        ('caçador', 'Caçador'),
        ('cavaleiro', 'Cavaleiro'),
        ('clérigo', 'Clérigo'),
        ('druída', 'Druída'),
        ('guerreiro', 'Guerreiro'),
        ('inventor', 'Inventor'),
        ('ladino', 'Ladino'),
        ('lutador', 'Lutador'),
        ('nobre', 'Nobre'),
        ('paladino', 'Paladino')
    ]
    nome = models.CharField (max_length=100, blank=False, ) 
    raca = models.CharField (max_length=100, choices = RACAS, null=False, verbose_name='Raça')
    classe = models.CharField (max_length=100, choices = CLASSE, null=False)
    tipo = models.CharField (max_length=100, editable=False, default='Jogador', choices=[('jogador', 'Jogador'), ('npc', 'NPC')])
    ativo = models.BooleanField (editable=False, default=True)
    dono = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        verbose_name = _("personagem")
        verbose_name_plural = _("personagens")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("personagem_detail", kwargs={"pk": self.pk})
        
    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        if (self.dono.is_staff) : 
            self.tipo = 'npc'
        super(Personagem, self).save()
        
class Cidade(models.Model):
    nome_cidade =  models.CharField (max_length=100, blank=False, verbose_name='Cidade')
    tesouro = models.FloatField (max_length=100, null=False)
    governante =  models.ForeignKey(Personagem, on_delete=models.CASCADE, limit_choices_to={'ativo': True})
    ativo = models.BooleanField(editable=False, default=True)       

    class Meta:
        verbose_name = _("cidade")
        verbose_name_plural = _("cidades")

    def __str__(self):
        return self.nome_cidade

    def get_absolute_url(self):
        return reverse("cidade_detail", kwargs={"pk": self.pk})

class Item (models.Model):
    QUALIDADE = [
        (None, '<selecione>'),
        ('ruim', 'Ruim'),
        ('pobre', 'Pobre'),
        ('medio', 'Médio'),
        ('bom', 'Bom'),
        ('excelente', 'Excelente')
    ]
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
    nome = models.CharField (max_length=100, blank=False, )
    preco_sugerido = models.FloatField (max_length=100, null=False, verbose_name='Preço Sugerido')
    qualidade = models.CharField (max_length=100, choices = QUALIDADE, null=False)
    categoria = models.CharField (max_length=100, choices = CATEGORIA, null=False)
    descricao = models.CharField (max_length=100, blank=False, verbose_name='Descrição')
    ativo = models.BooleanField(editable=False, default=True)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("itens")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

class Loja(models.Model):
    nome = models.CharField (max_length=100, blank=False, verbose_name = 'Nome da Loja')
    cidade = models.ForeignKey (Cidade, on_delete=models.CASCADE)
    responsavel = models.ForeignKey (Personagem, on_delete = models.CASCADE, verbose_name = 'Responsável', limit_choices_to={'ativo': True},)
    # estoque = models

    class Meta:
        verbose_name = _("loja")
        verbose_name_plural = _("lojas")

    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse("personagem_detail", kwargs={"pk": self.pk})
