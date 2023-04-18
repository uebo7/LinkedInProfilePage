from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_index, name='profile_index'),
    path('profile/<int:profile_id>/', views.profile_info, name='profile_info'),
    # crud
    path('profile/create/', views.ProfileCreate.as_view(), name='create_profile'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='delete_profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='update_profile'),
    #alt models
    path('profile/<int:profile_id>/add_education/', views.add_education, name='add_education'),
    path('profile/<int:profile_id>/add_experience/', views.add_experience, name='add_experience')
]