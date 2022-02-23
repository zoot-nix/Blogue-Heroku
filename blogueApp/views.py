from ast import Sub
from urllib import request
from blogueApp.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

from .models import Category, Comment, Post, Subscribers
from django.contrib.auth.models import User

from .forms import EditForm, PostForm, CommentForm, ContactForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# userList =User.objects.all()
# for u in userList:
#     print(u)

# def index(request):
#     userList =User.objects.all()
#     return render(request, 'home.html', {'users': userList})

# class UserListView(ListView):
#     model = User
#     template_name = 'home.html'

#Learn Page
def learn(request):
    return render(request, 'learn.html')


#Newsletter
class ContactView(CreateView):
    model = Subscribers
    form_class = ContactForm
    template_name = 'newsletter.html'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)  
        liked = True      
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    

    def get_context_data(self, *args , **kwargs):
        category_nav = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_nav"] = category_nav
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args , **kwargs):
        category_nav = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["category_nav"] = category_nav
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm  
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})



    