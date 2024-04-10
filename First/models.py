from django.db import models

class Building(models.Model):
    Nazvanie = models.CharField(max_length=100)
    Type_Zdanya = models.CharField(max_length=100)
    Adress = models.CharField(max_length=100)
    Square = models.IntegerField()

    def __str__(self):
        return self.Nazvanie

class Project(models.Model):
    Name = models.CharField(max_length=100)
    Data_start = models.DateField()
    Data_end = models.DateField()

    def __str__(self):
        return self.Name

class Manage(models.Model):
    ID_Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ID_Building = models.ForeignKey(Building, on_delete=models.CASCADE)
    Data_start = models.DateField()
    Data_end = models.DateField()