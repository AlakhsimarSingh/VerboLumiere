from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UploadedVideo
from .forms import VideoUploadForm, CustomLoginForm, RegisterForm
from .utils.pipeline import process_input_basic

# Create your views here.
def register_user(request):
    form = None
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
        else:
            form = RegisterForm()
    return render(request, 'processor/register.html', {'form':form})
def login_view(request):
    form = None
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
        else:
            form = CustomLoginForm()
    return render(request, 'processor/login.html',{'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    videos = UploadedVideo.objects.filter(user=request.user)
    return render(request, 'processor/dashboard.html',{'videos':videos})

@login_required
def upload_video(request):
    form = None
    if request.method =='POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()

            result = process_input_basic(video.original_video.path, input_type="video")
            video.translated_audio.name = result['translated_audio_path']
            video.translated_video.name = result['subtitle_video_path']
            video.transcript = result['transcript']

            video.save()
            return redirect('dashboard')
        else:
            form = VideoUploadForm()
    return render(request, 'processor/upload.html', {'form':form})
    
@login_required
def delete_video(request, video_id):
    video = UploadedVideo.objects.get(id=video_id, user=request.user)
    video.delete()
    return redirect('dashboard')

@login_required
def view_translation(request, video_id):
    video = get_object_or_404(UploadedVideo, id=video_id, user=request.user)

    context = {
        'video': video,
    }
    return render(request, 'processor/view_translation.html', context)
