from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile_index'),
    # crud
    path('profile/create/', views.ProfileCreate.as_view(), name='create_profile'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='delete_profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='update_profile'),
]