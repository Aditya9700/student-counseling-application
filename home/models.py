from django.db import models

# Create your models here.
from django.contrib.auth.models import User   # using Django's User model

class Marks(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20, unique=True)
    maths_10 = models.IntegerField()
    science_10 = models.IntegerField()
    english_10 = models.IntegerField()   
    social_science_10 = models.IntegerField()
    hindi_10 = models.IntegerField()
    pe_10 = models.IntegerField()   # ✅ lowercase, matches form
    total_10 = models.IntegerField()
    maths_12 = models.IntegerField()
    physics_12 = models.IntegerField()              
    chemistry_12 = models.IntegerField()
    english_12 = models.IntegerField()
    pe_12 = models.IntegerField()
    total_12 = models.IntegerField()    
    

    def __str__(self):
        return f"{self.name} - {self.email} {self.total_10} - {self.total_12}"
    
class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    subject = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="message_images/", blank=True, null=True)  # 🆕 allow image upload
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"To {self.user.username}: {self.subject}"

# Upload receipt model

# class FeeReceipt(models.Model):
#     student_name = models.CharField(max_length=100)  # Optional: auto-link to user later
#     message = models.TextField(blank=True, null=True)
#     receipt_image = models.ImageField(upload_to='fee_receipts/')  # image will be stored in /media/fee_receipts/
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student_name} - {self.uploaded_at.strftime('%Y-%m-%d')}"
class FeeReceipt(models.Model):
    student_name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    receipt_image = models.ImageField(upload_to='receipts/')   # uploaded to MEDIA_ROOT/receipts/

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

