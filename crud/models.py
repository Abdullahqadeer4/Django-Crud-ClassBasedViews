from django.db import models

# Create your models here.

class location(models.Model):
    locationname=models.CharField(max_length=30,unique=True)
    ltype=models.CharField(max_length=50)
    lserial=models.IntegerField()
    
    def __str__(self):
        return self.locationname
    
class items(models.Model):
    iname=models.CharField(max_length=30)
    itype=models.CharField(max_length=50)
    iserial=models.IntegerField()
    itemlocation=models.ForeignKey(location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.iname
    
