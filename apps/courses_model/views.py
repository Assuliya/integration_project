from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from ..login_reg_app.models import User
from django.urls import reverse

def index(request):
    courses = Course.objects.all()
    users = User.objects.all()
    context = {'courses':courses, 'users':users}
    return render(request, 'courses_model/index.html', context)

def delete(request, user_id):
    course = Course.objects.get(id=user_id)
    context = {'course':course}
    return render(request, 'courses_model/destroy.html', context)

def register(request):
    if request.method == "POST":
        print request.POST['user']
        user = User.objects.get(id=request.POST['user'])
        print user
        Course.objects.create(name = request.POST['name'],
 		     description = request.POST['description'], person = user)
        return redirect(reverse('course_index'))
    else:
	    return redirect(reverse('course_index'))

def destroy(request, user_id):
	if request.method == "GET":
 		Course.objects.filter(id = user_id).delete()
		return redirect(reverse('course_index'))
	else:
		return redirect(reverse('course_index'))

def back(request):
    return redirect(reverse('course_index'))
