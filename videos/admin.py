from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_approved')  # Show approval status in the admin panel
    list_filter = ('is_approved',)           # Filter videos based on approval status
    search_fields = ('title',)

admin.site.register(Video, VideoAdmin)
