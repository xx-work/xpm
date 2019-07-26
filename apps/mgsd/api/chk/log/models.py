from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _, ugettext
from django.utils.encoding import python_2_unicode_compatible, smart_text
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class Log(models.Model):
    action_time = models.DateTimeField(
        _('action time'),
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name=_('user'),
    )
    ip_addr = models.GenericIPAddressField(_('action ip'), blank=True, null=True)
    content_type = models.ForeignKey(
        ContentType,
        models.SET_NULL,
        verbose_name=_('content type'),
        blank=True, null=True,
    )
    object_id = models.TextField(_('object id'), blank=True, null=True)
    object_repr = models.CharField(_('object repr'), max_length=200)
    action_flag = models.CharField(_('action flag'), max_length=32)
    message = models.TextField(_('change message'), blank=True)

    class Meta:
        verbose_name = _('log entry')
        verbose_name_plural = _('log entries')
        ordering = ('-action_time',)
        db_table = 'orm_log'

    def __repr__(self):
        return smart_text(self.action_time)

    def __str__(self):
        if self.action_flag == 'create':
            return ugettext('Added "%(object)s".') % {'object': self.object_repr}
        elif self.action_flag == 'change':
            return ugettext('Changed "%(object)s" - %(changes)s') % {
                'object': self.object_repr,
                'changes': self.message,
            }
        elif self.action_flag == 'delete' and self.object_repr:
            return ugettext('Deleted "%(object)s."') % {'object': self.object_repr}

        return self.message

    def get_edited_object(self):
        "Returns the edited object represented by this log entry"
        return self.content_type.get_object_for_this_type(pk=self.object_id)