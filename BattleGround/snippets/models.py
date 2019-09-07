from django.db import models

# Create your models here.

from django.db import models

class Cube(models.Model):
    name = models.CharField(max_length = 100,default = "cube",blank = False,unique = False)
    length = models.FloatField(default = 1.0,blank = False)
    x_coordinate = models.FloatField(default = 0.0,blank = False)
    y_coordinate = models.FloatField(default = 0.0,blank = False)
    z_coordinate = models.FloatField(default = 0.0,blank = False)
    texID = models.IntegerField(default = 0,blank = False)
    mass = models.FloatField(default = 0.0,blank = False)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.name, self.length, self.x_coordinate,self.y_coordinate,self.z_coordinate,self.texID,self.mass)



class Rectangle(models.Model):
    ORIENTATION_CHOICES = (
        (0,"XY"),
        (1,"ZX"),
        (2,"ZY")
    )
    name = models.CharField(max_length = 100,default = "rectangle",blank = False,unique = False)
    length = models.FloatField(default = 1.0,blank = False)
    breadth = models.FloatField(default = 1.0,blank = False)
    x_coordinate = models.FloatField(default = 0.0,blank = False)
    y_coordinate = models.FloatField(default = 0.0,blank = False)
    z_coordinate = models.FloatField(default = 0.0,blank = False)
    texID = models.IntegerField(default = 0,blank = False)
    mass = models.FloatField(default = 0.0,blank = False)
    orientation = models.IntegerField(default = 0 ,blank = False,choices = ORIENTATION_CHOICES)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.name, self.length,self.breadth, self.x_coordinate,self.y_coordinate,self.z_coordinate,self.texID,self.mass,self.orientation)


