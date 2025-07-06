from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Gender(models.TextChoices):
    MALE = "male","Male"
    FEMALE = "female", "Female"
    
class User(models.Model):
    id = models.AutoField(primary_key=True, db_comment="PK of a User", help_text="PK of a User")
    username = models.CharField(max_length=150,unique=True)
    name = models.CharField(max_length= 150)
    gender = models.CharField(max_length= 10,choices=Gender.choices)
    birth_date = models.DateField(null=True,blank=True)
    created_date = models.DateTimeField()
    email = models.CharField(max_length=120,null=True,blank=True)
    password = models.CharField(max_length=128, db_comment="Hashed password of the user", help_text="Hashed password of the user")
    active = models.BooleanField(default=True)


    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    

    def __str__(self):
        return f"User ID{self.id}: Name: {self.name}, Username: {self.username}, Email: {self.email}, Active: {self.active}"