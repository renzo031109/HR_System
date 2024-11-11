from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=200)

    class Meta:
        ordering = ["department"]

    def __str__(self):
        return self.department

    #save input to uppercase
    def save(self):
        self.department = self.department.upper()
        super(Department, self).save()  



class Client(models.Model):
    client = models.CharField(max_length=200)

    class Meta:
        ordering = ["client"]

    def __str__(self):
        return self.client

    #save input to uppercase
    def save(self):
        self.client = self.client.upper()
        super(Client, self).save()  


class Component(models.Model):
    component = models.CharField(max_length=200)

    class Meta:
        ordering = ["component"]

    def __str__(self):
        return self.component
    
    #save input to uppercase
    def save(self):
        self.component = self.component.upper()
        super(Component, self).save()

        

class Employee_Record(models.Model):
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.last_name

    #save input to uppercase
    def save(self):
        self.last_name = self.last_name.upper()
        self.first_name = self.first_name.upper()
        super(Employee_Record, self).save()  
