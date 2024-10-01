def registrar_goles(nombre_equipo, goles_favor=0, goles_contra=0):
    equipos[nombre_equipo]["goles_favor"] += goles_favor
    equipos[nombre_equipo]["goles_contra"] += goles_contra

def registrar_estadisticas_jugador(nombre_equipo, nombre_jugador, goles=0, tarjetas_amarillas=0, tarjetas_rojas=0, faltas=0):
    jugador = equipos[nombre_equipo]["jugadores"][nombre_jugador]
    jugador["goles_anotados"] += goles
    jugador["tarjetas_amarillas"] += tarjetas_amarillas
    jugador["tarjetas_rojas"] += tarjetas_rojas
    jugador["faltas_cometidas"] += faltas

    def equipo_mas_goles():
    return max(equipos, key=lambda e: equipos[e]["goles_favor"])

def equipo_mas_goles_contra():
    return max(equipos, key=lambda e: equipos[e]["goles_contra"])

def equipo_ultimo():
    return min(equipos, key=lambda e: equipos[e]["puntos"])

def jugador_mas_faltas():
    max_faltas = 0
    jugador_max = None
    for equipo in equipos.values():
        for jugador, stats in equipo["jugadores"].items():
            if stats["faltas_cometidas"] > max_faltas:
                max_faltas = stats["faltas_cometidas"]
                jugador_max = jugador
    return jugador_max