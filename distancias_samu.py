import numpy as np
import math


coord_grad = np.array([[40.416705,-3.703582], [48.856697,2.351462],
			  [51.507322,-0.127647], [55.953346,-3.188375],
			  [50.087465,14.421254], [54.347629,18.645232],
			  [52.517037,13.388860], [43.511638,16.439966],
			  [52.37454 ,4.8979760], [41.89332 ,12.482932],
			  [45.813177,15.977048], [47.498382,19.040471],
			  [38.707751,-9.136592]])

# Cambio de grados a radianes de las coordenadas
coord_rad = math.pi /180 * coord_grad

# inicialización de matriz de distancias
dist = np.zeros((coord_rad.shape[0],coord_rad.shape[0]))

# bucle for para la matriz de distancias
for j in range(13):
	for i in range(13-j):

		# Fórmula teorema esférico del coseno:
		cos_AB = (math.cos(coord_rad[i][0])*      
			   	  math.cos(coord_rad[i+j][0]) + 
			      math.sin(coord_rad[i][0])*
			      math.sin(coord_rad[i+j][0])*
			      math.cos(coord_rad[i+j][1]-coord_rad[i][1]))
		dist[i][i+j] = math.acos(cos_AB) * 6371

# Muestra por pantalla la matriz de distancias calculada:
dista = np.savetxt("samu.csv", dist, delimiter=",")
print(dist)

# AB= distancia entre las dos ciudades
# PB= latitud de ciudad 2
# PA= latitud ciudad 1
# Ultimo coseno la resta de las longitudes de las dos ciudades
# 6371km es el radio de La Tierra considerado

v_crucero = 900;

tiempo = dist / v_crucero
print(tiempo)