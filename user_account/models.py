from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField


GENDER_TYPES = (
    ("F", "Female"),
    ("M", "Male"),
)
    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    """ 
    Use the indexes option instead. Where possible, use the Meta.indexes option instead. In nearly all cases, indexes provides more functionality than db_index. db_index may be deprecated in the future. """
    email = models.EmailField(
        _("email address"), 
        unique=True, 
        db_index=True
    ) 
    phone_number = PhoneNumberField(region="PH")
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
    
class Professional(models.Model):
    class LOCATION_TYPE(models.TextChoices):
        LOCAL = ("LOCAL", _("Local"))
        ANY = ("ANY", _("Anywhere"))
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    location_type = models.CharField(
        _("location type"),
        choices=LOCATION_TYPE.choices,
        max_length=15,
        default=LOCATION_TYPE.LOCAL
    )
    #If the location type is LOCAL then we need to set this field
    service_area_radius = models.IntegerField(
        _("service area radius"),
        help_text=_("Define a specific distance within which you are willing to provide your services."),
        blank=True,
        null=True
    )
    service_area = models.ManyToManyField(
        to="app_platform.City",
        related_name="professionals_multi_area"
    )
    base_location = models.ForeignKey(
        to="app_platform.City",
        help_text=_("Specify the central location, or origin."),
        related_name="professionals",
        on_delete=models.DO_NOTHING
    )
    about_me = models.TextField(_("about me"), null=True, blank=False)