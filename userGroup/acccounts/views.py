from django.shortcuts import render, redirect
from .models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import GroupForm


# Create your views here.
def index(request):
    users = User.objects.all()
    total_user = User.objects.all().count()
    return render(request, 'user_group/index.html', context= {
        'users': users,
        'total_user': total_user,
    })


def group_list(request):
    all_group = Group.objects.all().order_by('id')
    total_group = Group.objects.all().count()
    return render(request, 'user_group/all_group.html', context= {
        'list_group': all_group,
        'total_group': total_group,
    })


def view_user_info(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'user_group/user_info.html', context= {
        'user': user,
    })


def view_group_info(request, pk):
    group = Group.objects.get(id=pk)
    user = User.objects.filter(group=group).count
    return render(request, 'user_group/group_info.html', context= {
        'group': group,
        'total_user': user,
    })


class UserCreate(CreateView):
    model = User
    fields = '__all__'
    initial = {'nickname':'User nickname', 'created_date':'User created date', 'group':'Groups',}
    success_url = reverse_lazy('index')
    template_name_suffix = '_create'


class UserUpdate(UpdateView):
    model = User
    fields = ['nickname', 'group']
    template_name_suffix = '_update'


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('index')
    template_name_suffix = '_delete'

"""
class GroupCreate(CreateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('all_group')
    template_name_suffix = '_create'
class GroupUpdate(UpdateView):
    model = Group
    fields = ['id', 'name', 'descripion']
    template_name_suffix = '_update'
class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('all_group')
    template_name_suffix = '_delete'
"""

def group_create(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_group')
    return render(request, 'acccounts/group_create.html', context={
        'form': form
    })



def group_update(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group/{id}'.format(id=group.get_absolute_url()))
    return render(request, 'acccounts/group_update.html', context={
        'form': form
    })


def group_delete(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST'"":
        group.delete()
        return redirect('all_group')
    return render(request, 'acccounts/group_delete.html', context={
        'group': group
    })