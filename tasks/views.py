from django.shortcuts import render

tasks = [
    "Learn Python",
    "Learn SQL",
    "Learn Django"
]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add_task(request):
    return render(request, "tasks/add.html")
