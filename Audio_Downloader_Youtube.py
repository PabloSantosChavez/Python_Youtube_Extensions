from pytube import YouTube

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'  # Reemplaza con la URL del video que deseas descargar

# Crear una instancia de YouTube
yt = YouTube(url)

# Mostrar información del video
print(f'Título: {yt.title}')
print(f'Duración: {yt.length} segundos')

# Seleccionar el stream de audio
audio = yt.streams.filter(only_audio=True).first()

# Reemplazar caracteres no permitidos en nombres de archivos
audio_title = "".join([c if c.isalnum() or c in (' ', '.', '_') else '_' for c in yt.title])

# Descargar el audio
audio.download(output_path='.', filename=f'{audio_title}.mp3')

print('Descarga de audio completada')
