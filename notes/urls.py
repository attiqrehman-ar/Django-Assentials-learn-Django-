
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('notes', views.NotesListView.as_view(), name="notes.list"),
   path('notes/<int:pk>', views.NOtesDetailView.as_view(), name="note.detail"),
   path("notes/new", views.NotesCreateView.as_view(), name='notes.new'),
   path("notes/<int:pk>/edit", views.NotesUpdateView.as_view(), name='notes.update')
]
