print("*****WEBPAY*****")
print("Bienvenio a WebPay")
print("Porfavor ingrese su nombre de usuario")
Usuario ={"Jesus": "1234", "angel": "a24y"}
nombreusuario =(input("Ingrese su nombre de usuario: "))
contraseña =(input("Ingrese su contraseña: "))
if nombreusuario in Usuario and Usuario [nombreusuario] == contraseña :
  print("Bienvenido",nombreusuario)
  print("Elija una de las opciones")
  print("Opcion 1: Pagar Monto")
  print("Opcion 2: Conocer mi saldo")
  print("Opcion 3: salir")
opcion=int(input("Seleccione una opcion: "))
if opcion == 1:
 totalpago=int(input("Ingrese la cantidad a pagar: "))
 print("su cantidad a pagar es: ",totalpago)
print("Metodo de Pago:   \n(1)tarjeta de credito \n(2)tarjeta de debito \n(3)Salir ")

