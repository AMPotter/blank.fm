from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponse
from .models import ArticlePost, ArtistProfile, FanProfile, ContributerProfile, ArtistPost
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArtistProfileForm, FanProfileForm, ArticlePostForm, UserForm, ContributerProfileForm, ArtistPostForm

def isContributer(user):
    return user.groups.filter(name='Contributers').exists()

def isArtist(user):
    return user.groups.filter(name='Artists').exists()

def can_post(user):
    return isContributer(user) or isArtist(user)




class ArticleList(LoginRequiredMixin, ListView):
    context_object_name = "article_list"
    queryset = ArticlePost.objects.all().order_by('-timestamp')
    template_name = 'main/home.html'
    login_url = 'login/'



class ArticleDetail(DetailView):
    model = ArticlePost
    template_name = 'main/article_detail.html'

class ArtistPostDetail(DetailView):
    model = ArtistPost
    template_name = 'main/artist_detail.html'


def fan_signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = FanProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            group = Group.objects.get(name='Fans')
            user.groups.add(group)
            user.save()
            location = profile_form.cleaned_data['location']
            age = profile_form.cleaned_data['age']
            bio = profile_form.cleaned_data['bio']
            user = get_object_or_404(User, pk=request.user.pk)
            profile = FanProfile(location=location, age=age, bio=bio, user=user)
            profile.save()

            return redirect('main:home')
    else:
        user_form = UserForm()
        profile_form = FanProfileForm()
    return render(request, 'registration/fansignup.html', {'user_form':user_form, 'profile_form':profile_form})

def artist_signup(request):
    if request.method == 'POST':
        artist_user_form = UserForm(request.POST)
        artist_profile_form = ArtistProfileForm(request.POST)
        if artist_user_form.is_valid() and artist_profile_form.is_valid():
            artist_user_form.save()
            username = artist_user_form.cleaned_data.get('username')
            raw_password = artist_user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            group = Group.objects.get(name='Artists')
            user.groups.add(group)
            user.save()
            location = artist_profile_form.cleaned_data['location']
            age = artist_profile_form.cleaned_data['age']
            genre = artist_profile_form.cleaned_data['genre']
            bio = artist_profile_form.cleaned_data['bio']
            user = get_object_or_404(User, pk=request.user.pk)
            profile = ArtistProfile(location=location, age=age, genre=genre, bio=bio, user=user)
            profile.save()

            return redirect('main:home')
    else:
        artist_user_form = UserForm()
        artist_profile_form = ArtistProfileForm()
    return render(request, 'registration/artistsignup.html', {'artist_user_form':artist_user_form, 'artist_profile_form':artist_profile_form})

@login_required
@user_passes_test(isContributer, 'main:login')
def add_article(request):
    if request.method == 'POST':
        addarticle = ArticlePostForm(request.POST)
        if addarticle.is_valid():
            title = addarticle.cleaned_data['title']
            body = addarticle.cleaned_data['body']
            user = get_object_or_404(User, pk=request.user.pk)
            post = ArticlePost(title=title, body=body, user=user)
            post.save()
            return redirect('main:home')
    else:
        addarticle = ArticlePostForm()
    return render(request, 'main/add_article.html', {'addarticle':addarticle})

@login_required
@user_passes_test(isArtist, 'main:login')
def artist_post(request):
    if request.method == 'POST':
        artistpost = ArtistPostForm(request.POST)
        if artistpost.is_valid():
            title = artistpost.cleaned_data['title']
            body = artistpost.cleaned_data['body']
            user = get_object_or_404(User, pk=request.user.pk)
            post = ArtistPost(title=title, body=body, user=user)
            post.save()
            return redirect('main:profile_redirect')
    else:
        artistpost = ArtistPostForm()
    return render(request, 'main/artist_post.html', {'artistpost':artistpost})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if user.groups.filter(name='Fans').exists():
        profile = get_object_or_404(FanProfile, user=user)
        return render(request, 'main/fan_profile.html', {'fanprofile':profile})
    elif user.groups.filter(name='Artists').exists():
        profile = get_object_or_404(ArtistProfile, user=user)
        artistposts = ArtistPost.objects.filter(user=user)
        return render(request, 'main/artist_profile.html', {'artistprofile':profile, 'artistposts':artistposts})
    elif user.groups.filter(name='Contributers').exists():
        profile = get_object_or_404(ContributerProfile, user=user)
        articleposts = ArticlePost.objects.filter(user=user)
        return render(request, 'main/contributer_profile.html', {'contributerprofile':profile, 'articleposts':articleposts})
    else:
        return redirect('main:login')

@login_required
def profile_redirect(request):
    return redirect('main:profile', username=request.user.username)

@login_required
@user_passes_test(can_post, 'main:login')
def post(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if user.groups.filter(name='Artists').exists():
        return redirect('main:artistpost')
    if user.groups.filter(name='Contributers').exists():
        return redirect('main:addarticle')











# Create your views here.
