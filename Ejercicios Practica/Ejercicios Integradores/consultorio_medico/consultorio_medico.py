from validates import validar_edad, validar_sintomas

salida = "s"
acumulador_edad = 0
total_pacientes = 0
contador_fiebre = 0
contador_dolor_cabeza = 0
edad_paciente_mas_joven = ""
nombre_paciente_mas_joven = ""
sintoma_paciente_mas_joven = ""
bandera_paciente_mas_joven = 0



while salida == "s":

    nombre_paciente = input("Nombre del paciente: ")
    edad_paciente = validar_edad(input("Edad: "))
    sintoma_principal = validar_sintomas(input("Sintoma principal: ").lower())

    acumulador_edad += int(edad_paciente)
    total_pacientes += 1

    if sintoma_principal == "fiebre":
            contador_fiebre += 1
    else:
            contador_dolor_cabeza += 1
    

    #mas_joven = buscar_paciente_mas_joven(nombre_paciente,edad_paciente,sintoma_principal, bandera_paciente_mas_joven)
    #print(mas_joven)




    salida = input("¿Desea agregar otro paciente? S/N: ").lower()

promedio_edad = acumulador_edad // total_pacientes
print(f"Promedio de edad: {promedio_edad}")

if contador_fiebre > contador_dolor_cabeza:
    print("Consultar sobre posibles infecciones.")
elif contador_dolor_cabeza > contador_fiebre:
    print("Posible estrés o migraña.")
else:
    ("Síntoma no identificado, consultar más detalles.")






'''def buscar_paciente_mas_joven(nombre, edad, sintoma, bandera):
    
    if bandera_paciente_mas_joven == 0:
        nombre_paciente_mas_joven = nombre
        edad_paciente_mas_joven = edad
        sintoma_paciente_mas_joven = sintoma
        bandera_paciente_mas_joven = 1
    if edad > edad_paciente_mas_joven:
        nombre_paciente_mas_joven = nombre
        edad_paciente_mas_joven = edad
        sintoma_paciente_mas_joven = sintoma
    paciente_mas_joven = [nombre_paciente_mas_joven, edad_paciente_mas_joven, sintoma_paciente_mas_joven]
    return paciente_mas_joven'''