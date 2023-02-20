from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    # on delete argument is CASCADE, if a user is deleted then the profile will be deleted as well. But not vice versa 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def __str__(self): 
        return f'{self.user.username} Profile'    
    
    def save(self,*args, **kwargs): 
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300: 
            output_size=(300,300)
            img.thumbnail(output_size) # resize the image so that it can fit in the 300x300 image field
            img.save(self.image.path)   # save the new resized image in the same directory