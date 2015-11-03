from django.shortcuts import render , render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Product,ProductType, Category
from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return redirect('http://127.0.0.1:8000/pasal/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def doneContact(request):
    return render_to_response('doneContact')

def contactUs(request):
    return render_to_response('contactus.html')

def show(request):
    products=Product.objects.all()
    categories= Category.objects.all()
    producttypes= ProductType.objects.all()
    return render_to_response('show.html',{'products':products,'categories':categories,'producttypes':producttypes})

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def register_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')        

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})   

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def category(request):
    categories= Category.objects.all()
    return render_to_response('category.html',{'categories':categories})

def customers(request):
    customers= Category.objects.all()
    return render_to_response('customer.html',{'customers':customers})

def products(request, id):
    products=Product.objects.filter(id=id)
    return render_to_response('productDetail.html',{'products':products})



