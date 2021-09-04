
from django.http.response import HttpResponse
from django.shortcuts  import render, redirect
from .models import KhachHang, NhanVien
from django.contrib.auth import authenticate, login, logout
from .forms import AddCustomer,UserLogin,UserAddForm
from django.contrib import messages
from django.contrib.auth.models import Group,User,UserManager
# Create your views here.
def index(request):
    if not (request.user.is_authenticated or request.user.is_superuser or request.user.is_staff):
        return redirect('/')

    return render(request, 'index.html')

def customer(request):
    data = { 'khachhang': KhachHang.objects.all() }
    return render(request, 'customer.html', data)

def staff(request):
    data = { 'nhanvien': NhanVien.objects.all() }
    return render(request, 'staff.html', data)

def addcustomer(request):
    if not (request.user.is_authenticated or request.user.is_superuser or request.user.is_staff):
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AddCustomer(data = request.POST)
            if form.is_valid():
                instance = form.save(commit = False)

                instance.HoTen= request.POST.get('HoTen')
                instance.SoDienThoai = request.POST.get('SoDienThoai')
                instance.DiaChi = request.POST.get('DiaChi')
                instance.SoCMT = request.POST.get('SoCMT')

                instance.save()


                messages.success(request,'Emergency Successfully Created for ',extra_tags = 'alert alert-success alert-dismissible show')
                return redirect('Quanly:addcustomer')

            else:
                messages.error(request,'Error Creating Emergency for ',extra_tags = 'alert alert-warning alert-dismissible show')
                return redirect('Quanly:addcustomer')

        dataset = dict()
        form = AddCustomer()
        dataset['form'] = form
        dataset['title'] = 'create customer'
        return render(request,'addCustomer.html',dataset)


# login
def login_view(request):
	'''
	work on me - needs messages and redirects
	
	'''
	login_user = request.user
	if request.method == 'POST':
		form = UserLogin(data = request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)
			if user and user.is_active:
				login(request,user)
				if login_user.is_authenticated:
					return redirect('Quanly:index')
			else:
			    messages.error(request,'Account is invalid',extra_tags = 'alert alert-error alert-dismissible show' )
			    return redirect('Quanly:login')

		else:
			return HttpResponse('data not valid')

	dataset=dict()
	form = UserLogin()
	dataset['form'] = form
    
	return render(request,'accounts/login.html',dataset)

# logout
def logout_view(request):
	logout(request)
	return redirect('Quanly:login')








# if request.method == 'POST':
#         form = AddCustomer(data = request.POST or None)
# 		if form.is_valid():
# 			instance = form.save(commit = False)
# 			# user = request.POST.get('user')
# 			# assigned_user = User.objects.get(id = user)
# 			# instance.user = assigned_user

# 			instance.HoTen= request.POST.get('HoTen')
# 			instance.SoDienThoai = request.POST.get('SoDienThoai')
# 			instance.DiaChi = request.POST.get('DiaChi')
# 			instance.SoCMT = request.POST.get('SoCMT')
			

# 			# now = datetime.datetime.now()
# 			# instance.created = now
# 			# instance.updated = now

# 			instance.save()

# 			# employee_email = instance.user.email
# 			# email_subject = 'Humanly Access Credentials'
# 			# email_message = 'You have been added to Rabotecgroup Staff List,username and password'
# 			# from_email = settings.EMAIL_HOST_USER
# 			# to_email = [employee_email]
# 			'''
# 			Work on it - user@gmail.com & user@rabotecgroup.com -> send Template
# 			'''
# 			# send_mail(
# 			# 	email_subject,
# 			# 	email_message,
# 			# 	from_email,
# 			# 	to_email,
# 			# 	fail_silently=True
# 			# 	)
            
# 			#Send email - username & password to employee, how to get users decrypted password ?
            
# 			return redirect('QuanLy:addcustomer')
# 		else:
# 			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
# 			return redirect('QuanLy:addcustomer')
# 	dataset = dict()
# 	form = AddCustomer()
# 	dataset['form'] = form
# 	dataset['title'] = 'create customer'
# 	return render(request,'addcustomer.html',dataset)
# def saveCustomer(request):
#     # g = addcustomer()
#     if request.method == 'POST':
#         g = addcustomer(request.POST)
#         if g.is_valid():
#             instance = g.save(commit = False)
#             instance.save() 
#             username = g.cleaned_data.get("HoTen")

#             messages.success(request,'Account created for {0} !!!'.format(username),extra_tags = 'alert alert-success alert-dismissible show')
#             return redirect('Quanly:addcustomer') 
# 		    # return redirect('Quanly:addcustomer')   
#         else:
#             messages.error(request,'Username is invalid',extra_tags = 'alert alert-warning alert-dismissible show')
#             return redirect('Quanly:addcustomer')
	 	

    # def register_user_view(request):
	# # WORK ON (MESSAGES AND UI) & extend with email field
	# if request.method == 'POST':
	# 	form = UserAddForm(data = request.POST)
	# 	if form.is_valid():
	# 		instance = form.save(commit = False)
	# 		instance.save()
	# 		username = form.cleaned_data.get("username")

	# 		messages.success(request,'Account created for {0} !!!'.format(username),extra_tags = 'alert alert-success alert-dismissible show' )
	# 		return redirect('accounts:register')
	# 	else:
	# 		messages.error(request,'Username or password is invalid',extra_tags = 'alert alert-warning alert-dismissible show')
	# 		return redirect('accounts:register')


	# form = UserAddForm()
	# dataset = dict()
	# dataset['form'] = form
	# dataset['title'] = 'register users'
	# return render(request,'accounts/register.html',dataset)