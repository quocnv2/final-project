from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def show_list_student(request):
    student_list = Student.objects.all()
    return render(request, 'student.html', {
        "student_list": student_list,
    })


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_list_student")
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {
        'form': form,
    })


def student_edit(request, id):
    student_list = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student_list)
        if form.is_valid():
            form.save()
            return redirect("show_list_student")
    else:
        form = StudentForm(instance=student_list)

    return render(request, 'student_edit.html', {
        'student_list': student_list,
        'form': form,
    })


def student_delete(request, id):
    student_list = Student.objects.get(id=id)
    if request.method == "POST":
        student_list.delete()
        return redirect("show_list_student")

    return render(request, 'student_delete.html', {
        'student_list': student_list,
    })
