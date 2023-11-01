from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

GENDER_TYPES = (
    ("F", "Female"),
    ("M", "Male"),
)
    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    """ 
    Use the indexes option instead. Where possible, use the Meta.indexes option instead. In nearly all cases, indexes provides more functionality than db_index. db_index may be deprecated in the future. """
    email = models.EmailField(_("email address"), unique=True, db_index=True) 
    phone_number = models.CharField(_("phone number"), max_length=20, null=False, blank=False)
    # profile_img = models.FileField(
    #     max_length=1000, upload_to=img_url,
    #     null = True, blank=True
    # )
    
    #Same as django is_active auth model AbstractUser
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    #Same as django is_staff auth model AbstractUser
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    
    gender = models.CharField(
        choices=GENDER_TYPES,
        max_length=10,
        blank=True,
        null=True
    )
    address = models.ManyToManyField("app_platform.Address")
    dob = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    email_verified = models.BooleanField(_("email verified"),default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    objects = UserManager()
