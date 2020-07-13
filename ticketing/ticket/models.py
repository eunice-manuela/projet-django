from django.db import models
from django.utils.timezone import now

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings

class BaseUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

class Service(models.Model):
    nom = models.CharField(_('Identifiant Client'), max_length=50, verbose_name='Nom du service')

    def __str__(self):
        return self.nom

class Client(models.Model):
    base_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)

class Ticket(models.Model):
    ETATS = (
        ('Créé', _('Créé')),
        ('En cours', _('En cours')),
        ('Résolu', _('Résolu'))
    )

    cas = models.CharField(_('Description'), max_length=255)
    etat = models.CharField(_('Etat du ticket'), choices=ETATS, max_length=10)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    commentaire = models.CharField(max_length=255, blank=True, null=True)