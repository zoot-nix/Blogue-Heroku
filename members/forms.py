from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.forms.fields import CharField
from blogueApp.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

class EditBioForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('bio', 'headline', 'profile_picture', 'instagram_url', 'facebook_url', 'website_url', 'github_url', 'linkedin_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'headline': forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'github_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control'}),
        }


class CreateBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'headline', 'profile_picture', 'instagram_url', 'facebook_url', 'website_url', 'github_url', 'linkedin_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'headline': forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'github_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control'}),
        }
