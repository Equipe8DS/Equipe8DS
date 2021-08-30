from django.db import models
from django.utils.translation import gettext as _

class Personagem (models.Model): 
    nome = models.CharField (max_length=100)
    raca = models.CharField (max_length=100)
    classe = models.CharField (max_length=100)
    tipo = models.CharField (max_length=100)
    ativo = models.BooleanField (editable=False, default=True)

    class Meta:
        verbose_name = _("personagem")
        verbose_name_plural = _("personagens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("personagem_detail", kwargs={"pk": self.pk})