from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')
        #
        # 가져온 데이터를 저장하는 법

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        #데이터베이스에 정보를 가져와서 출력하는 법
        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

        # return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
