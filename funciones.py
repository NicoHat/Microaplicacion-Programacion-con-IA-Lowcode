import json
import pandas as pd
from typing import List, Dict, Any


def cargar_datos(ruta_archivo: str) -> List[Dict[str, Any]]:
    """Carga los datos de los jugadores desde el archivo JSON con manejo de errores."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: El archivo JSON está corrupto o mal formateado.")
        return []


def filtrar_por_equipo(datos: List[Dict[str, Any]], equipo_buscado: str) -> List[Dict[str, Any]]:
    """Filtra y devuelve los jugadores que pertenecen a un equipo específico usando Pandas."""
    try:
        df = pd.DataFrame(datos)
        if df.empty:
            print("⚠️ No hay datos cargados en el sistema.")
            return []
        
        resultado_df = df[df['equipo'].str.contains(equipo_buscado, case=False, na=False)]
        return resultado_df.to_dict(orient='records')
    except Exception as e:
        print(f"❌ Ocurrió un error al filtrar por equipo: {e}")
        return []


def filtrar_por_posicion(datos: List[Dict[str, Any]], posicion_buscada: str) -> List[Dict[str, Any]]:
    """Filtra los jugadores según su posición en la cancha."""
    try:
        df = pd.DataFrame(datos)
        if df.empty:
            return []
        
        resultado_df = df[df['posicion'].str.contains(posicion_buscada, case=False, na=False)]
        return resultado_df.to_dict(orient='records')
    except Exception as e:
        print(f"❌ Ocurrió un error al filtrar por posición: {e}")
        return []


def calcular_estadisticas_avanzadas(datos: List[Dict[str, Any]]) -> None:
    """Calcula indicadores clave y estadísticos utilizando Pandas."""
    try:
        df = pd.DataFrame(datos)
        if df.empty:
            print("⚠️ No hay datos suficientes para calcular indicadores.")
            return

        print("\n--- 📊 ESTADÍSTICAS AVANZADAS DE LA LIGA ---")
        
        # 1. Total de jugadores registrados
        total_jugadores = len(df)
        print(f"1. Total de futbolistas analizados: {total_jugadores}")

        # 2. Promedio de edad general en la liga
        if 'edad' in df.columns:
            promedio_edad = df['edad'].mean()
            print(f"2. Promedio de edad general: {promedio_edad:.1f} años")

        # 3. Cantidad de equipos analizados
        if 'equipo' in df.columns:
            total_equipos = df['equipo'].nunique()
            print(f"3. Total de equipos incluidos: {total_equipos}")

        # 4. Nacionalidad más frecuente
        if 'nacionalidad' in df.columns:
            nacionalidad_comun = df['nacionalidad'].mode()[0]
            print(f"4. Nacionalidad predominante: {nacionalidad_comun}")

    except Exception as e:
        print(f"❌ Error al calcular las estadísticas: {e}")


def agregar_jugador(ruta_archivo: str, datos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Permite registrar un nuevo jugador completo y actualizar el archivo JSON."""
    try:
        print("\n--- Registro de Nuevo Jugador ---")
        equipo = input("Ingrese el equipo: ").strip()
        dorsal = int(input("Ingrese el dorsal: "))
        nombre = input("Ingrese el nombre del jugador: ").strip()
        posicion = input("Ingrese la posición: ").strip()
        edad = int(input("Ingrese la edad: "))
        nacionalidad = input("Ingrese la nacionalidad: ").strip()
        altura = input("Ingrese la altura (ej: 1,80m): ").strip()
        pie_dominante = input("Ingrese el pie dominante (Derecho/Izquierdo): ").strip()
        valor_mercado = input("Ingrese el valor de mercado (ej: 5,00 mill. €): ").strip()

        nuevo = {
            "equipo": equipo,
            "dorsal": dorsal,
            "nombre": nombre,
            "posicion": posicion,
            "fecha_nacimiento": "N/D",
            "edad": edad,
            "nacionalidad": nacionalidad,
            "altura": altura,
            "pie_dominante": pie_dominante,
            "fecha_llegada": "N/D",
            "club_procedente": "N/D",
            "fecha_contrato": "N/D",
            "valor_mercado": valor_mercado
        }

        datos.append(nuevo)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        print("✅ ¡Jugador agregado y guardado con éxito en el JSON!")
        return datos
    except ValueError:
        print("❌ Error: La edad y el dorsal deben ser números enteros válidos.")
        return datos
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al guardar: {e}")
        return datos