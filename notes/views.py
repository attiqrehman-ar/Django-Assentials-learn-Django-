from django.shortcuts import render
from notes.forms import NotesForm
from notes.models import Notes
from django.http import Http404
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.


class NotesDeleteView(DeleteView):
     model= Notes
     success_url="/smart/notes"
     template_name= "notes/notes_delete.html"

class NotesCreateView(CreateView):
    model=Notes
    form_class=NotesForm
    success_url="/smart/notes"


class NotesUpdateView(UpdateView):
      model=Notes
      form_class=NotesForm
      success_url="/smart/notes"

class NotesListView(ListView):
    model=Notes
    context_object_name="notes"



class NOtesDetailView(DetailView):
    model= Notes
    context_object_name="note"
