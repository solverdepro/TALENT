from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm,CommentForm
from .models import Video,Comment
from django.http import HttpResponseRedirect


# View to upload a video
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after upload
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

# View to show success message after video upload
def upload_success(request):
    # Notify user that video is waiting for admin approval
    return render(request, 'upload_success.html', {
        'message': 'Your video has been uploaded and is awaiting admin approval.'
    })

# View to display approved videos
def video_list(request):
    # Only display videos that have been approved by the admin
    videos = Video.objects.filter(is_approved=True)
    return render(request, 'vid.html', {'videos': videos})


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = video.comments.all()  # Get all comments for this video

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user  # Assume the user is logged in
            comment.save()
            return redirect('video_detail', video_id=video_id)  # Reload the page after posting the comment
    else:
        form = CommentForm()

    return render(request, 'video_detail.html', {
        'video': video,
        'comments': comments,
        'form': form
    })


def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.likes += 1
    video.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))