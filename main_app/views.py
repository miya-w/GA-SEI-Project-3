import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Property, Amenity, Photo
from .forms import RentingForm

import json
from django.conf import settings



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
  
@login_required
def properties_index(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'properties/index.html', {
        'properties': properties
    })
    
@login_required
def properties_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    id_list = property.amenities.all().values_list('id')
    amenities_property_doesnt_have = Amenity.objects.exclude(id__in=id_list)
    renting_form = RentingForm()
    return render(request, 'properties/detail.html', {
        'property':property,
        'renting_form': renting_form,
        'amenities': amenities_property_doesnt_have

    })

class PropertyAdd(CreateView):
    model = Property
    fields = ['title', 'address', 'suburb', 'state', 'postcode', 'details', 'price']
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
    
class PropertyUpdate(UpdateView):
  model = Property
  fields = ['title', 'address', 'suburb', 'state', 'postcode', 'details', 'price']

class PropertyDelete(DeleteView):
  model = Property
  success_url = '/properties'
    

def add_renting(request, property_id):
    form = RentingForm(request.POST)
  # validate the form
    if form.is_valid():
        new_renting = form.save(commit=False)
        new_renting.property_id = property_id
        new_renting.save()
    return redirect('detail', property_id=property_id)

class AmenityList(ListView):
  model = Amenity

class AmenityDetail(DetailView):
  model = Amenity

class AmenityCreate(CreateView):
  model = Amenity
  fields = '__all__'

class AmenityUpdate(UpdateView):
  model = Amenity
  fields = ['name']

class AmenityDelete(DeleteView):
  model = Amenity
  success_url = '/amenities'     

@login_required
def assoc_amenity(request, property_id, amenity_id):
    Property.objects.get(id=property_id).amenities.add(amenity_id)
    return redirect('detail', property_id=property_id)
  
@login_required
def unassoc_amenity(request, property_id, amenity_id):
    Property.objects.get(id=property_id).amenities.remove(amenity_id)
    return redirect('detail', property_id=property_id)
  
@login_required 
def add_photo(request, property_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, property_id=property_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', property_id=property_id)
  

def signup(request):
  error_message = ''
  form = UserCreationForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
