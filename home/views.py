from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.db import IntegrityError
from .models import UserMessage
from django.conf import settings

from django.contrib import messages
# from datetime import datetime
from home.models import Marks   
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'home/index.html')   # ✅ must return something


# def login(request):
#     # 🔒 Prevent logged-in users from going back to login page
#     if request.user.is_authenticated:
#         return redirect('home')   # replace 'home' with your homepage route name

#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # ⚠️ Default Django authenticate() expects `username` unless you've set up a custom user model
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             auth_login(request, user)  # login user
#             return redirect('home')
#         else:
#             return render(request, 'home/login.html', {"error": "Invalid credentials"})

#     # ✅ Handle GET request (show login page)
#     return render(request, 'home/login.html')

from .utils import send_otp, verify_otp

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         otp = request.POST.get('otp')

#         user = authenticate(request, username=email, password=password)

#         # Case 1: Password login successful
#         if user is not None:
#             auth_login(request, user)
#             return redirect('home')

#         # Case 2: OTP login
#         elif phone and otp and verify_otp(phone, otp):
#             try:
#                 user = User.objects.get(username=email)
#                 auth_login(request, user)
#                 return redirect('home')
#             except User.DoesNotExist:
#                 return render(request, "home/login.html", {"error": "User not found for this phone"})
        
#         # Case 3: Send OTP if only phone entered
#         elif phone and not otp:
#             send_otp(phone)
#             return render(request, "home/login.html", {"phone": phone, "info": "OTP sent to your number"})

#         else:
#             return render(request, "home/login.html", {"error": "Invalid credentials or OTP"})

#     return render(request, 'home/login.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from .utils import send_otp, verify_otp

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        otp = request.POST.get("otp")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, "home/login.html", {"error": "User not found"})

        # 1️⃣ Check password first
        if password:
            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                auth_login(request, user_auth)
                return redirect("home")

        # 2️⃣ If no password, check OTP from session
        if otp:
            saved_otp = request.session.get("otp")
            if saved_otp and otp == saved_otp:
                auth_login(request, user)
                # clear OTP after login
                del request.session["otp"]
                return redirect("home")

        return render(request, "home/login.html", {"error": "Invalid credentials or OTP"})

    return render(request, "home/login.html")


def logout(request):
    auth_logout(request)   # ✅ avoid recursion
    return redirect('login')


def upload(request):
    return render(request, 'home/upload.html')


def services(request):
    return render(request, 'home/services.html')

def home(request):
        return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        maths_10 = request.POST.get('maths_10')
        science_10 = request.POST.get('science_10')
        english_10 = request.POST.get('english_10')
        social_science_10 = request.POST.get('social_science_10')
        hindi_10 = request.POST.get('hindi_10')
        pe_10 = request.POST.get('pe_10')
        total_10 = request.POST.get('total_10')
        maths_12 = request.POST.get('maths_12')
        physics_12 = request.POST.get('physics_12')
        chemistry_12 = request.POST.get('chemistry_12')
        english_12 = request.POST.get('english_12')
        pe_12 = request.POST.get('pe_12')
        total_12 = request.POST.get('total_12')

        # ✅ Step 1: Check if any field is empty
        fields = [name, email, maths_10, science_10, english_10, social_science_10, hindi_10, pe_10,
                  total_10, maths_12, physics_12, chemistry_12, english_12, pe_12, total_12]

        if any(f is None or f.strip() == "" for f in fields):
            messages.error(request, "⚠️ Please fill all fields before submitting.")
            return render(request, 'home/contact.html')

        # ✅ Step 2: Validate marks range (only subjects, not totals)
        subject_fields = [maths_10, science_10, english_10, social_science_10, hindi_10, pe_10,
                          maths_12, physics_12, chemistry_12, english_12, pe_12]

        try:
            subject_marks = list(map(int, subject_fields))
            if not all(0 <= m <= 100 for m in subject_marks):
                messages.error(request, "⚠️ Marks must be between 0 and 100.")
                return render(request, 'home/contact.html')

            total_10 = int(total_10)
            total_12 = int(total_12)

        except ValueError:
            messages.error(request, "⚠️ Please enter valid numbers only.")
            return render(request, 'home/contact.html')

        # ✅ Step 3: Save if everything is valid
        marks = Marks(
            name=name,
            email=email,
            maths_10=subject_marks[0],
            science_10=subject_marks[1],
            english_10=subject_marks[2],
            social_science_10=subject_marks[3],
            hindi_10=subject_marks[4],
            pe_10=subject_marks[5],
            total_10=total_10,
            maths_12=subject_marks[6],
            physics_12=subject_marks[7],
            chemistry_12=subject_marks[8],
            english_12=subject_marks[9],
            pe_12=subject_marks[10],
            total_12=total_12
        )

        try:
            marks.save()
            messages.success(request, "✅ Marks uploaded successfully!")
        except IntegrityError:
            messages.error(request, "⚠️ Email already exists. Please use a different one.")

    return render(request, 'home/contact.html')


def services(request):
    if request.user.is_authenticated:
        user_messages = UserMessage.objects.filter(user=request.user).order_by('-created_at')
    else:
        user_messages = []
    
    return render(request, 'home/services.html', {"messages": user_messages})

# uploading a receipt 
from .forms import FeeReceiptForm
def upload_receipt(request):
    if request.method == 'POST':
        form = FeeReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_receipt')  # reload the page after saving
    else:
        form = FeeReceiptForm()

    return render(request, 'home/upload_receipt.html', {'form': form})


# def upload_receipt(request):
#     if request.method == 'POST':
#         form = FeeReceiptForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_receipt')  # reload page after success
#     else:
#         form = FeeReceiptForm()
#     return render(request, 'home/upload_receipt.html', {'form': form})


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            return render(request, "home/register.html", {"error": "⚠️ Email already exists"})

        # ✅ Create new user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()

        # Auto login after register (optional)
        auth_login(request, user)
        return redirect("home")

    return render(request, "home/register.html")


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# @csrf_exempt
# def send_otp_view(request):
#     if request.method == "POST":
#         phone = request.POST.get("phone")
#         if not phone:
#             return JsonResponse({"error": "Phone number required"}, status=400)

#         otp = send_otp(phone)  # your utils.py function
#         return JsonResponse({"success": True, "message": f"OTP sent to {phone}"})

#     return JsonResponse({"error": "Invalid request"}, status=400)

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from twilio.rest import Client
import random

User = get_user_model()

# Store OTP temporarily in session (for testing)
def send_otp(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        if not phone:
            return JsonResponse({"success": False, "message": "Phone number is required"})

        # ✅ Generate OTP
        otp = str(random.randint(1000, 9999))

        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            client.messages.create(
                body=f"Your login OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,   # 👈 Your Twilio phone number
                to=phone              # 👈 Must include +91 or country code
            )

            # Optionally save OTP to session (or DB)
            request.session["otp"] = otp
            return JsonResponse({"success": True, "message": "OTP sent successfully"})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request"})

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")   # ✅ used for OTP only
        password = request.POST.get("password")

        # username = email
        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists with this email.")
            return redirect("/register")

        # ✅ Create User
        user = User.objects.create(
            username=email, 
            email=email,
            first_name=name,
            password=make_password(password)  # hash password
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("/login")

    return render(request, "register.html")

