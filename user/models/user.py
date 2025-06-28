from django.db import models

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
     
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"User ID{self.id}: Name: {self.name}, Role: {self.role}"