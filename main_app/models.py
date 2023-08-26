from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PURPOSES = (
  ('H', 'House Sharing'),
  ('R', 'Room Sharing'),
  ('E', 'Entire property'),
)

# Create your models here.
class Amenity(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('amenities_detail', kwargs={'pk': self.id})



class Property(models.Model):
  title = models.CharField(max_length=50)
  address = models.TextField(max_length=200)
  suburb = models.CharField(max_length=50)
  state = models.CharField(max_length=3)
  postcode = models.IntegerField()
  details = models.TextField(max_length=200)
  price = models.IntegerField()
  amenities = models.ManyToManyField(Amenity)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return f'{self.title} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'property_id': self.id})
  
class Renting(models.Model):
    available_date = models.DateField('availability Date')
    purpose = models.CharField(
      max_length=1,
      choices=PURPOSES,
      default=PURPOSES[0][0]
      )
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_purpose_display()} on {self.available_date}"
    
    
    class Meta:
     ordering = ['-available_date']
     
     
     
class Photo(models.Model):
  url = models.CharField(max_length=200)
  property = models.ForeignKey(Property, on_delete=models.CASCADE)

  def __str__(self):
        return f"Photo for property_id: {self.property_id} @{self.url}"