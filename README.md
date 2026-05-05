# Students Counseling Web Application

## Overview
This project is a full-stack web application built using Django that allows students to submit academic details, view rankings, receive messages from administrators, and upload documents. It also includes a custom-built admin panel for managing users, messages, and student data.

The system integrates OTP-based authentication using Twilio along with traditional password-based login, providing flexibility in user authentication.

---

## Features

### Student Functionality
- User registration and authentication using Django's built-in User model
- Login using either password or OTP (via Twilio)
- Submission of Class 10 and Class 12 marks
- Viewing ranking based on academic performance
- Receiving messages from administrators (with optional image attachments)
- Uploading fee receipts and supporting documents
- Access to a personalized dashboard

### Admin Functionality (Custom Admin Panel)
- Dashboard displaying:
  - Total number of users
  - Total messages sent
  - Total uploaded receipts
  - Student ranking table
- Manage users
- Send messages to users (with optional image attachments)
- View uploaded receipts
- Rank students based on Class 12 marks and combined total

---

## Technology Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default, can be replaced with PostgreSQL/MySQL)
- Authentication: Django Authentication System + Twilio OTP
- Media Handling: Django Media Files

---

## System Architecture

### High-Level Architecture
