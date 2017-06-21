# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from django.views.generic import ListView

from vmm.models import Vm


class ListVmView(ListView):

    model = Vm
    template_name= 'Vm_list.html'
    

class CreateVmView(CreateView):

    model = Vm
    template_name = 'edit_Vm.html'

    def get_success_url(self):
        return reverse('Vms-list')
    
    