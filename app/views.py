from email import message
from django.shortcuts import render, redirect
from django.views import generic
from requests import request
from django.contrib.auth.decorators import login_required
from user.models import Profile
from .models import PostList, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from sendgrid import SendGridAPIClient
from decouple import config
from sendgrid.helpers.mail import Mail, From, To, PlainTextContent, HtmlContent


class PostView(generic.ListView):
    context_object_name = 'PostList'
    template_name = 'app/index.html'

    def get_queryset(self):
        return PostList.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = PostList
    context_object_name = 'post'
    template_name = 'app/detail.html'



class CreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = PostList
    context_object_name = 'post'
    # success_url = '/'
    success_message = "Post created successfully"
    template_name = 'app/add.html'
    fields = ['title', 'description']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(kwargs)
    #     print(type(self.get_object))
    #     # self.object = kwargs['self.object.pk']
        # self.object.pk = self.kwargs.get(self.pk_url_kwarg)

        

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = PostList
    success_url = '/'
    success_message = "Post deleted successfully"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
    template_name = 'app/delete.html'

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = PostList
    context_object_name = 'post'
    template_name = 'app/edit.html'
    fields = ['title', 'description']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class AddCommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'app/add_comment.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        # form.instance.email = self.request.user.email
        return super().form_valid(form)