from django.shortcuts import render,redirect
from shareapp.forms import UploadFileForm
from .models import Files
from django.utils.crypto import get_random_string
import mimetypes
from django.http import HttpResponse
import os
import pyqrcode
from PIL import Image, ImageTk

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            key = get_random_string(length=32)
            files = Files(key = key ,file = request.FILES['file'])
            files.save()
            url = request.build_absolute_uri()
            s = f"{url}{key}"
            print(s)
            qr = pyqrcode.create(str(s))
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            fl_path = BASE_DIR+'/media/'+key+'.png'
            fl = 'media/'+key+'.png'
            qr.png(fl_path, scale=8)
            return render(request,'sucess.html',{'key':key,'qr':fl_path,'pth':fl})
    else:
        form = UploadFileForm()
    return render(request, 'transfer.html', {'form': form})

def sucess(request):
    return render(request,'sucess.html')

def download_file(request,key):
    # fill these variables with real values
    files = Files.objects.get(key = key)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = str(files.file)
    fl_path = BASE_DIR+'/media/'+filename
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(filename)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
