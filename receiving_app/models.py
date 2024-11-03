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

        

class Staff_Record(models.Model):
    employee_id = models.IntegerField()
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return self.last_name

    #save input to uppercase
    def save(self):
        self.last_name = self.last_name.upper()
        self.first_name = self.first_name.upper()
        super(Staff_Record, self).save()  
