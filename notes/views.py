from django.shortcuts import render

from notes.models import Notes
from django.http import Http404
# Create your views here.

def notes_list(request):
    notes_all= Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':notes_all})


def detail(request, pk):
    try:
       note= Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404 ("this pk does not exists")
    return render(request, 'notes/notes_detail.html', {'note':note})