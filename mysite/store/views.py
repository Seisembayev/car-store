from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Comment, Picture
import datetime
from django.conf import settings

def index(request):
    cars = Car.objects.all()
    pictures = Picture.objects.all()
    return render(request, "store/index.html", {'cars': cars, 'pictures': pictures})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def new(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		model = request.POST.get('model')
		year = request.POST.get('year')
		motor = request.POST.get('motor')
		mileage = request.POST.get('mileage')
		drive = request.POST.get('drive')
		wheel = request.POST.get('wheel')
		info = request.POST.get('info')
		price = request.POST.get('price')
		color = request.POST.get('color')
		now = datetime.datetime.now()
		newCar = Car(name=name, model=model, info=info, year=year, motor=motor, price=price, color=color, mileage=mileage, drive=drive, wheel=wheel, user=request.user, date=now)
		newCar.save()
		newPic = Picture(image=request.FILES['image'], car=newCar, main=True)
		newPic.save()
		return redirect('index')
	return render(request, 'store/new.html')

def car(request):
	car_id = int(request.GET.get('id'))
	car = Car.objects.get(id = car_id)
	comments = Comment.objects.all()
	pictures = Picture.objects.all()
	return render(request, 'store/car.html', {'car': car, 'comments': comments, 'pictures': pictures})

def addComment(request):
	if request.method == 'POST':
		comment = request.POST.get('comment')
		car_id = int(request.POST.get('car_id'))
		car = Car.objects.get(id = car_id)
		now = datetime.datetime.now()
		newComment = Comment(comment=comment, user=request.user, car=car, date=now)
		newComment.save()
		return redirect(request.META.get('HTTP_REFERER','/'))
	return render(request, 'store/addComment.html')

def delComment(request):
	if request.method == 'GET':
		id = request.GET.get('id')
		comment = Comment.objects.get(id=id)
		comment.delete()
		return redirect(request.META.get('HTTP_REFERER','/'))
	return render(request, 'store/delComment.html')

def delCar(request):
	if request.method == 'GET':
		id = request.GET.get('id')
		car = Car.objects.get(id=id)
		car.delete()
		return redirect('index')
	return render(request, 'store/delCar.html')

def delPic(request):
	if request.method == "GET":
		id = int(request.GET.get('id'))
		pic = Picture.objects.get(id=id)
		all = Picture.objects.all()
		pic.delete()
		if pic.main == True:
			for i in all:
				if i.id == id+1:
					i.main = True
					i.save()
		return redirect(request.META.get('HTTP_REFERER','/'))
	return render(request, 'store/delPic.html')	

def edit(request):
	pictures = Picture.objects.all()
	if request.method == "GET":
		id = request.GET.get('id')
		car = Car.objects.get(id=id)
	elif request.method == "POST":
		id = request.POST.get('id')
		car = Car.objects.get(id=id)
		car.name = request.POST.get('name')
		car.model = request.POST.get('model')
		car.year = request.POST.get('year')
		car.motor = request.POST.get('motor')
		car.mileage = request.POST.get('mileage')
		car.drive = request.POST.get('drive')
		car.wheel = request.POST.get('wheel')
		car.info = request.POST.get('info')
		car.price = request.POST.get('price')
		car.color = request.POST.get('color')
		car.phone = request.POST.get('phone')
		car.city = request.POST.get('city')
		car.save()
		flag = True
		if bool(request.FILES) == True:
			for i in pictures:
				if i.car == car:
					flag = False
			if flag:
				newPic = Picture(image=request.FILES['image'], car=car, main=True)
				newPic.save()
			else: 
				newPic = Picture(image=request.FILES['image'], car=car)
				newPic.save()
		return redirect(request.META.get('HTTP_REFERER','/'))
	return render(request, 'store/edit.html', {'car': car, 'pictures': pictures})

def search(request):
	if request.method == "POST":
		check = True
		car = Car.objects.all()
		search = request.POST.get('search').lower()
		res = []
		for i in car:
			if i.name.lower().find(search)!=-1:
				res.append(i.id)
		pictures = Picture.objects.all()
		if bool(res) == False:
			check = False
	return render(request, 'store/search.html', {'car': car, 'pictures': pictures, 'search': search, 'res': res, 'check': check})

def profile(request):
	car = Car.objects.all()
	pictures = Picture.objects.all()
	return render(request, 'store/profile.html', {'user': request.user, 'car': car, 'pictures': pictures})