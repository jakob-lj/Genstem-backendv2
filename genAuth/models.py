
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
import secrets
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, **kwargs):
        user = self.model(email=email, name=name)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, **kwargs):
        user = self.create_user(name, email)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)


class User(AbstractUser):
    username=None
    #identifier = models.CharField(max_length=225, unique=True, default=getPk)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=225, default='John Doe')
    email = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    dummy = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=[]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def getShortName(self):
        return str(self.name).split(' ')[0]

    # def getAccess(self):
    #     tokens = get_tokens_for_user(self)
    #     url = 'https://owe-it.com/landing/loginAsUser/%s' % tokens['access']
    #     print(url)
    #     #return url


class UserVerificationToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200, default=secrets.token_hex(), editable=False, unique=True)
    date = models.DateField(auto_now=True)
