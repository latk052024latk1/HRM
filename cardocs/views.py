from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connections
from cardocs.forms import *
from django.http import FileResponse, Http404
import datetime
from cardocs.models import *
from users.models import *
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
# Create your views here.

class CarCreate(CreateView):
    model = Cars
    fields = ['car_vin', 'car_reg_number', 'driver']
    template_name = "driverdocs/driver_add.html"
    success_url = reverse_lazy('cardocs:car_new')

@login_required()
def car_create(request, template_name="cardocs/car_add.html"):
    from django.core.exceptions import ObjectDoesNotExist
    y = Drivers.objects.all()
    form = CarForm(request.POST)
    if form.is_valid():
        
        obj = form.save(commit=False)
        obj.driver_id = int(request.POST["dropdown"])
        driver1 = Drivers.objects.get(pk=obj.driver_id)
        vin = request.POST["car_vin"]
        reg = request.POST["car_reg_number"]
        user = User.objects.get(pk=request.user.id)

        if Cars.objects.filter(driver=driver1).exists():
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ მძღოლისთვის უკვე
                 განსაზღვრულია მანქანა.""")
       
        elif (Cars.objects.filter(car_reg_number=reg).exists() or Cars.objects.filter(car_vin=vin).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ ნომრების მქონე 
                        მანქანა უკვე ბაზაშია.""")

        else:
            obj.save()
            return redirect('cardocs:car_new')
    return render(request, template_name, {'form': form, 'y': y})

@login_required()
def docs_create(request, template_name='cardocs/docs_add.html'):
    from django.core.exceptions import ObjectDoesNotExist

    c = Cars.objects.all()
    form = CarDocsForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.car_id = int(request.POST["dropdown"])
        obj.relevance=True
        car1 = Cars.objects.get(pk=obj.car_id)

        category1 = request.POST['car_doc_category']
        user1 = User.objects.get(pk=request.user.id)

        cat = DocCategories.objects.get(cat_id=category1)
        cat_id1 = cat.cat_id

        if (CarDocuments.objects.filter(car_doc_number=request.POST["car_doc_number"]).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                           'ამ ნომრის მქონე დოკუმენტი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')
            obj = form.save(commit=False)
        

        elif CarDocuments.objects.filter(car_id=car1.car_id, car_doc_category=cat_id1, relevance=True).exists():
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                           'ამ ტიპის დოკუმენტი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')    
            obj = form.save(commit=False)
        else:
            obj.save()

            return redirect('cardocs:docs_new')
    return render(request, template_name, {'form':form, 'c':c})

@login_required()
def docs_update(request, car_id, car_doc_category, template_name='cardocs/docs_update.html'):
    certaind = Cars.objects.get(pk=car_id)
    cat_data = DocCategories.objects.get(pk=car_doc_category)

    form = CarDocsUForm(request.POST, request.FILES)
    oldd = CarDocuments.objects.get(car=certaind, car_doc_category=cat_data, relevance=True)

    pk1 = car_id
    cat = car_doc_category

    if form.is_valid():

        if (CarDocuments.objects.filter(car_doc_number=request.POST["car_doc_number"]).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ ნომრების მქონე 
                        ტრაილერი უკვე ბაზაშია.""")
        else:             

            oldd.relevance = False
            oldd.save()

            c = CarDocuments.objects.create(car=certaind, car_doc_number = request.POST["car_doc_number"], car_doc_category=cat_data, car_doc_given = request.POST["car_doc_given"], car_doc_expire = request.POST["car_doc_expire"], relevance = True, car_doc_path = request.FILES["car_doc_path"])
            c.save()

            filtered = User.objects.get(pk=request.user.id)

            u = UserActions.objects.create(user1=filtered, action=f"მანქანა {certaind.car_reg_number} ისთვის საბუთის შეცვლა ({car_doc_category})")

            return redirect(reverse_lazy('cardocs:car_view', kwargs={'pk': certaind.car_id}))
    return render(request, template_name, {'form': form, 'certaind': certaind, 'pk1': pk1, "cat": cat, "oldd":oldd})


@login_required()
def car_view(request, pk, template_name='cardocs/car_detail.html'):
    cars = get_object_or_404(Cars, pk=pk)
    docs = CarDocuments.objects.filter(car_id=pk, relevance = True)

    now1 = datetime.datetime.now().date()
    end_day = now1 + datetime.timedelta(days=30)
    days = CarDocuments.objects.filter(car_doc_expire__lte=end_day)

    return render(request, template_name, {'object':cars, "docs":docs, "days":days})

class CarList(ListView):
    model = Cars
    template_name = "cardocs/car_list.html"


@login_required()
def pdf_view_car(request, pk):
    d = CarDocuments.objects.get(pk=pk)
    file1 = d.car_doc_path
    try:
        return FileResponse(open(file1.path, 'rb'))
    except FileNotFoundError:
        raise Http404()

@login_required()
def trailer_create(request, template_name="cardocs/trailer_add.html"):
    y = Cars.objects.all()
    form = TrailerForm(request.POST)
    if form.is_valid():

        obj = form.save(commit=False)
        a = int(request.POST["dropdown"])
        car1 = Cars.objects.get(pk=a)
        obj.car = car1
        vin = request.POST["trailer_vin"]
        reg = request.POST["trailer_reg_number"]

        if Trailers.objects.filter(car=car1).exists():
        
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                """ამ მანქანისთვის უკვე განსაზღვრულია ტრაილერი.""")
     
        elif (Trailers.objects.filter(trailer_reg_number=reg).exists() or Trailers.objects.filter(trailer_vin=vin).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ ნომრების მქონე 
                        ტრაილერი უკვე ბაზაშია.""")

            obj = form.save(commit=False)        

        else:
            user = User.objects.get(pk=request.user.id)

            u = UserActions.objects.create(user1=user,
                                           action=f"ტრაილერის ({vin},{reg}) დამატება")
            obj.save()

            return redirect('cardocs:car_new')

    return render(request, template_name, {'form': form, 'y': y})

