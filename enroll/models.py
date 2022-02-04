from django.db import models


class BaseModel(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    city = models.CharField(max_length=90)
    age = models.IntegerField()


class TeacherModel(BaseModel):
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class StudentModel(BaseModel):
    roll = models.IntegerField()
    date = models.DateField()
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
