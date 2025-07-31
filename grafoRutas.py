#Bryan Angulo
grafoDistancias = {
    'Tulcan': [('Ibarra', 126)],
    'Ibarra': [('Tulcan', 126), ('Quito', 113)],
    'Quito': [('Ibarra', 113), ('SantoDomingo', 152), ('Ambato', 151), ('Tena', 192)],
    'SantoDomingo': [('Quito', 152), ('Esmeraldas', 180), ('Manta', 245), ('Guayaquil', 282)],
    'Esmeraldas': [('SantoDomingo', 180)],
    'Manta': [('SantoDomingo', 245), ('Guayaquil', 195)],
    'Guayaquil': [('SantoDomingo', 282), ('Ambato', 276), ('Cuenca', 196), ('Machala', 183), ('Manta', 195)],
    'Ambato': [('Quito', 151), ('Macas', 214), ('Guayaquil', 276), ('Cuenca', 308)],
    'Tena': [('Quito', 192), ('Macas', 204)],
    'Macas': [('Tena', 204), ('Ambato', 214)],
    'Cuenca': [('Ambato', 308), ('Loja', 212), ('Machala', 169), ('Guayaquil', 196)],
    'Loja': [('Cuenca', 212), ('Machala', 237)],
    'Machala': [('Guayaquil', 183), ('Cuenca', 169), ('Loja',237)]
}

grafoPrecios = {
    'Tulcan': [('Ibarra', 25)],
    'Ibarra': [('Tulcan', 25), ('Quito', 20)],
    'Quito': [('Ibarra', 20), ('SantoDomingo', 15), ('Ambato', 35), ('Tena', 27)],
    'SantoDomingo': [('Quito', 15), ('Esmeraldas', 10), ('Manta', 19), ('Guayaquil', 18)],
    'Esmeraldas': [('SantoDomingo', 10)],
    'Manta': [('SantoDomingo', 19), ('Guayaquil', 27)],
    'Guayaquil': [('SantoDomingo', 18), ('Ambato', 14), ('Cuenca', 26), ('Machala', 40), ('Manta', 27)],
    'Ambato': [('Quito', 35), ('Macas', 21), ('Guayaquil', 14), ('Cuenca', 13)],
    'Tena': [('Quito', 27), ('Macas', 12)],
    'Macas': [('Tena', 12), ('Ambato', 21)],
    'Cuenca': [('Ambato', 13), ('Loja', 16), ('Machala', 11), ('Guayaquil', 26)],
    'Loja': [('Cuenca', 16), ('Machala', 41)],
    'Machala': [('Guayaquil', 40), ('Cuenca', 11), ('Loja',41)]
}

# Distancias entre ciudades (en km):
# Tulcán - Ibarra: 126 km
# Ibarra - Quito: 113 km
# Quito - Santo Domingo (por Tandapi, Alluriquín): 152 km
# Quito - Ambato: 151 km
# Quito - Tena: 192 km

# Santo Domingo - Esmeraldas: 180 km
# Santo Domingo - Manta: 245 km
# Santo Domingo - Guayaquil (por Babahoyo): 282 km

# Manta - Guayaquil: 195 km

# Guayaquil - Ambato (por Guaranda): 276 km
# Guayaquil - Cuenca (por El Cajas): 196 km
# Guayaquil - Machala: 183 km
# Guayaquil - Manta: 195 km

# Ambato - Macas (por Riobamba): 214 km
# Ambato - Cuenca: 308 km

# Macas - Tena: 204 km

# Cuenca - Loja: 212 km
# Cuenca - Machala: 169 km

# Loja - Machala: 237 km
