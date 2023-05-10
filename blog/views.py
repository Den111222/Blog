from datetime import datetime

from django.contrib import auth
from django.shortcuts import render, redirect
from blog.forms import PostForm, CommentForm
from blog.models import Post, Comments, Category


def post_list(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    return render(request,'blog/post_list.html', {
        'items': posts,
        'category': category,
    })

def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    comments = Comments.objects.filter(post=post)
    counter = comments.count()
    rate=0
    score = 0
    for x in comments:
        score += 1
        rate = (rate + x.rate)
    rate = rate / score

    return render(request, 'blog/post_detail.html', {'post': post,'comments': comments,
                                                     'counter': counter,'rate': rate,
                                                     })

def post_new(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect('post_list')

def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        post = form.save(commit=False)
        post.created_date = datetime.now()
        post.published_date = datetime.now()
        post.save()
        return redirect('post_detail', post_pk=post.id)

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post_list')

def published_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.published_date = datetime.now()
    post.published = True
    post.save()
    return redirect('post_list')

def post_draft(request):
    posts = Post.objects.all()
    return render(request,'blog/post_draft.html', {'items': posts})

def category(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    return render(request, 'blog/post_list.html', {'items': posts,
                                                   'category': category})

def comment_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'blog/comment_post.html', {'form': form})
    else:
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.published_date = datetime.now()
        comment.author = auth.get_user(request)
        comment.save()
        return redirect('post_detail', post_pk=post.id)