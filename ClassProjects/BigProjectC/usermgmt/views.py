# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from usermgmt.models import Member

def list_members(request):
    members = Member.objects.all()
    return render(request, 'usermgmt/list_members.html', {'members' : members})


from usermgmt.forms import MemberForm

def create_member(request):
    form = MemberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_members')

    return render(request, 'usermgmt/member_form.html', {'form': form})


def update_member(request, id):
    member = Member.objects.get(id=id)
    form = MemberForm(request.POST or None, instance=member)

    if form.is_valid():
        form.save()
        return redirect('list_members')

    return render(request, 'usermgmt/member_form.html', {'form': form, 'member': member})


def delete_member(request, id):
    member = Member.objects.get(id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('list_members')

    return render(request, 'usermgmt/member_delete_confirm.html', {'member': member})
