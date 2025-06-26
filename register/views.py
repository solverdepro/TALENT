from django.shortcuts import render, redirect
from .form import MediaUploadedForm

# Create your views here.
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MediaUploadedForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'success.html')









def home(request):
    return render(request, 'home.html')
