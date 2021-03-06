from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
import random
# Create your models here.


class PdfInput(models.Model):
    """SQL table associating the membership form with the user"""
    user = models.OneToOneField(User, on_delete=ChildProcessError)
    pdf_file = models.FileField(upload_to='user_experience/static/user_experience/')


class PdfOutput(models.Model):
    """SQL table associating the membership form with the user"""
    user = models.OneToOneField(User, on_delete=ChildProcessError)
    pdf_file = models.FileField(upload_to='user_experience/static/user_experience/pdf_output/')


class Workshop(models.Model):
    """SQL table containing information for each workshop"""
    type = models.CharField(max_length=30)
    nb_places = models.IntegerField()
    places = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        """Customizing the print python method"""
        return "ATELIER : {} ||| DATE : {} ||| PLACES : {} ||| ID : {} "\
            .format(self.type, self.date, self.nb_places, self.id)

    def get_absolute_url(self):
        return reverse('admin')


class Client(models.Model):
    """SQL table containing the information of each client of the association"""
    user = models.OneToOneField(User, on_delete=ChildProcessError)
    first_name = models.CharField(max_length=254, default="test")
    last_name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=10)
    date_birth = models.DateTimeField(default=timezone.now)
    mail_adress = models.EmailField(max_length=30)

    def __str__(self):
        return "CLIENT : {} NOM : {} ID : {}\n Tél : {} Email : {}"\
            .format(self.first_name, self.last_name, self.id, self.Phone, self.mail_adress)


class Inscribe(models.Model):
    """SQL table managing customer registration for workshops"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return "id = " + str(self.workshop.id)


class SecretCode(models.Model):
    """SQL table containing the secret code for each user"""
    user = models.OneToOneField(User, on_delete=ChildProcessError)
    code = models.CharField(max_length=254, default=str(random.randint(10001, 99999)))

    def __str__(self):
        return f"Utilisateur : {self.user.username} / Code secret : {self.code}"