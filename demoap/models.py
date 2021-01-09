from django.db import models

from django.utils.translation import gettext, gettext_lazy, ugettext , ugettext_lazy


# Create your models here.

class DemoDB(models.Model):
    username = models.CharField(max_length=50, help_text=ugettext_lazy('help text1'))
    real_name = models.CharField(max_length=50, help_text=ugettext('help text2'))

    class Meta:
        verbose_name = 'DemoDB'
        db_table = 'demodb'