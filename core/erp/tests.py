from config.wsgi import *
from core.erp.models import Type,Employee

# #LISTAR
# query=Type.objects.all()
# print(query)

 #Insertar
# t=Type(name='Asistente').save()

#Edicion
# t=Type.objects.get(pk=5)
# print(t.name)
# t.name='Gerente'
# t.save()

#otro tipo de listar
# obj=Type.objects.filter(name__icontains='Pre')
for i in Type.objects.filter(name__endswith='e'):
    print(i.name)

#Eliminacion
# try:
#     t=Type.objects.get(pk=10)
#     print(t.name)cls

#     t.delete()
# except Exception as e:
#     print(e)

