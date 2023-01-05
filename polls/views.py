from django.urls import reverse_lazy
from . import models
from . import forms
from .models import SettingSize
from .forms import SignUpForm
from django.utils import timezone
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    DeleteView)


def EachSize(num):
    HeikinList=[]
    sizes = SettingSize.objects.filter(type = num)
    counts = len(sizes)
    for type,typeVa  in zip(types,types.values()):
        sizelist = list(sizes.values_list(type, flat=True))
        i = 0
        for size in sizelist:
            i += size
            heikin = i//counts
            StrHeikin = str(heikin)              
            ave_resu= typeVa+':'+StrHeikin
        HeikinList.append(ave_resu)

    return HeikinList


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SizeView(CreateView):
    template_name = "size_registration.html"
    form_class = forms.SizeForm
    success_url ="/"
    

class SizeList(ListView):
    model=models.SettingSize
    context_object_name='size_list'
    template_name = "size_list.html"

class SizeDetails(DetailView):
    model=models.SettingSize
    context_object_name='size_detail'
    template_name = "size_details.html"

class SizeUpdate(UpdateView):
    template_name = "size_update.html"
    model=models.SettingSize
    fields = ("name","type","body_length","chest","shoulder","arm","comfort")
    success_url = reverse_lazy('list')    
    
    def form_valid(self, form):
        size = form.save(commit=False)
        size.updated_at = timezone.now()
        size.save()
        return super().form_valid(form)

class SizeDelete(DeleteView):
    template_name = "size_delete.html"
    model = models.SettingSize
    success_url = reverse_lazy('list')



class Average(ListView):
    model = models.SettingSize
    template_name ="size_ave.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        HeikinList=[]
        sizes = SettingSize.objects.all()
        types = {
            'body_length':'着丈',
            'chest':'胸囲',
            'shoulder':'肩幅',
            'arm':'袖丈'
            }
        counts = len(sizes)        

        for type,typeVa  in zip(types,types.values()):
            sizelist = list(sizes.values_list(type, flat=True))
            i = 0     
            for size in sizelist:          
                i += size
                heikin = i//counts                     
                StrHeikin = str(heikin)                
                heikins = typeVa+':'+StrHeikin                
            HeikinList.append(heikins)

        
        context['HeikinList'] = HeikinList
        context['counts'] = counts
        context['outers'] = EachSize(1)     
        context['longs'] = EachSize(2)     
        context['shorts'] = EachSize(3)     
        context['sweats'] = EachSize(5)     

        return context    




nums= (1,2,3,4)
numsTys=('アウター','長袖トップス','半袖トップス','スウェット/パーカー')
HeikinList=[]
sizes = SettingSize.objects.all()
types = {
    'body_length':'着丈',
    'chest':'胸囲',
    'shoulder':'肩幅',
    'arm':'袖丈'
    }
# counts = len(sizes)
for num,numTy in zip(nums,numsTys):
    sizes = SettingSize.objects.filter(type = num)
    counts = len(sizes)  
    for type,typeVa  in zip(types,types.values()):
        sizelist = list(sizes.values_list(type, flat=True))
        i = 0     
        for size in sizelist:          
            i += size
            heikin = i//counts      
        # print(typeVa,':',heikin) 
            StrHeikin = str(heikin)                
            heikins = typeVa+':'+StrHeikin
    eachTy = numTy+'・'+heikins
    HeikinList.append(eachTy)



def EachSize(num):
    HeikinList=[]
    sizes = SettingSize.objects.filter(type = num)
    counts = len(sizes)
    for type,typeVa  in zip(types,types.values()):
        sizelist = list(sizes.values_list(type, flat=True))
        i = 0
        for size in sizelist:
            i += size
            heikin = i//counts
            StrHeikin = str(heikin)              
            ave_resu= typeVa+':'+StrHeikin
        HeikinList.append(ave_resu)

    return HeikinList