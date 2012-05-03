from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from registration.signals import user_registered

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    gender = models.CharField(choices=(settings.GENDER_CHOICES), max_length=20)
    birthday = models.DateField(blank=True)
    height = models.CharField(max_length=5, blank=True)
    weight = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.user.__unicode__()
    
def create_user_profile(sender, user, request, **kwargs):  
    profile, created = UserProfile.objects.get_or_create(user=user, birthday=request.POST.get('birthday'), gender=request.POST.get('gender'))
    
user_registered.connect(create_user_profile)
    
    