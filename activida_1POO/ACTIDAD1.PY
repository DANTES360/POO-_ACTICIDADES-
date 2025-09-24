#Calcular el promedio de una lista de calificaciones
def calcular_promedio(calificacione):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)
def main ():
    print("===promedio de calificaciones==="")
          calificaciones = []
          #bucle para ingresar 5 calificaciones 
          for i range(5):
          nota = float(input("ingrsr la cilificacion #{i+1}: " ))
            # Condicional para validar la nota
        if nota < 0 or nota > 100:
            print(" Nota inválida, debe estar entre 0 y 100")
        else:
            calificaciones.append(nota)

    # Mostrar las calificaciones
    print("\nLas calificaciones ingresadas fueron:")
    for nota in calificaciones:
        print(f"- {nota}")

    # Llamar a la función para calcular el promedio
    promedio = calcular_promedio(calificaciones)

    # Mostrar resultado con condicional
    print(f"\nEl promedio es: {promedio:.2f}")
    if promedio >= 70:
        print("Aprobado")
    else:
        print("Reprobado")


# ------------------------
# Ejecutar el programa principal
if _name_ == "_main_":
    main()