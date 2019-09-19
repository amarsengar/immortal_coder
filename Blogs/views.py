from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Count,Q
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from Blogs.models import Author,Post,PostView
# Create your views here.


def get_author(user):

    Auth= Author.objects.filter(user=user)
    if Auth.exists():
        return Auth[0]
    return None


class IndexView(View):

    def get(self,request,*args,**kwargs):
        featured = Post.objects.filter(featured=True)
        latest = Post.objects.order_by('-timestamp')[0:3]
        context={
            'object_list':featured,
            'latest':latest,
        }
        return render(request,'index.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self,  **kwargs):
        category_count = get_category_count()
