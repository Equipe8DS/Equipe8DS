from django.db import models
from django.utils.translation import gettext as _

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
    nome = models.CharField (max_length=100, blank=False )
    raca = models.CharField (max_length=100, choices = RACAS, null=False)
    classe = models.CharField (max_length=100, choices = CLASSE, null=False)
    tipo = models.CharField (max_length=100, editable=False, default='Jogador', choices=[('jogador', 'Jogador'), ('npc', 'NPC')])
    ativo = models.BooleanField (editable=False, default=True)

    class Meta:
        verbose_name = _("personagem")
        verbose_name_plural = _("personagens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("personagem_detail", kwargs={"pk": self.pk})

