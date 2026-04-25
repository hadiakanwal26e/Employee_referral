from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    cnic = models.CharField(max_length=15)
    cell = models.CharField(max_length=15)
    job_title_working = models.CharField(max_length=200)
    for_job = models.CharField(max_length=200)
    skill_set = models.TextField()
    department = models.CharField(max_length=200)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.employee_name