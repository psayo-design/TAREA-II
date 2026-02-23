"""
=========================================================
Programa: Operaciones Matemáticas con Funciones Recursivas
Autor: Pablo Andrés Say Oliva
Curso: Programación
=========================================================
"""

# =========================================================
# FUNCIONES RECURSIVAS
# =========================================================

def convertir_a_binario(numero: int) -> str:
    """
    Convierte un número entero a su representación binaria
    utilizando recursividad.
    """
    if numero < 0:
        return "-" + convertir_a_binario(-numero)
    if numero < 2:
        return str(numero)
    return convertir_a_binario(numero // 2) + str(numero % 2)


def contar_digitos(numero: int) -> int:
    """
    Cuenta la cantidad de dígitos de un número entero
    utilizando recursividad.
    """
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)


def calcular_raiz_cuadrada(numero: int, candidato: int) -> int:
    """
    Función auxiliar recursiva que encuentra la raíz cuadrada entera.
    """
    if candidato * candidato > numero:
        return candidato - 1
    return calcular_raiz_cuadrada(numero, candidato + 1)


def raiz_cuadrada_entera(numero: int):
    """
    Devuelve la raíz cuadrada entera de un número.
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return calcular_raiz_cuadrada(numero, 0)


def convertir_a_decimal(romano: str) -> int:
    """
    Convierte un número romano a decimal utilizando recursividad.
    """
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    if not romano:
        return 0

    if len(romano) == 1:
        if romano not in valores:
            raise ValueError("Número romano inválido.")
        return valores[romano]

    if romano[0] not in valores:
        raise ValueError("Número romano inválido.")

    if valores[romano[0]] < valores.get(romano[1], 0):
        return convertir_a_decimal(romano[1:]) - valores[romano[0]]
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])


def suma_numeros_enteros(numero: int) -> int:
    """
    Suma todos los números desde 0 hasta un número positivo dado.
    """
    if numero < 0:
        raise ValueError("Debe ingresar un número entero positivo.")
    if numero == 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)


# =========================================================
# MENÚ INTERACTIVO
# =========================================================

def mostrar_menu():
    print("\n==============================")
    print("  MENÚ OPERACIONES RECURSIVAS")
    print("==============================")
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    print("3. Raíz Cuadrada Entera")
    print("4. Convertir Romano a Decimal")
    print("5. Suma de Números Enteros")
    print("6. Salir")


def main():
    """
    Función principal del programa.
    Controla el flujo del menú interactivo.
    """
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                numero = int(input("Ingrese un número entero: "))
                print("Resultado:", convertir_a_binario(numero))

            elif opcion == 2:
                numero = int(input("Ingrese un número entero: "))
                print("Cantidad de dígitos:", contar_digitos(numero))

            elif opcion == 3:
                numero = int(input("Ingrese un número entero: "))
                print("Raíz cuadrada entera:", raiz_cuadrada_entera(numero))

            elif opcion == 4:
                romano = input("Ingrese un número romano: ").upper()
                print("Equivalente decimal:", convertir_a_decimal(romano))

            elif opcion == 5:
                numero = int(input("Ingrese un número entero positivo: "))
                print("Resultado:", suma_numeros_enteros(numero))

            elif opcion == 6:
                print("Programa finalizado correctamente.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Ocurrió un error inesperado. Intente nuevamente.")


# =========================================================
# EJECUCIÓN
# =========================================================

if __name__ == "__main__":
    main()