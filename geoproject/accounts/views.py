from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                return redirect("/index.html")
            return render(request, 'registration/login.html', { 'msg': '', 'form': form })
        else:
            return render(request, 'registration/login.html', { 'msg': u'ユーザID、あるいはパスワードが一致しません。', 'form': form})
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', { 'msg': '', 'form': form })