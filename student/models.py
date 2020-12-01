from django.db import models

class Student(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    name = models.CharField(max_length=120)
    picture = models.ImageField(upload_to= 'studentphoto')
    father = models.CharField(max_length=120)
    mother = models.CharField(max_length=120)
    roll = models.IntegerField(max_length=6, unique=True)
    reg = models.IntegerField(max_length=6, unique=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    dob = models.DateField()
    date_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.roll)