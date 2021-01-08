from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogPostForm,CommentsForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import BlogPost,Comments
# Create your views here.
LogInUrl = '/login/'

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = BlogPost

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = LogInUrl
    redirect_field_name = 'BlogApp/post_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = LogInUrl
    redirect_field_name = 'BlogApp/post_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post_list')

class PostDraftListView(LoginRequiredMixin,ListView):
    login_url = LogInUrl
    redirect_field_name = 'BlogApp/post_list.html'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

@login_required
def publish_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)


def add_comment_to_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentsForm() 
    return render(request,'BlogApp/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail',comment.Post.pk)

@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.Post.pk
    comment.delete()
    return redirect('post_detail',post_pk)






















