# beats/playlist/urls.py (Modifique este arquivo)

from django.urls import path
# Importe a nova view
from .views import PlaylistListView, PlaylistDetailView, PlaylistCreateView, PlaylistAddMusicaView 

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist_list'),
    
    # Rota para ver os detalhes
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'), 
    
    # NOVA ROTA: Rota para processar a adição de música
    path('<int:pk>/adicionar-musica/', PlaylistAddMusicaView.as_view(), name='adicionar_musica_playlist'),
    
    path('criar/', PlaylistCreateView.as_view(), name='criar_playlist'), 
]