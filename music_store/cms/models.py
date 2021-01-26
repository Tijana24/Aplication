from django.db import models

# Create your models here.
class Service(models.Model):
    name= models.CharField(max_length=150)
    description= models.CharField(max_length=450)
    image= models.URLField(default="https://i.pinimg.com/originals/a6/98/a0/a698a0a05318d6753c67635c32b9a7ae.jpg")
    price= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
    
