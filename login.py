import re

def es_contraseña_segura(contraseña):
    return (re.search(r'[a-z]', contraseña) and
            re.search(r'[A-Z]', contraseña) and
            re.search(r'[0-9]', contraseña))

def registrar_usuario(ruta):
    print("\n--- Registro de Cliente ---")
    nombres = input("Nombres: ").strip()
    identificacion = input("Identificación: ").strip()
    edad = input("Edad: ").strip()
    usuario = input("Correo electrónico: ").strip()
    
    while True:
        contraseña = input("Contraseña (minimo una minuscula, mayuscula y numero): ")
        if es_contraseña_segura(contraseña):
            break
        print("Contraseña no segura. Intenta de nuevo.")

    with open(ruta, 'a') as f:
        f.write(f"{nombres},{identificacion},{edad},{usuario},{contraseña}\n")
    print("Usuario registrado.")

def iniciar_sesion_cliente(ruta):
    print("\n--- Inicio de Sesión Cliente ---")
    usuario = input("Correo electrónico: ").strip()
    contraseña = input("Contraseña: ")

    try:
        with open(ruta, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) == 5 and datos[3] == usuario and datos[4] == contraseña:
                    print("Sesion iniciada.")
                    funcion_cliente(usuario)
                    return True
        print("Usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
    return False

def iniciar_sesion_admin():
    print("\n--- Inicio de Sesion Administrador ---")
    usuario = input("Correo electronico: ").strip()
    contraseña = input("Contraseña: ")

    if usuario == "administrador@epn.edu.com" and contraseña == "Uz4s4r82":
        print("Sesion de administrador iniciada.")
        funcion_administrador()
        return True
    else:
        print("Credenciales incorrectas.")
        return False

def funcion_administrador():
    print("\nBienvenido ADMINISTRADOR")





    print("Funciones de administrador aún por implementar.")



    

def funcion_cliente(usuario):
    print(f"\nBienvenido {usuario}")







    print("Funciones de cliente aún por implementar.")







def menu_cliente(ruta):
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Registrar")
        print("2. Iniciar sesión")
        print("3. Volver")
        opcion = input("Opción: ").strip()

        if opcion == '1':
            registrar_usuario(ruta)
        elif opcion == '2':
            if iniciar_sesion_cliente(ruta):
                break
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

def main():
    ruta = "usuarios.txt"
  
    while True:
        print("\n=== Menú Principal ===")
        print("1. Administrador")
        print("2. Cliente")
        print("3. Salir")
        opcion = input("Opción: ").strip()

        if opcion == '1':
            iniciar_sesion_admin()
        elif opcion == '2':
            menu_cliente(ruta)
        elif opcion == '3':
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida.")

main()
