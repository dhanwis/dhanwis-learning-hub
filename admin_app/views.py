from django.shortcuts import render, redirect
from admin_app.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/auth/admin/login/')
def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/dashboard.html', context)

@login_required(login_url='/auth/admin/login/')
def course_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        duraction = request.POST.get('duraction')
        
        course = Course(
            image=image,  
            heading=heading,
            description=description,
            duraction=duraction,
        )
        course.save()
        return redirect('course-list')
    else:
        return render(request, 'admin_app/course-add.html')

@login_required(login_url='/auth/admin/login/')
def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'admin_app/course-list.html', context)

@login_required(login_url='/auth/admin/login/')
def course_edit(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return render(request, 'admin_app/page-not-found.html') 

    if request.method == 'POST':
        new_image = request.FILES.get('image')
        if new_image:
            course.image = new_image
        else:
            new_image = course.image
        course.heading = request.POST.get('heading')
        course.description = request.POST.get('description')
        course.duraction = request.POST.get('duraction')
        course.save()
        return redirect('course-list')

    context = {
        'course': course
    }

    return render(request, 'admin_app/course-edit.html', context)

@login_required(login_url='/auth/admin/login/')
def course_delete(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return render(request, 'admin_app/page-not-found.html')  

    course.delete()
    return redirect('course-list')


        
        