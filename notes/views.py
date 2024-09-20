from django.shortcuts import render
from notes.models import Notes
from django.http import Http404
from django.views.generic import ListView,DetailView
# Create your views here.

class NotesListView(ListView):
    model=Notes
    context_object_name="notes"



class NOtesDetailView(DetailView):
    model= Notes
    context_object_name="note"
