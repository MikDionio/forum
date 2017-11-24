from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.context_processors import csrf
from django.template import loader
from django.utils import timezone
from .models import Post, Comment
from .forms import CreateComment

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-post_pubdate')
    template = loader.get_template('forum/forum.html')
    context ={
        'latest_post_list':latest_post_list,
    }
    return HttpResponse(template.render(context,request))

def viewpost(request, post_id):
    if request.method == 'POST':
        comment_form = CreateComment(request.POST)
        if comment_form.is_valid():
            # csrf_token = django.middleware.csrf.get_token(request)
            comment_text = comment_form.cleaned_data['text']
            new_comment = Comment(comment_post_id = post_id, comment_text=comment_text, comment_pubdate=timezone.now(), comment_author = request.user)
            new_comment.save()
            return HttpResponseRedirect(reverse('forum:post', args=post_id))
    else:
        comment_form = CreateComment()
        template = loader.get_template('forum/post.html')
        post = get_object_or_404(Post, pk=post_id)
        comments = Comment.objects.filter(comment_post_id=post_id).order_by('-comment_pubdate')[:10]
        context={
            'post':post,
            'comments':comments,
            'comment_form':comment_form
        }
        return HttpResponse(template.render(context,request))

# def comment(request, post_id):
#     if request.method == 'POST':
#         newcomment =
#     return HttpResponseRedirect(reverse('forum:post', args=post_id))

def create(request):
    template = loader.get_template('forum/create.html')
    context = {

    }
    return HttpResponse(template.render(context,request))
