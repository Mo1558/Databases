from django.db import models


class Client(models.Model):
    '''
    this is a model for client have many fields client
    name,logo and country (related at country  model)
    '''
    name=models.CharField(max_length=20)
    logo=models.FileField(upload_to='logos')
    country=models.ForeignKey('Country',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)





class Country(models.Model):
    '''
    it is country model have many fields name and flag 
    '''
    name=models.CharField(max_length=25)
    flag=models.FileField(upload_to='Flags')

    def __str__(self):
        return self.name