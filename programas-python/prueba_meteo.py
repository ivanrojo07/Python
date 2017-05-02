from meteo import Meteo, mostrar_meteo

cs = Meteo(estacion='CS1', temp=[20.2, 19.1, 27.2, 24.8], lluvia=[0, 0, 0, 0])
mostrar_meteo(cs)
