from django.http import HttpResponse
from django.shortcuts import render
from .models import place, person


# Create your views here.
# def demo(request):
#   return HttpResponse("hallo world")


def demo(request):
    obj = place.objects.all()
    per = person.objects.all()
    return render(request, 'index.html', {'result': obj,'person': per})



#def demo(request):
  #  per = person.objects.all()
#    return render(request, 'index.html', {})
