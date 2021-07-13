from django.shortcuts import render


posts = [
    {
        'author': 'Kuba',
        'title': 'post 1',
        'content': 'First post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Monika',
        'title': 'post 2',
        'content': 'Second post',
        'date_posted': 'August 27, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})