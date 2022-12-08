from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def show_list_student(request):
    search = request.GET.get('search', None)
    order_by = request.GET.get('order_by', None)
    page = request.GET.get('page', 1)
    student_list = Student.objects.all()
    if search:
        student_list = student_list.filter(Q(name__contains=search))
    if order_by == "age":
        student_list = student_list.order_by("age")
    paginator = Paginator(student_list, 3)
    page_object = paginator.page(page)
    return render(request, 'student.html', {
        "student_list": student_list,
        "page_object": page_object,
        "search": search,

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
