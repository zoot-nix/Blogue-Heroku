from django.contrib.auth.forms import UserChangeForm
from django.urls import path, include
from django.views.generic.edit import CreateView
from .views import CreateBioView, ShowProfileView, UserEditView, UserRegisterView, PasswordsChangeView, EditBioView

urlpatterns = [ 
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('edit-account/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ShowProfileView.as_view(), name="profile-page"),
    path('<int:pk>/edit-profile', EditBioView.as_view(), name="bio-page"),
    path('create-profile', CreateBioView.as_view(), name="create-profile-page")
    
]
