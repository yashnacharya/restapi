from django.shortcuts import redirect, render
from .models import Empoyees
# from . models import Empoyees
# Create your views here.
def index(request):
    emp = Empoyees.objects.all()

    context = {
        'emp': emp,
    }
    return render(request,'index.html',context)
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Empoyees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        print(emp)
        emp.save()

    return redirect('index')
def edit(request):
    emp = Empoyees.objects.all()
    context = {
        'emp':emp,
    }
    return redirect(request, 'index.html', context)
def update(request, id):
    if request.method == 'POST':
        # id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Empoyees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        print(emp)
        emp.save()

    return redirect('index')
    # return render(request,'index.html',context)
def delete(request, id):
    emp = Empoyees.objects.filter(id = id).delete()
        # emp = Empoyees.objects.all()

    context = {
        'emp': emp,
    }
    return redirect('index')