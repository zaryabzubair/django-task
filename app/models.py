from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee} - {self.position} ({self.start_date} to {self.end_date})"
