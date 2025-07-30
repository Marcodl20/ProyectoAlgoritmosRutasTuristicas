grafo = {
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
    'Machala': [('Guayaquil', 183), ('Cuenca', 169), ('Loja', 237)]
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
