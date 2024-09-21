from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_page(request, name):
    return render(request, f"entries/{name}.md")

def add(request):
    return render(request, "encyclopedia/add.html")

def new_entry(request):
    if request.method == "POST":
        print("This is a POST Method")
        title = request.POST.get("title")
        return HttpResponse(f"<h1> NEW POST for: {title} </h1>")
