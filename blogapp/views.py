from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy,reverse
from  .models import Post,Comment,Like
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class HomeView(ListView):
    model = Post
    template_name= 'home.html'


class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


def LikePost(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created = Like.objects.get_or_create(user - user,post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        Like.save()

        return redirect("post:post-list")



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign.html'















