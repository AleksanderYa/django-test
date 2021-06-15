from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')

def post_list_two(request):
    return render(request, 'blog/post_list_two.html')