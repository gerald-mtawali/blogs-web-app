from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    # query the post data over here
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'blogs/home.html', context, content_type='text/html')


def about(request):
    # return HttpResponse("<h1> About Blogs </h1>")
    return render(request, 'blogs/about.html', {'title': 'Web App About'}, content_type='text/html')


""" Class based architecture of views. 
    These views are generated using django's builtin class based views 
"""


class PostListView(ListView):
    """Home page for the Blogs app. 
        Inherits functionality from a ListView. 
        We have configured the parameters of this class to match our existing definitions
    Args:
        ListView (_type_): _description_
    """
    model = Post
    # naming convention is <app-name>/<model>_<viewtype>.html
    template_name = 'blogs/home.html'
    # set the context to match the object we're looking for in the template
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """Home page for the Blogs app. 
        Inherits functionality from a ListView. 
        We have configured the parameters of this class to match our existing definitions
    Args:
        ListView (_type_): _description_
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create post view for the Blogs app. 
        Inherits functionality from a CreateView. 
        The CreateVIew creates a form for us to create posts
    Args:
        ListView (_type_): _description_
    """
    model = Post
    fields = ['title', 'content']
    # post author will now be set to whichever user is making the request

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Create post view for the Blogs app. 
        Inherits functionality from a CreateView. 
        The CreateVIew creates a form for us to create posts
    Args:
        ListView (_type_): _description_
    """
    model = Post
    fields = ['title', 'content']
    # post author will now be set to whichever user is making the request

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView): 
    model=Post
    success_url='/'
    # test to see whether the user is the author
    def test_func(self): 
        post=self.get_object()
        if post.author == self.request.user: 
            return True
        return False