from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # on delete argument is CASCADE, if a user is deleted then the profile will be deleted as well. But not vice versa 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self): 
        return f'{self.user.username} Profile'    
    