from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm

# Create your views here.

def getPosts(request):
    template_name = 'postapp/list.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name=template_name, context=context)


def getPost(request, pk):
    template_name = 'postapp/detail.html'
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment =comment_form.save(commit=False)
            comment.post_id = post.id
            comment.save()
    print("Get")
    context = {"post":post, "comment_form":comment_form, "comments":comments}
    return render(request=request, template_name=template_name, context=context)
