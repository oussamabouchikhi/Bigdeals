from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save

# User Profile Model
class Profile(models.Model):
    # each user has one profile
    user      = models.OneToOneField(User, verbose_name = _("user"), on_delete=models.CASCADE)
    slug      = models.SlugField(blank=True, null=True, verbose_name=_("URL"))
    image     = models.ImageField(upload_to='profile_img', verbose_name=_("image"), blank=True, null=True)
    country   = CountryField()
    address   = models.CharField(max_length=100)
    join_date = models.DateTimeField(verbose_name=_("join date"), default = datetime.datetime.now)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    """
    Override save method
    **kwargs: used when we don't know
    how much info a function will get
    """
    def save(self, *args, **kwargs):
        # if there is no slug
        if not self.slug :
            # Generate a slug from username
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})

    # auto create a profile for any user created
    def create_profile(sender, **kwargs):
        # When a new user is created some data will be sent ['instance'. 'created', 'row'...]
        # so if there is info 'created' received
        if kwargs['created']:
            # create a profile for this user with this instance info
            user_profile = Profile.objects.Create(user = kwargs['instance'])

    """ Connect create_profile with User
    - sender(All user info) will be kwargs
    """
    post_save.connect(create_profile, sender = User)
