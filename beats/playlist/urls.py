from django.urls import path
from .views import PlaylistListView, PlaylistDetailView, PlaylistCreateView, PlaylistAddMusicaView 

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist_list'),
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'), 
    path('<int:pk>/adicionar-musica/', PlaylistAddMusicaView.as_view(), name='adicionar_musica_playlist'),
    path('criar/', PlaylistCreateView.as_view(), name='criar_playlist'), 
]