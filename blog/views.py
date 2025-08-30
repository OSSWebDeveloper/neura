from django.shortcuts import render, redirect
from .models import Worker


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            worker = Worker.objects.get(name=username, password=password)
            request.session["worker_id"] = worker.id  # Sessiyaga saqlaymiz

            # Redirect by role
            if worker.category == "Teacher":
                return redirect("teacher_home", id=worker.id)

            else:  # Student
                return redirect("student_home")

        except Worker.DoesNotExist:
            return render(request, "index.html", {"error": "Login yoki parol noto‘g‘ri"})

    return render(request, "index.html")


def student_home(request ):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        return render(request, "student/home.html", {"worker": worker})
    return redirect("index")


def teacher_home(request , id):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        if worker.category == "Teacher" and worker.id == id:
            groups = worker.groups.all()
            return render(request, "teacher/home/home.html", {"worker": worker, "groups": groups})
    return redirect("index")


def teacher_group_detail(request, teacher_id, group_id):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        if worker.category == "Teacher" and worker.id == teacher_id:
            group = worker.groups.get(id=group_id)
            return render(request, "teacher/home/guruhlar/detail.html", {"worker": worker, "group": group})
    return redirect("index")



""" def admin_home(request):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        return render(request, "admin/home.html", {"worker": worker})
    return redirect("index")
 """

def student_lessons(request, worker_id):
    worker_id = request.session.get("worker_id")
    if worker_id and Worker.category == "Student":
        worker = Worker.objects.get(id=worker_id)
        return render(request, "student/lesson/lesson.html", {"worker": worker})
    return redirect("index")


def student_reyting(request , worker_id):
    worker_id = request.session.get("worker_id")
    if worker_id and Worker.category == "Student":
        worker = Worker.objects.get(id=worker_id)
        return render(request, "student/reyting.html", {"worker": worker})
    return redirect("index")


def student_setting(request , worker_id):
    worker_id = request.session.get("worker_id")
    if worker_id and Worker.category == "Student":
        worker = Worker.objects.get(id=worker_id)
        return render(request, "student/setting.html", {"worker": worker})
    return redirect("index")

# Teacher-specific views

def teacher_lessons(request):
    worker_id = request.session.get("worker_id")
    if worker_id :
        worker = Worker.objects.get(id=worker_id)
        return render(request, "teacher/lesson/lesson.html", {"worker": worker})
    return redirect("index")


def teacher_reyting(request):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        if worker.category == "Teacher":
            return render(request, "teacher/reyting/reyting.html", {"worker": worker})
    return redirect("index")


def teacher_setting(request ):
    worker_id = request.session.get("worker_id")
    if worker_id:
        worker = Worker.objects.get(id=worker_id)
        return render(request, "teacher/setting/setting.html", {"worker": worker})
    return redirect("index")




# logout view
def logout_view(request):
    request.session.flush()  # Barcha sessiya ma'lumotlarini o‘chiradi
    return redirect("index")
