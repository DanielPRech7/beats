from django.contrib import admin
from .models import Musica, Playlist

# Registra o modelo Musica para que apareça no Admin
@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'youtube_id')
    search_fields = ('titulo', 'artista')

# Registra o modelo Playlist
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    # Isso permite que você adicione as Músicas (ManyToMany) diretamente no Admin da Playlist
    filter_horizontal = ('musicas',)