from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from notes.forms import NotesForm
from notes.models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NotesDeleteView(DeleteView):
     model= Notes
     success_url="/smart/notes"
     template_name= "notes/notes_delete.html"

class NotesCreateView(CreateView):
    model=Notes
    form_class=NotesForm
    success_url="/smart/notes"

    def form_valid(self, form):
       self.object=form.save(commit=False)
       self.object.user= self.request.user
       self.object.save()
       return HttpResponseRedirect(self.get_success_url())
    


class NotesUpdateView(UpdateView):
      model=Notes
      form_class=NotesForm
      success_url="/smart/notes"

class NotesListView(LoginRequiredMixin, ListView):
    model=Notes
    context_object_name="notes"
    login_url="/admin"

    def get_queryset(self):
         return self.request.user.notes.all()



class NOtesDetailView(DetailView):
    model= Notes
    context_object_name="note"
