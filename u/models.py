from django.db import models as m
from django.contrib.auth.models import User as U


from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.translation import gettext_lazy as _

from a.models import N


class P(m.Model):

    u = m.OneToOneField(U, on_delete = m.CASCADE, related_name='p')

    n = m.CharField(_("Name"), max_length = 100)

    p = m.BooleanField(_("Premium"), default = False)

    an = m.ForeignKey(N, on_delete = m.DO_NOTHING, blank = True, null = True, related_name='an', verbose_name = 'Active Note')


    def __str__(self):
        
        return f"{self.n} | {self.u.username}"
    
    class Meta:

        ordering = ['-n']
        verbose_name = 'Profile'

@receiver(post_save, sender = U)
def cup(sender, instance, created, **kwargs):
    
    if created:

        P.objects.create(u = instance)