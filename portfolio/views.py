from django.shortcuts import render, get_object_or_404
from .models import Project,ContactMessage

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def detail_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'detail_page.html', {'project': project})

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        context = {'message_sent': True}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
    
    
def demo(request):
    return render(request, 'demo.html')