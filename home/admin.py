
# Register your models here.
from django.contrib import admin
from .models import Marks ,UserMessage

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "email",
        "maths_10", "science_10", "english_10", "social_science_10", "hindi_10", "pe_10", "total_10",
        "maths_12", "physics_12", "chemistry_12", "english_12", "pe_12", "total_12"
    )
    search_fields = ("name", "email")
    list_filter = ("maths_10", "maths_12", "total_10", "total_12")
    list_per_page = 20

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("user__username", "subject", "body")

#file upload model registration
from django.contrib import admin
from .models import FeeReceipt

@admin.register(FeeReceipt)
class FeeReceiptAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'uploaded_at')
    search_fields = ('student_name', 'message')


