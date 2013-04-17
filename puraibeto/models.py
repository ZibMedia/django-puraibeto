from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from . import fields
from . import settings



class AttachedFileBase(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey('content_type', 'object_id')

    file = fields.PrivateFileField()
    name = models.CharField(verbose_name=_('Name'), blank=True, null=True)
    description = models.TextField(verbose_name=("Description"), blank=True, null=True)

    class Meta:
        abstract = True
        permissions = (
            ('can_view', 'Can see file in lists'),
            ('can_download', 'Can download file'),
            ('can_remove', 'Can remove file'),
        )

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        # for now we'll assume you're attaching your urlpatterns under a
        # route that uses 'attached_pk' as a url argument
        return ('puraibeto_download', (), {
            'attached_pk': self.object_id,
            'pk': self.pk,
        })


class PrivateFile(AttachedFileBase): pass