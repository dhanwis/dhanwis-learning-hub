from django.shortcuts import render
from admin_app.models import Course

# Create your views here.

def index(request):
    current_page = 'index'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user/index.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user/about.html', context)

def courses(request):
    current_page = 'courses'
    courses = Course.objects.all()
    context = {
        'current_page': current_page,
        'courses' : courses,
    }
    return render(request, 'user/courses.html', context)

def placements(request):
    current_page = 'placements'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user/placements.html', context)


def careers(request):
    current_page = 'careers'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user/careers.html', context)


def contact(request):
    current_page = 'contact'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user/contact.html', context)
