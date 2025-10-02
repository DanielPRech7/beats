from django.db import models

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=11, unique=True) 
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Playlist(models.Model):
    nome = models.CharField(max_length=200)
    musicas = models.ManyToManyField(Musica, related_name='playlists')
    def __str__(self):
        return self.nome