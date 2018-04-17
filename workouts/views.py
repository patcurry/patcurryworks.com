# patcurryworks.com/workouts/views.py
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from workouts.models import Exercise, Set, Session


# Session views
class SessionList(ListView):
    model = Session

    
class SessionDetail(DetailView):
    """The sets will be creatable from this page."""
    model = Session

    
class SessionCreate(CreateView):
    model = Session
    fields = ['title']
    template_name = 'workouts/session_create.html'

    def get_success_url(self):
        return reverse('workouts:SessionDetail', kwargs={'pk': self.object.pk})

    
class SessionUpdate(UpdateView):
    model = Session
    fields = ['title']
    success_url = reverse_lazy('workouts:SessionList')

    
class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('workouts:SessionList')


# Exercise views
class ExerciseList(ListView):
    model = Exercise


class ExerciseDetail(DetailView):
    model = Exercise
    slug_field = 'exercise_slug'


class ExerciseCreate(CreateView):
    model = Exercise
    fields = ['title']
    template_name = 'workouts/exercise_create.html'

    def get_success_url(self):
        return reverse('workouts:ExerciseDetail', kwargs={'slug': self.object.exercise_slug})


class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = ['title']
    slug_field = 'exercise_slug'
    success_url = reverse_lazy('workouts:ExerciseList')

    
class ExerciseDelete(DeleteView):
    model = Exercise
    slug_field = 'exercise_slug'
    success_url = reverse_lazy('workouts:ExerciseList')



# Set views
class SetList(ListView):
    model = Set
