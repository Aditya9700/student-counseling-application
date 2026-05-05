# home/utils.py
from twilio.rest import Client
import random
from django.conf import settings

# Temporary OTP storage
otp_store = {}

def send_otp(phone):
    otp = str(random.randint(100000, 999999))
    otp_store[phone] = otp

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your OTP for login is: {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )
    return otp

def verify_otp(phone, otp):
    return otp_store.get(phone) == otp
# # utils.py (create in your app folder)

# import random
# from twilio.rest import Client
# from django.conf import settings

# otp_storage = {}  # simple in-memory store (use cache/db in production)

# def send_otp(phone):
#     otp = str(random.randint(100000, 999999))
#     otp_storage[phone] = otp  # store OTP for verification
    
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         body=f"Your OTP for login is {otp}",
#         from_=settings.TWILIO_PHONE_NUMBER,
#         to=phone
#     )
#     return otp

# def verify_otp(phone, otp):
#     valid = otp_storage.get(phone) == otp
#     if valid:
#         otp_storage.pop(phone)  # remove after successful verification
#     return valid
