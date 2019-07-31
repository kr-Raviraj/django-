from django.db import models

# Create your models here.
class Student(models.Model):
    SId=models.IntegerField()
    Name=models.CharField(max_length=80)
    Branch=models.CharField(max_length=50)

    def __str__(self):

        return self.Name

    # def st1(self):
    #     return self.SId
    #
    # def st2(self):
    #     return self.Branch

