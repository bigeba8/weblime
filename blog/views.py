from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post

# Create your views here.

def profile_home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'user': request.user
    }
    return render(request, 'blog/profile_home.html', context)

def user_posts(request):
    context = {
        'posts': Post.objects.filter(author=request.user).order_by('-date_posted')
    }
    return render(request, 'blog/user_posts.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/profile_home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({ 'seo_title': self.get_object().title, 'seo_description': self.get_object().excerpt })
        return context

class PostDetailViewUser(DetailView):
    model = Post
    template_name = 'blog/post_detail_user.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'cover_image', 'content', 'excerpt']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'cover_image', 'content', 'excerpt']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/profile'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
