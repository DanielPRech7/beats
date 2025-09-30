from django.db import models

# Modelo para a música
class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    # Aqui vamos armazenar apenas o ID do vídeo (a parte curta no final do link)
    youtube_id = models.CharField(max_length=11, unique=True) 

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

# Modelo para a Playlist (se você já tiver, ignore)
# Relacionamento ManyToMany para adicionar várias músicas a uma playlist
class Playlist(models.Model):
    nome = models.CharField(max_length=200)
    musicas = models.ManyToManyField(Musica, related_name='playlists')

    def __str__(self):
        return self.nome