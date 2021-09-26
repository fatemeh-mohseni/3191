from django.shortcuts import render  , redirect
#   render(request, template_name, context=None, content_type=None, status=None, using=None)
#   Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
#  request : The request object used to generate this response.
#  context :  A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

#   redirect(to, *args, permanent=False, **kwargs)¶
#   Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.

from .forms import LoginForm, RegisterForm
from django.contrib.auth import SESSION_KEY, login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here in this way :
# def foo():
#   return render(request , 'sub directory in the templates directory / file.html ' )




def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
        
        

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/users/register')
        else:
            login_form.add_error('user_name', 'Not Found')

    context = {
        'login_form': login_form
    }

# user logout after an hour 
# check session attribs for more details
    request.session.set_expiry(3600)
    return render(request, 'userapp/login.html', context)

# --------------------------------------------------------------------------

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/users/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'userapp/register.html', context)

# --------------------------------------------------------------------------
