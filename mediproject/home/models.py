from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserSignupDb(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobileNumber=models.CharField(max_length=20)
    age=models.IntegerField()
    choice=[('M','Male'),('F','Female'),('O','Others')]
    gender=models.CharField(choices=choice,null=True,max_length=1)
    
    def __str__(self):
        return self.user.username

class UserImage(models.Model):
    patienteye=models.ImageField(upload_to="retinal_scan",blank=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    dateOfUpload=models.DateField()
    timeOfUpload=models.TimeField()

    def __str__(self):
        return self.name.username