from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin  # UserPassesTestMixin qe vetem autori i postit mund ta editoje


# LoginRequiredMixin si login_required dekorator por per class views

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html -> e kerkon template ne kete format
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html -> e kerkon template ne kete format
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  #merr username nga vete url
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):  # kur e bojm class based kerkon ket template: <app>/<model>_<viewtype>.html dhe
    # konteksin e qujm object
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # e setton autorin per userin aktual
        return super().form_valid(form)  # e validon formen


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'  # i bo redirect ne home pasi fshin nje post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def home(request):
    return render(request, 'blog/home.html', {"posts": Post.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})

# posts = [
#     {
#         "author": "Endi",
#         "title": "blog post",
#         "content": "first post content",
#         "date": "June 21 2022",
#     },
#     {
#         "author": "Sefa",
#         "title": "blog post",
#         "content": "second post content",
#         "date": "June 22 2022",
#     }
# ]
