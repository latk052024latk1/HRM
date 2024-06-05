from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connections
from .forms import *
from django.http import FileResponse, Http404
import datetime
from .models import *
from users.models import *
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class DriverList(ListView):
    model = Drivers
    template_name = "driverdocs/driver_list.html"

@login_required()
def driver_view(request, pk, template_name='driverdocs/driver_detail.html'):
    drivers = get_object_or_404(Drivers, pk=pk)
    docs = Documents.objects.filter(dr_id=pk, relevance = True)

    now1 = datetime.datetime.now().date()
    end_day = now1 + datetime.timedelta(days=30)
    days = Documents.objects.filter(doc_expire__lte=end_day)

    return render(request, template_name, {'object':drivers, "docs":docs, "days":days})


class DriverCreate(CreateView):
    model = Drivers
    fields = ['dr_name', 'dr_surname', 'dr_email', 'birth_date']
    template_name = "driverdocs/driver_add.html"
    success_url = reverse_lazy('driverdocs:dr_new')

@login_required()
def driver_create(request, template_name = "driverdocs/driver_add.html"):
    from django.core.exceptions import ObjectDoesNotExist
    user = User.objects.get(pk=request.user.id)
    y = Drivers.objects.all()
    
    form = DriverForm(request.POST)
    
    if form.is_valid():
        new_d = request.POST["dr_personal"]
        try:  
            driver1 = Drivers.objects.get(dr_personal=new_d)
            if driver1:
                messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'ამ პირადი ნომრის მქონე მძღოლი უკვე არის დამატებული.')
        except Drivers.DoesNotExist:
            if (len(new_d)!=11):
                messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'პირადი ნომერი შეიცავს 11 ციფრს.')
            else:    
                u = UserActions.objects.create(user1=user,action=
f"მძღოლის დამატება ({request.POST['dr_name']} {request.POST['dr_surname']})")
                form.save()            
     
                return redirect(reverse_lazy('driverdocs:dr_list'))
    return render(request, template_name, {'form':form, 'y':y})

@login_required()
def docs_create(request, template_name='driverdocs/docs_add.html'):
    from django.core.exceptions import ObjectDoesNotExist
    y = Drivers.objects.all()
    form = DocsForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.dr_id_id = int(request.POST["dropdown"])
        driver1 = Drivers.objects.get(pk=obj.dr_id_id)
        category1 = request.POST['doc_category']
        user = User.objects.get(pk=request.user.id)

        if Documents.objects.filter(dr_id=driver1.dr_id, doc_category=category1, relevance=True).exists():
        
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
            'ამ ტიპის საბუთი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')

        
        elif Documents.objects.filter(doc_number=request.POST["doc_number"]).exists():
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                               'ამ ნომრის მქონე საბუთი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')
                    
        else:            
            obj.save()

    return render(request, template_name, {'form':form, 'y':y})


@login_required()
def pdf_view(request, pk):
    d = Documents.objects.get(pk=pk)
    file1 = d.doc_path
    try:
        return FileResponse(open(file1.path, 'rb'))
    except FileNotFoundError:
        raise Http404()

@login_required()
def docs_update(request, person_id, doc_category, template_name='driverdocs/docs_update.html'):
    certaind = Drivers.objects.get(pk=person_id)
    form = DocsForm1(request.POST, request.FILES)
    oldd = Documents.objects.get(dr_id_id=person_id, doc_category=doc_category, relevance=True)
    
    dc = DriverDocCategories.objects.get(cat_id = doc_category)
    
    pk1 = person_id
    cat = doc_category

    if form.is_valid():

        if (Documents.objects.filter(doc_number=request.POST["doc_number"]).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ ნომრის მქონე 
                        დოკუმენტი უკვე ბაზაშია.""")

        else:            
            oldd.relevance = False
            oldd.save()

            Documents.objects.create(dr_id_id=person_id, doc_number = request.POST["doc_number"], doc_category=dc, doc_given = request.POST["doc_given"], doc_expire = request.POST["doc_expire"], relevance = True, doc_path = request.FILES["doc_path"])

            name1 = certaind.dr_name
            surname1 = certaind.dr_surname
            user = request.user.id

            filtered = User.objects.get(pk=request.user.id)

            u = UserActions.objects.create(user1=filtered, action=
f"მძღოლიისთვის ({certaind.dr_name} {certaind.dr_surname}) საბუთის შეცვლა ({doc_category})")

            return redirect(reverse_lazy('driverdocs:dr_list'))
    return render(request, template_name, {'form': form, 'certaind': certaind, 'pk1': pk1, "cat": cat, "oldd":oldd})
