class cola(object):
    def __init__(self):
        self.items=[]

    def encolar (self,x):
        self.items.append(x)

    def vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def desencolar(self):
        if self.vacia():
            return None
        else:
            return self.items.pop(0)
def registro():
    cola1 =cola()
    print("****** Bienvenido ******* ")
    while True:
        x=0
        print("""
        1. registrar empleado
        2. pagar al  empleado 
        3. cantidad de empleados actualmente 
        4. salir""")
        x= input("por favor ingrese una opcion ")
        x=int(x)
        if x==1:
            empleado=input("nombre del empleado: ")
            cola1.encolar(empleado)
            idd=int(input("cual es su numero de identicacion: "))
            horas = int(input("digite sus horas trabajadas: "))
            sueldo = int(input("digite su sueldo por hora: "))
            st=horas*sueldo
        elif x==2:
            print("    registro de pago       ")
            print("empleado:",empleado,"\nsu sueldo es de:",st)
        elif x==3:
            print(len(cola1.items))
        elif x==4:
            break
        else: 
            print("digite una opcion valida")
registro()

