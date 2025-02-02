from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user") , on_delete=models.CASCADE)  # cascade --> nese fshihet user,
                                                                # fshihet dhe profili i tij por jo e kunderta
    image = models.ImageField(_('image'), default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # del te admini emri i profilit me foton perkatese

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')