from pytube import YouTube

# URL del video de YouTube
url = ''  # Reemplaza con la URL del video que deseas descargar

# Crear una instancia de YouTube
yt = YouTube(url)

# Mostrar información del video
print(f'Título: {yt.title}')
print(f'Duración: {yt.length} segundos')

# Seleccionar la mejor resolución de video disponible
video = yt.streams.get_highest_resolution()

# Reemplazar caracteres no permitidos en nombres de archivos
video_title = "".join([c if c.isalnum() or c in (' ', '.', '_') else '_' for c in yt.title])

# Descargar el video
video.download(output_path='.', filename=f'{video_title}.mp4')

print('Descarga completada')
