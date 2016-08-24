from django.http import HttpResponse
'''from django.template import loader'''
from .models import applicants
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.http import Http404
from django.views.generic.edit import  CreateView,UpdateView,DeleteView




def index(request):

        all_app= applicants.objects.all()
        '''
                for email in all_app:
            url='/aces/' + str(email.id) + '/'
            html +='<a href="' + url + '">'+ email.email + '</a><br>'
        '''

        context ={'all_app':all_app}
        return render(request,'aces/index.html',context)
'''return HttpResponse(template.render(context,request))'''



def detail(request,aces_id):

    try:
        email= applicants.objects.get(pk=aces_id)
    except applicants.DoesNotExist:
        raise Http404("email doesn't exist")
    return render(request, 'aces/detail.html', {'email':email})


class UserFormView(View):
    form_class=UserForm
    template_name='aces/login.html'

#display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #process form data
    def post(self,request):
        form =self.form_class(request.POST)

        if form.is_valid():
            #here we store data locally not in data base first
            user=form.save(commit=False)
            username =form.cleaned_data('username')
            password =form.cleaned_data('password')
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user =authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('aces/login.html') #elurl dah lessa h3mlo
            return render(request,self.template_name,{'form':form})



