from django.shortcuts import render
from .models import place
from .models import team


# Create your views here.
def web(request):
    obj = place.objects.all()
    obg = team.objects.all()
    return render(request, "index.html", {'result': obj , 'results' : obg})


# def web1(request):
#     obj1 = team.objects.all()
#     return render(request, "index.html", {'results': obj1})
