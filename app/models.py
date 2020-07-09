from django.db import models

class Produtos(models.Model):

    price = models.FloatField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    base_discount_percent = models.FloatField()

    class Meta:
        db_table = 'produtos'
        
        constraints = [
            models.CheckConstraint(check=models.Q(base_discount_percent__lte=25.0), name='base_discount_max')
        ]


    def __str__(self):
        return self.title


class Usuarios(models.Model):
    

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    class Meta:
        db_table = 'usuarios'
    

    def __str__(self):
        return self.first_name
