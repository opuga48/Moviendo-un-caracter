import os
ac=0
posi=0
vali=0
op=""
pasos=0
def Derecha(posi,pasos):
	if(posi<pasos):
		posi=posi+1
	return(posi)

def Izquierda(posi):
	if(posi>0):
		posi=posi-1
	return(posi)

while(ac==0):
	ps=str(input("Introduzca la cantidad de pasos: "))
	if(ps.isdigit()==True and ps.lstrip('-').isdigit()== True) :
		pasos=int(ps)
		ac=1
		os.system("cls")
		while vali==0:
			print(" "*posi+"@")
			opp=str(input("Introduzca la accion a realizar por la arroba(d=derecha,i=izquierda) o presione s para salir: "))
			op=opp.lower()
			if(op=="d"):
				posi=Derecha(posi,pasos)
			if op=="i":
				posi=Izquierda(posi)
			elif(op=="s"):
				vali=10
			os.system("cls") 
		print("Gracias por su preferencia")
	else:
		print("Entrada invalida, debe ser un numero igual o mayor a 0")
        