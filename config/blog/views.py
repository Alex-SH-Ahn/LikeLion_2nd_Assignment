from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def create(request):
    if request.method =='POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']
        # new_blog.created_at = request.POST['created_at']
        new_blog.save()
        return redirect('detail', blog_id=new_blog.id)
    return render(request, 'create.html')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def test_page(request):
    return render(request, 'test_page.html')

