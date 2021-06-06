from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from student.models import student
from django.urls import reverse_lazy

class studentListView(ListView):
    model=student

class studentDetailView(DetailView):
    model=student

class studentCreateView(CreateView):
 model = student
 fields = ('name','mail','mobilenumber')

class studentUpdateView(UpdateView):
   model=student
   fields=('name','mobilenumber')


class studentDeleteView(DeleteView):
   model=student
   success_url=reverse_lazy('home')