@login_required()
def trailer_docs_create(request, template_name='cardocs/trailer_docs_add.html'):
    from django.core.exceptions import ObjectDoesNotExist

    c = Trailers.objects.all()
    form = TrailerDocsForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.trailer_id = int(request.POST["dropdown"])
        trailer1 = Trailers.objects.get(pk=obj.trailer_id)

        category1 = request.POST['trailer_doc_category']
        user1 = User.objects.get(pk=request.user.id)

        cat = DocCategories.objects.get(cat_id=category1)
        cat_id1 = cat.cat_id

        if (TrailerDocuments.objects.filter(trailer_doc_number=request.POST["trailer_doc_number"]).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                           'ამ ნომრის მქონე დოკუმენტი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')
            obj = form.save(commit=False)
            

        elif (TrailerDocuments.objects.filter(trailer_id=trailer1.trailer_id, trailer_doc_category=cat_id1, relevance=True).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
                           'ამ ტიპის დოკუმენტი უკვე არის ბაზაში, შეგიძლიათ შეცვალოთ იგი.')

            obj = form.save(commit=False)

        else:
            u = UserActions.objects.create(user1=user1,
                                               action=f"ტრაილერისთვის ({trailer1.trailer_reg_number}) საბუთის დამატება ({category1})")
            obj.save()
            return redirect('cardocs:trailer_docs_new')
    return render(request, template_name, {'form':form, 'c':c})

@login_required()
def trailer_docs_update(request, trailer_id, trailer_doc_category, template_name='cardocs/trailer_docs_update.html'):
    certaind = Trailers.objects.get(pk=trailer_id)
    cat_data = DocCategories.objects.get(pk=trailer_doc_category)

    form = TrailerDocsUForm(request.POST, request.FILES)
    oldd = TrailerDocuments.objects.get(trailer=certaind, trailer_doc_category=cat_data, relevance=True)

    pk1 = trailer_id
    cat = trailer_doc_category

    if form.is_valid():

        if (TrailerDocuments.objects.filter(trailer_doc_number=request.POST["trailer_doc_number"]).exists()):
            messages.add_message(request, settings.MY_EXTRA_ERROR, """ამ ნომრის მქონე 
                        დოკუმენტი უკვე ბაზაშია.""")
        else:             
            oldd.relevance = False
            oldd.save()

            c = TrailerDocuments.objects.create(trailer_id=certaind.trailer_id, trailer_doc_number = request.POST["trailer_doc_number"], trailer_doc_category=cat_data, trailer_doc_given= request.POST["trailer_doc_given"], trailer_doc_expire = request.POST["trailer_doc_expire"], relevance = True, trailer_doc_path = request.FILES["trailer_doc_path"])
            c.save()

            filtered = User.objects.get(pk=request.user.id)

            u = UserActions.objects.create(user1=filtered, action=f"მანქანა {certaind.trailer_reg_number} ისთვის საბუთის შეცვლა ({trailer_doc_category})")

            return redirect(reverse_lazy('cardocs:trailer_view', kwargs={'pk': certaind.trailer_id}))
    return render(request, template_name, {'form': form, 'certaind': certaind, 'pk1': pk1, "cat": cat, "oldd":oldd})

@login_required()
def trailer_view(request, pk, template_name='cardocs/trailer_detail.html'):
    trailers = get_object_or_404(Trailers, pk=pk)
    docs = TrailerDocuments.objects.filter(trailer_id=pk, relevance = True)

    now1 = datetime.datetime.now().date()
    end_day = now1 + datetime.timedelta(days=30)
    days = TrailerDocuments.objects.filter(trailer_doc_expire__lte=end_day)

    return render(request, template_name, {'object':trailers, "docs":docs, "days":days})

class TrailerList(ListView):
    model = Trailers
    template_name = "cardocs/trailer_list.html"

@login_required()
def pdf_view_trailer(request, pk):
    d = TrailerDocuments.objects.get(pk=pk)
    file1 = d.trailer_doc_path
    try:
        return FileResponse(open(file1.path, 'rb'))
    except FileNotFoundError:
        raise Http404()
