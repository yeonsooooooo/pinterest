from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# Create your views here.

@login_required
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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    # 방문한 사람의 정보가 아니라, 특정 pk를 가진 사람의 정보를 보여주려면 view에서 제공하는 context_object_name 을 써주면 된다.
    context_object_name = 'target_user'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required,'post')
@method_decorator(account_ownership_required,'get')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required,'post')
@method_decorator(account_ownership_required,'get')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template = 'accountapp/delete.html'
    context_object_name = 'target_user'