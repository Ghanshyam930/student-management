
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from .models import StudentProfile, StudentDoubt, TeacherProfile

# About Page
def aboutus(request):
    return render(request, "about.html")

# Signup
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        user = User.objects.create(
            first_name=name,
            username=email,
            email=email,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, "signup.html")

# Login
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            request.session['role'] = role

            if role == "student":
                return redirect("student")
            elif role == "teacher":
                return redirect("teacher")
            elif role == "admin":
                return redirect("admin_panel")
            else:
                messages.error(request, "Invalid role selected.")
                return redirect("login")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "login.html")

# Student Dashboard
def student(request):
    student = None
    try:
        student = StudentProfile.objects.get(user=request.user)
    except:
        pass
    return render(request, "student_panel.html", {'student': student, 'user': request.user})

# Teacher Dashboard
def teacher(request):
    teacher = None
    try:
        teacher = TeacherProfile.objects.get(user=request.user)
    except:
        pass
    return render(request, "teacher_panel.html", {'teacher': teacher, 'user': request.user})

# Admin Dashboard
# def admin_panel(request):
#     return render(request, "admin_panel.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Submit Doubt
def submit_doubt(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        doubt = request.POST.get('question')
        student = StudentProfile.objects.get(user=request.user)

        # doubt save karo (abhi subject_assignment None rahega temporary)
        StudentDoubt.objects.create(student=student, subject_assignment=None, doubt_text=doubt)

        messages.success(request, "Doubt submitted successfully!")
        return redirect('student')
    return redirect('student')
