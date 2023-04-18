from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Experience, Education
from .forms import EducationForm, ExperienceForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile_index(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'main_app/profile_index.html', {'profile': profile})

def profile_info(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    experience_form = ExperienceForm()
    education_form = EducationForm()
    return render(request, 'main_app/profile_info.html', {
        'profile': profile,
        'experience_form': experience_form,
        'education_form': education_form
    })

def add_education(request, profile_id):
    form = EducationForm(request.POST)
    if form.is_valid():
        new_education = form.save(commit=False)
        new_education.profile_id = profile_id
        new_education.save()
    return redirect('profile_info', profile_id=profile_id)

def add_experience(request, profile_id):
    form = ExperienceForm(request.POST)
    if form.is_valid():
        new_experience = form.save(commit=False)
        new_experience.profile_id = profile_id
        new_experience.save()
    return redirect('profile_info', profile_id=profile_id)

def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_index')
        else:
            error = 'Invalid Sign In'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error
    })

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'about_me', 'current_position']
    template_name = 'main_app/profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'main_app/profile_confirm_delete.html'
    success_url = '/profile/'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'about_me', 'current_position']
    template_name = 'main_app/profile_form.html'


