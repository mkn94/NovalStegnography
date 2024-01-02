from django.db import models
class UserAccount(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,default='user',blank=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=50,blank=True)
    mobile=models.CharField(max_length=50)
    email=models.EmailField(default='')
    status=models.IntegerField(default=0,blank=True)
    class Meta:
        db_table="useraccount"


# class HiddenImage(models.Model):
#     image = models.ImageField(upload_to='hidden_images/')
#     text = models.CharField(max_length=5555)
#     encrypted_image_path = models.CharField(max_length=255, blank=True, null=True)
#     num_encrypted_images = models.PositiveIntegerField(default=0)
#     class Meta:
#         db_table="hiddenimage"

from django.db import models

from django.db import models

class HiddenImage(models.Model):
  image = models.FileField()
  encrypted_text = models.BinaryField()
  aes_key = models.BinaryField()

   