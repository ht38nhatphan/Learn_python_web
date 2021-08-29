from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # arr = ['10','11','12','13']
    # i = len(arr)-1
    # arr1 = []
    # while(i>0):
    #     arr1.append(arr[i])
    #     i = i-1
    # arr1 = arr1[::-1]
    return render(request, 'pages/content.html',{
        #link
        "Link" : link.objects.order_by('-id')[:1],
        #hero
        "Hero" : hero.objects.order_by('-id')[:1],
        # about
        "About" : about.objects.order_by('-id')[:1],
        #process
        "Process" : process.objects.order_by('-id')[:3],
        #team
        "Team" : team.objects.order_by('-id')[:3],
        #solutions
        "Solution" : solutions.objects.order_by('-id')[:1],
        #possibilities
        "Possibilities" : possibilities.objects.order_by('-id')[:1],
        #services
        "Services" : services.objects.order_by('-id')[:1],
        #footer
        "Footer" : footer.objects.order_by('-id')[:1]

    })

