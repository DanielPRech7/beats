from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404 
from django.views import View 
from django.views.generic import ListView, DetailView, CreateView
from .models import Playlist, Musica
import logging

logger = logging.getLogger(__name__)

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
    context_object_name = 'playlists'

    def get(self, request, *args, **kwargs):
        logger.info("Playlist list view foi acessada.")
        return super().get(request, *args, **kwargs)

#aaaa
class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist/playlist_detail.html'
    context_object_name = 'playlist'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todas_musicas'] = Musica.objects.all().order_by('titulo')
        return context

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['nome']
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list') 

class PlaylistAddMusicaView(View):
    def post(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        musica_id = request.POST.get('musica_id')
        
        if musica_id:
            musica = get_object_or_404(Musica, pk=musica_id)
            playlist.musicas.add(musica)
        return redirect('playlist_detail', pk=playlist.pk)