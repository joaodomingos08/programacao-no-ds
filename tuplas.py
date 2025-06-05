# Solicita ao usuário que forneça as coordenadas geográficas (latitude e longitude)
coordenadas = input("Digite a latitude e longitude separadas por vírgula: ")
lat, lon = map(float, coordenadas.split(','))

# Exibe as coordenadas extraídas
print(f"Latitude: {lat}")
print(f"Longitude: {lon}")
