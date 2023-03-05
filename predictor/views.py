from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')


def predict(request):
    path="/home/bishal/bishal/major_project/classificationSystem/babyCryClassificationSystem/predictor/uploaded_file"
    audio = request.POST['audio']
    with open(path.join(audio), 'wb+') as destination:
        for chunk in audio_file.chunks():
            destination.write(chunk)
    return render(request,'result.html')