from django.forms import ModelForm
from .models import Experience, Education

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'years', 'Career', 'about']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'about', 'skills']
