from django.forms import ModelForm
from .models import Renting

class RentingForm(ModelForm):
  class Meta:
    model = Renting
    fields = ['available_date', 'purpose']