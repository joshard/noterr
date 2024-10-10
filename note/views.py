from django.shortcuts import redirect, render
from .models import Note, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as login_process, logout as logout_process
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    notes = Note.objects.all()
    context = {"Notes":notes}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")

# @login_required
def noteCreate(request):
    if request.method == "POST":
        author = request.user
        title = request.POST.get("title")
        content = request.POST.get("content")
        createNote = Note.objects.create(author=author, title=title, content=content)
        createNote.save()
        return render(request, "noteCreate.html")
    else:
        notes = Note.objects.all()
        context = {"Notes": notes}
        return render(request, "noteCreate.html", context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html")
        else:
            form = UserCreationForm()
            return render(request, "signup.html", {'form': form})
        
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_process(request, user)
            notes = Note.objects.all()
            context = {"Notes": notes}
            return render(request, "index.html", context)
        # else:
        #     return render(request, "login.html")
    else:
        return render(request, "login.html")

def logout(request):
    logout_process(request)
    return redirect('login')
