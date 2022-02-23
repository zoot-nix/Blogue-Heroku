from django import forms
from django.forms import fields
from .models import Post, Category, Comment, Subscribers

# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []

# for item in choices:
#     choice_list.append(item)

#Newsletter
class ContactForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Here'}),
            # 'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }   


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'article_image','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            # 'author': forms.Select(attrs={'class':'form-select'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'author_id', 'type':'hidden'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class':'form-select'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Main Content'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Main Content'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'username', 'comment')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'hidden', 'value': '','id':'name'}),
            'username': forms.TextInput(attrs={'class':'form-control','type':'hidden','value': '','id':'username'}),
            'comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Comment'}),
        }