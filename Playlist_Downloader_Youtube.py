from pytube import Playlist

# URL de la playlist de YouTube
playlist_url = ''  # Reemplaza con la URL de tu playlist

# Crear una instancia de Playlist
playlist = Playlist(playlist_url)

# Mostrar el título de la playlist
print(f'Título de la playlist: {playlist.title}')

# Descargar cada video en orden y mantener su nombre original
for i, video in enumerate(playlist.videos, start=1):
    print(f'Descargando video {i} de {len(playlist.video_urls)}: {video.title}')
    # Reemplazar caracteres no permitidos en nombres de archivos
    video_title = "".join([c if c.isalnum() or c in (' ', '.', '_') else '_' for c in video.title])
    video.streams.get_highest_resolution().download(output_path='.', filename=f'{video_title}.mp4')
    print(f'Video {i} descargado y guardado como {video_title}.mp4')

print('Descarga de la playlist completada')
