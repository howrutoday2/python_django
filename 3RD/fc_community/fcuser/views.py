from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password ## password 암호화
from .models import Fcuser
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    print(user_id)

    if user_id:
        fcuser= Fcuser.objects.get(pk=user_id)
        print(fcuser)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home!')

def logout(request):
    if request.session.get['user']:
        del(request.session['user'])
    return redirect('/')


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            ##
            request.session['user']=form.user_id
            return redirect('/')
    else:
        form=LoginForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        print("--post==")
        username=request.POST.get('username',None)
        useremail=request.POST.get('useremail',None)
        password=request.POST.get('password', None)
        re_password=request.POST.get('re-password',None)

        print(username,useremail, password, re_password)


        res_data = {} ##response data
        
        ##예외처리: 비어있을경우
        if not(username and useremail and password and re_password):
            res_data['error'] = '모든값을 입력해주세요'
        
        ## 예외처리2: 비밀번호 확인과 다른경우
        elif password !=re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            # return HttpResponse("비밀번호가 다릅니다.")
        else:

            fcuser= Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()
        return render(request, 'register.html', res_data)