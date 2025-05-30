from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
