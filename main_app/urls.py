from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_index, name='profile_index'),
    path('profile/<int:profile_id>/', views.profile_info, name='profile_info'),
    path('education/<int:education_id>/', views.education_info, name='education_info'),
    path('experience/<int:experience_id>/', views.experience_info, name='experience_info'),
    # Profile crud
    path('profile/create/', views.ProfileCreate.as_view(), name='create_profile'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='delete_profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='update_profile'),
    # Experience crud
    path('profile/<int:profile_id>/experience/create/', views.ExperienceCreate.as_view(), name='create_experience'),
    path('experience/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='delete_experience'),
    path('experience/<int:pk>/update/', views.ExperienceUpdate.as_view(), name='update_experience'),
    # Education crud
    path('profile/<int:profile_id>/education/create/', views.EducationCreate.as_view(), name='create_education'),
    path('education/<int:pk>/delete/', views.EducationDelete.as_view(), name='delete_education'),
    path('education/<int:pk>/update/', views.EducationUpdate.as_view(), name='update_education'),
    
]