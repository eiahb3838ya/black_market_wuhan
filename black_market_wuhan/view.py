from django.shortcuts import render


def hello(request):
    content = {'hello': 'hello world!'}
    return render(request, 'main_view.html', content)
