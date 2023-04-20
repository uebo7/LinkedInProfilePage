from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Experience, Education
from .forms import EducationForm, ExperienceForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile_index(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'main_app/profile_index.html', {
        'profile': profile,
    })

@login_required
def profile_info(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    experiences = Experience.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    return render(request, 'main_app/profile_info.html', {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
    })

@login_required
def education_info(request, education_id):
    education = Education.objects.get(id=education_id)
    return render(request, 'Education/education_info.html', {
        'education': education,
    })

@login_required
def experience_info(request, experience_id):
    experience = Experience.objects.get(id=experience_id)
    return render(request, 'Experience/experience_info.html', {
        'experience': experience,
    })

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
#profile
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
    success_url = '/'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'about_me', 'current_position']
    template_name = 'main_app/profile_form.html'
    success_url = '/profile/'

#Experience
class ExperienceCreate(LoginRequiredMixin, CreateView):
    model = Experience
    fields = ['company', 'years', 'Career', 'about']
    template_name = 'Experience/experience_form.html'

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.kwargs.get('profile_id'))
        form.instance.profile = profile
        return super().form_valid(form)

class ExperienceDelete(LoginRequiredMixin, DeleteView):
    model = Experience
    template_name = 'Experience/experience_confirm_delete.html'
    success_url = '/profile/'

class ExperienceUpdate(LoginRequiredMixin, UpdateView):
    model = Experience
    fields = ['company', 'years', 'Career', 'about']
    template_name = 'Experience/experience_form.html'
    
#Education
class EducationCreate(LoginRequiredMixin, CreateView):
    model = Education
    fields = ['school', 'degree', 'about', 'skills']
    template_name = 'Education/education_form.html'

    def form_valid(self, form):
        print(self.kwargs.get('profile_id'))
        profile = Profile.objects.get(pk=self.kwargs.get('profile_id'))
        form.instance.profile = profile
        return super().form_valid(form)

class EducationDelete(LoginRequiredMixin, DeleteView):
    model = Education
    template_name = 'Education/education_confirm_delete.html'
    success_url = '/profile/'

class EducationUpdate(LoginRequiredMixin, UpdateView):
    model = Education
    fields = ['school', 'degree', 'about', 'skills']
    template_name = 'Education/education_form.html'


