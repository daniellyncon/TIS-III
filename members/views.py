from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from django.http import HttpResponse
from .forms import MemberForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def members_list(request):
    member = Member.objects.all()
    return render(request, 'members_list.html/', {'members': member})


def members_new(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'members_form.html', {'form': form})


def members_update(request, id):
    member = get_object_or_404(Member, pk=id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'members_form.html', {'form': form})


def members_delete(request, id):
    member = get_object_or_404(Member, pk=id)
    form = MemberForm(request.POST or None, instance=member)

    if request.method == 'POST':
        member.delete()
        return redirect('member_list')

    return render(request, 'members_delete_confirm.html/', {'member': member})
