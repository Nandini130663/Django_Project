from django.shortcuts import render,redirect
from Foood.forms import Usregis,Upd,Pad,ContactForm,SoF
from django.http import HttpResponse
from online1 import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Foood.models import Exfd,South
from Foood.models import Work,Crpf
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'ht/about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['nanduchamarthi44@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, "ht/contact.html", {'t': form})


def regis(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				y.save()
				messages.success(request,"please check your {}  for login creadentials".format(rc))
				return redirect('/lg')
				messages.danger(request,"please check your {}  for login creadentials".format(rc))
	y = Usregis()
	return render(request,'ht/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'ht/dashboard.html')

@login_required
def prfle(request):
	return render(request,'ht/profile.html')

@login_required
def food(request):
	return render(request,'ht/foodlist.html')

	
@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'ht/updateprofile.html',{'r':p,'q':t})

@login_required
def chani(request):
	return render(request,'ht/north.html')

@login_required
def south(request):
	return render(request,'ht/south.html')

@login_required
def southw(request):
	return render(request,'ht/south1.html')

@login_required
def northw(request):
	return render(request,'ht/north1.html')

@login_required
def northwa(request):
	return render(request,'ht/north2.html')


@login_required
def southwa(request):
	return render(request,'ht/south2.html')

@login_required
def hyde(request):
	return render(request,'ht/hyd.html')


@login_required
def wrklg(request):
	p = Work.objects.filter(m_id=request.user.id)
	return render(request,'ht/worklog.html',{'y':p})

def creationwrk(request):
	if request.method == "POST":
		m = Work.objects.filter(m_id=request.user.id,date=request.POST['date'])
		if len(m)==0:
			r = WrkForm(request.POST)
			if r.is_valid():
				t = r.save(commit=False)
				t.m_id = request.user.id
				t.save()
				messages.success(request,"Successfully Uploaded your task")
				return redirect('/ke')
		messages.info(request,"Sorry you have already Submitted worklog for today")
		return redirect('/ke')
	r = WrkForm()
	return render(request,'ht/crwrk.html',{'d':r})

def delet(request):
	context ={}
	Work.objects.filter(id=request.user.id).delete()
	# obj = get_object_or_404(Work, id = request.user.id)
	# if request.method =="POST":
	# 	m.delete()
	# 	messages.success(request,"Data is deleted Successfully")
	return redirect('wk')
	# return render(request,'ht/delete.html',{'s':m})

# Create your views here.
