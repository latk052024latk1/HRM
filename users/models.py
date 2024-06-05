from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils import timezone



def modify_fields(**kwargs):
    def wrap(cls):
        for field, prop_dict in kwargs.items():
            for prop, val in prop_dict.items():
                setattr(cls._meta.get_field(field), prop, val)
        return cls
    return wrap



@modify_fields(username={'verbose_name': 'მომხმარებლის სახელი','help_text': ''})
class User(AbstractUser):
    phone = models.CharField(max_length=16,  blank=True, null=True, verbose_name="ტელეფონი")
    birth_date = models.DateField(blank=True, null=True, verbose_name="დაბადების თარიღი")
    photo = models.ImageField(default = "user_photo/default_user_picture.png",upload_to = 'user_photo', null=True, blank=True)


    def display_login(self):
        t_login = self.last_login.strftime("%d.%m.%Y, %H:%M:%S")
        return t_login

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/user_photo/default_user_picture.png"



class UserActions(models.Model):
    act_id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100,  blank=False, verbose_name="Action")
    time_affected = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Time")

    def display_affected(self):
        time0 = self.time_affected.strftime("%d.%m.%Y, %H:%M:%S")
        return time0


