from django.urls import path
from .views import upload_video, upload_success, video_list, video_detail, like_video

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('success/', upload_success, name='success'),
    path('list/', video_list, name='video_list'),
    path('video/<int:video_id>/', video_detail, name='video_detail'),  # Video detail page with comments
    path('video/<int:video_id>/like/', like_video, name='like_video'),
]
