from django.shortcuts import render

from projects.models import Project
from .models import Profile

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="")
    other_skills = prof.skill_set.filter(description="")
    
    user_projects = Project.objects.filter(owner=prof)
    
    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
        'projects': user_projects,
    }
    return render(request, 'users/profile.html', context)