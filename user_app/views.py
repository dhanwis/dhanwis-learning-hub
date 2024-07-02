from django.shortcuts import render
from admin_app.models import Course, Company, Placement, Gallery

# Create your views here.

def index(request):
    current_page = 'index'
    companies = Company.objects.all()
    placements = Placement.objects.all()[:3]  # Fetching first 3 placements as an example
    context = {
        'current_page': current_page,
        'companies': companies,
        'placements': placements
    }
    return render(request, 'user_app/index.html', context)

def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/about.html', context)

def courses(request):
    current_page = 'courses'
    courses = Course.objects.all()
    context = {
        'current_page': current_page,
        'courses' : courses,
    }
    return render(request, 'user_app/courses.html', context)

def placements(request):
    current_page = 'placements'
    placements = Placement.objects.all()
    context = {
        'current_page': current_page,
        'placements' : placements
    }
    return render(request, 'user_app/placements.html', context)


def careers(request):
    current_page = 'careers'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/careers.html', context)


def contact(request):
    current_page = 'contact'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/contact.html', context)


def gallery(request):
    current_page = 'gallery'
    galleries = Gallery.objects.all()
    context = {
        'current_page': current_page,
        'galleries' : galleries
    }
    return render(request, 'user_app/gallery.html', context)