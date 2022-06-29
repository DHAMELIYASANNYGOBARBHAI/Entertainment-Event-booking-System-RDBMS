from django.shortcuts import render
from Event_Registration.models import CustModel,EventModel
from django.contrib import messages
from Event_Registration.forms import Custforms,Eventforms
from django.db import connection

def homepage(request):
    return render(request, 'Homepage.html')

def showcust(request):
    showall=CustModel.objects.all()
    return render(request, 'Index.html', {"data":showall})

def InsertCust(request):
    if request.method == "POST":
        if request.POST.get('c_id') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('c_email') and request.POST.get('c_Bdate') and request.POST.get('c_phno') and request.POST.get('password') and request.POST.get('age'):
            saverecord=CustModel()
            saverecord.c_id = request.POST.get('c_id')
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.c_email = request.POST.get('c_email')
            saverecord.c_Bdate = request.POST.get('c_Bdate')
            saverecord.c_phno = request.POST.get('c_phno')
            saverecord.password = request.POST.get('password')
            saverecord.age = request.POST.get('age')
            saverecord.save()
            messages.success(request, 'Customer' + saverecord.first_name + ' saved successfully!!!')
            return render(request, 'insert.html')
    else:
            return render(request, 'insert.html')

def EditCust(request, c_id):
    edittmpobject = CustModel.objects.get(c_id=c_id)    
    return render(request, 'Edit.html', {"CustModel":edittmpobject})

def UpdateCust(request, c_id):
    updatecustmor=CustModel.objects.get(c_id=c_id)
    form=Custforms(request.POST, instance=updatecustmor)
    if form.is_valid():
        form.save()
        messages.success(request, 'record updated Successfully!!')
        return render(request, 'Edit.html', {"CustModel":updatecustmor})

def DeleteCust(request, c_id):
    deletecust=CustModel.objects.get(c_id=c_id)
    deletecust.delete()
    showdata=CustModel.objects.all()
    return render(request, "Index.html", {"data": showdata})













def showevent(request):
    showall=EventModel.objects.all()
    return render(request, 'IndexEvent.html', {"data":showall})

def Insertevent(request):
    if request.method == "POST":
        if request.POST.get('event_id') and request.POST.get('e_type_id') and request.POST.get('e_name') and request.POST.get('e_date') and request.POST.get('e_size') and request.POST.get('address_line_1') and request.POST.get('address_line_2') and request.POST.get('pincode') and request.POST.get('e_manager'):
            saverecord=EventModel()
            saverecord.event_id = request.POST.get('event_id')
            saverecord.e_type_id = request.POST.get('e_type_id')
            saverecord.e_name = request.POST.get('e_name')
            saverecord.e_date = request.POST.get('e_date')
            saverecord.e_size = request.POST.get('e_size')
            saverecord.address_line_1 = request.POST.get('address_line_1')
            saverecord.address_line_1 = request.POST.get('address_line_2')
            saverecord.pincode = request.POST.get('pincode')
            saverecord.e_manager = request.POST.get('e_manager')
            saverecord.save()
            messages.success(request, 'event ' + saverecord.e_name + ' saved successfully!!!')
            return render(request, 'InsertEvent.html')
    else:
            return render(request, 'InsertEvent.html')

def EditEvent(request, event_id):
    edittmpobject = EventModel.objects.get(event_id=event_id)    
    return render(request, 'EditEvent.html', {"EventModel":edittmpobject})

def UpdateEvent(request, event_id):
    updateEvent=EventModel.objects.get(event_id=event_id)
    form=Eventforms(request.POST, instance=updateEvent)
    if form.is_valid():
        form.save()
        messages.success(request, 'record updated Successfully!!')
        return render(request, 'EditEvent.html', {"EventModel":updateEvent})

def DeleteEvent(request, event_id):
    deleteEvent=EventModel.objects.get(event_id=event_id)
    deleteEvent.delete()
    showdata=EventModel.objects.all()
    return render(request, "IndexEvent.html", {"data": showdata})




def runQueryCustomer(request):
    raw_query = "select * from customer where  age>=18 order by c_id;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQueryCustomer.html',{"data":alldata})


def runQueryEvent(request):
    raw_query = "select e_name, sum(no_of_tickets) from ticket natural join event group by e_name;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQueryEvent.html',{"data":alldata})