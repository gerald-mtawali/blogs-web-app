from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post 
"""
    dummy_posts = [
        {
            'author': 'JeradiM',
            'title': 'First Blog Post',
            'content': 'This is the first post written by the council',
            'date_posted': "2023-01-29 14:44:57"
        },

        {
            'author': 'JeradiM',
            'title': 'Second Blog Post',
            'content': 'This is the second post written by the council',
            'date_posted': "2023-01-29 14:45:43"
        },
    ]
"""

def home(request):
    # query the post data over here
    context = {
        'posts': Post.objects.all(),
    }
    
    return render(request, 'blogs/home.html', context, content_type='text/html')


def about(request):
    # return HttpResponse("<h1> About Blogs </h1>")
    return render(request, 'blogs/about.html', {'title': 'Web App About'},content_type='text/html')
