from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import pandas as pd
import random
import glob
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from django.http import HttpResponse
from django.conf import settings

#model_path = os.path.join(BASE_DIR, 'basic_app/saved_model')
our_model = load_model('basic_app/vgg16_model2.h5')

# Create your views here.
def index(request):

    file_path = settings.MEDIA_ROOT

    if request.method == 'POST':
        #img_new = request.FILES.get()'pic']
        img_new = request.FILES.get('pic')
        if img_new:
            print('success')
        else:
            print('no img')
        print(img_new.name)

        fs = FileSystemStorage(location=file_path)
        filename = fs.save(img_new.name, img_new)
        file_url = fs.url(filename)
        print(file_url)
        img=image.load_img(os.path.join(file_path,img_new.name),target_size=(224,224,3))
        img=image.img_to_array(img)
        resize=np.expand_dims(img,axis=0)
        resize=resize/255.0
        pred = our_model.predict(resize)
        predlist = list(pred)
        print(predlist[0][1])
        score = predlist[0][1]
        if score>=0.5:
            item = 'Handloom'
        else:
            item = 'Powerloom'

        print(type(predlist))

        return render(request, 'basic_app/index.html', {'item':item, 'photo_url':file_url})

    return render(request, 'basic_app/index.html')

def home(request):
    return render(request, 'basic_app/project3.html')

def new_one(request):
    file_path = settings.MEDIA_ROOT

    if request.method == 'POST':
        #img_new = request.FILES.get()'pic']
        img_new = request.FILES.get('pic')
        if img_new:
            print('success')
        else:
            print('no img')
        print(img_new.name)

        fs = FileSystemStorage(location=file_path)
        filename = fs.save(img_new.name, img_new)
        file_url = fs.url(filename)
        print(file_url)
        img=image.load_img(os.path.join(file_path,img_new.name),target_size=(224,224,3))
        img=image.img_to_array(img)
        resize=np.expand_dims(img,axis=0)
        resize=resize/255.0
        pred = our_model.predict(resize)
        predlist = list(pred)
        print(predlist[0][1])
        score = predlist[0][1]
        if score>=0.5:
            item = 'Handloom'
        else:
            item = 'Powerloom'

        print(type(predlist))

        return render(request, 'basic_app/project1.html', {'item':item, 'photo_url':file_url})

    return render(request, 'basic_app/project1.html')
