from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id'] #si es descendente ['-id]

class Category(models.Model): 
    name = models.CharField(max_length=150,verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['id'] #si es descendente ['-id]

class Employee(models.Model):
    type=models.ForeignKey(Type, on_delete=models.CASCADE) #Set Null para q no se borre, 
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    date_joined=models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation=models.DateTimeField(auto_now=True) #la fecha se actualiza una vez (inicio)
    date_updated=models.DateTimeField(auto_now_add=True) #la fecha se actualiza automaticamente al modificar elregistro
    age=models.PositiveIntegerField(default=0)
    salary=models.DecimalField(default=0,max_digits=9,decimal_places=2)
    state=models.BooleanField(default=True)
    # gender=models.CharField(max_length=50)
    avatar=models.ImageField(upload_to='avatar/%Y/%m%d',null=True,blank=True) #para guardar en carpeta por fecha
    cvitae=models.ImageField(upload_to='cvitae/%Y/%m%d',null=True,blank=True) #para guardar en carpeta por fecha

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        # db_table='empleado' #el nombre como se va a crear la tabla
        ordering=['id'] #si es descendente ['-id]



    








