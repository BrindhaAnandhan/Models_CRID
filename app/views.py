from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

#This is display dept 
def display_dept(request):
    QLDO = Dept.objects.all()
    QLDO = Dept.objects.filter(Q(Dept_no__gt = 100) & Q(Loc__startswith = 'B') | Q(Dname = 'Worker'))
    data = {'dept': QLDO}
    return render(request,'display_dept.html', data)

# This is to display emp
def display_emp(request):
    QLEO = Emp.objects.all()
    # QLEO = Emp.objects.filter(Job= , Ename__startswith = 'A')
    data = {'emp': QLEO}
    return render(request,'display_emp.html', data)


# inserting from backend, for dept 
def Insert_dept(request):
    dn = int(input("Enter Dept Number: "))
    dname = input("Enter Dname: ")
    loc = input('Enter Location: ')

    ndo = Dept.objects.get_or_create(Dept_no = dn, Dname = dname, Loc = loc)[0]
    ndo.save()
    QLIO = Dept.objects.all()
    data = {'dept': QLIO}
    return render(request,'display_dept.html', data)

# inserting from backend for emp 

def Insert_emp(request):
    empn = int(input("Enter Emp number: "))
    ename = input("Enter Ename: ")
    job = input("Enter job: ")
    Mgr = int(input("Enter MGR: "))
    hiredate = input("Enter Hiredate: ")
    comm = int(input("Enter comm: "))
    deptno = int(input("Enter deptno: "))

    do = Dept.objects.get(Dept_no = deptno)
    empo = Emp.objects.get_or_create(Empno = empn, Ename = ename, Job = job, MGR = Mgr, Hiredate = hiredate, Comm= comm, Deptno = do)[0]
    empo.save()
    Qleo = Emp.objects.all()
    date = {'emp' : Qleo}
    return render(request, 'display_emp.html', date)



