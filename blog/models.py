from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Post(models.Model):
    title = models.CharField(_('title'),max_length=100)
    content = models.TextField(_("content"))
    date_posted = models.DateTimeField(_("date posted"),default=timezone.now)
    author = models.ForeignKey(User,verbose_name=_("author"), on_delete=models.CASCADE)   # cascade --> nese fshihet user,
                                                                 # fshihen dhe postimet e tij por jo e kunderta

    def __str__(self):
        return self.title

    def get_absolute_url(self):          #kthen full path si string pasi ben nje post
        return reverse('post-detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')