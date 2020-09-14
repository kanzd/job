from django.db import models

class users(models.Model):
    id= models.AutoField
    name=models.CharField(max_length=30)
    passcode=models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
class bookings(models.Model):
    id=models.AutoField
    user=models.CharField(max_length=30)
    time=models.TextField(blank=True)
    pastbook=models.TextField(blank=True)
    near=models.TextField(blank=True)
    location=models.CharField(max_length=30)
    Aloc=models.CharField(max_length=30)
    Bloc=models.CharField(max_length=30)
    def get_time(self):
        if self.time:
            return self.time.split(',')
        else:
            return []
    def set_time(self,time):
        if self.time:
            self.time=self.time+' , '+time
            return True
        else:
            self.time=time
            return False

    def get_pastbook(self):
        if self.pastbook:
            return self.pastbook.split(',')
        else:
            return []

    def set_pastbook(self, books):
        if self.pastbook:
            self.pastbook = self.pastbook + ' , ' + books
            return True
        else:
            self.pastbook = books
            return False
    def get_near(self):
        if self.near:
            return self.near.split(',')
        else:
            return []
    def set_near(self,near):
        if self.near:
            self.near=self.near+' , '+near
            return True
        else:
            self.near=near
            return False
    def __str__(self):
        return str(self.id)


