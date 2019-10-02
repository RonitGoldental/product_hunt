from django.db import models
from django import forms


class Accounts(models.Model):
    name=models.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

