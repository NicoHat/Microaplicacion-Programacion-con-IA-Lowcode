from funciones import cargar_datos, filtrar_por_equipo, filtrar_por_posicion, calcular_estadisticas_avanzadas, agregar_jugador

def main() -> None:
    archivo_datos = "datos.json"
    jugadores = cargar_datos(archivo_datos)

    while True:
        print("\n==================================================")
        print(" ⚽ GESTIÓN LIGA PROFESIONAL DE FÚTBOL ARGENTINO ⚽ ")
        print("==================================================")
        print("1. Filtrar jugadores por equipo")
        print("2. Filtrar jugadores por posición")
        print("3. Ver estadísticas avanzadas (Pandas)")
        print("4. Agregar un nuevo jugador")
        print("5. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))

            if opcion == 1:
                busqueda = input("Ingrese el nombre del equipo: ")
                filtrados = filtrar_por_equipo(jugadores, busqueda)
                if filtrados:
                    print(f"\n--- Jugadores de '{busqueda}' ---")
                    for j in filtrados:
                        print(f"• [Dorsal {j.get('dorsal')}] {j.get('nombre')} - {j.get('posicion')} ({j.get('edad')} años, {j.get('altura')})")
                else:
                    print("⚠️ No se encontraron registros para ese equipo.")

            elif opcion == 2:
                busqueda = input("Ingrese la posición (ej: Portero, Delantero): ")
                filtrados = filtrar_por_posicion(jugadores, busqueda)
                if filtrados:
                    print(f"\n--- Jugadores en posición '{busqueda}' ---")
                    for j in filtrados:
                        print(f"• {j.get('nombre')} ({j.get('equipo')}) - Valor: {j.get('valor_mercado')}")
                else:
                    print("⚠️ No se encontraron registros para esa posición.")

            elif opcion == 3:
                calcular_estadisticas_avanzadas(jugadores)

            elif opcion == 4:
                jugadores = agregar_jugador(archivo_datos, jugadores)

            elif opcion == 5:
                print("\n¡Gracias por usar la aplicación! Saliendo...")
                break
            else:
                print("❌ Opción inválida. Elija un número entre 1 y 5.")

        except ValueError:
            print("❌ Error: Debe ingresar obligatoriamente un número entero.")

if __name__ == "__main__":
    main()