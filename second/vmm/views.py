# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context

from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from django.views.generic import ListView

from vmm.models import Fw


class ListVmView(ListView):

    model = Fw
    template_name= 'Vm_list.html'
    

class CreateVmView(CreateView):

    model = Fw
    template_name = 'edit_Vm.html'

    def get_success_url(self):
        return reverse('Vms-list')
    
def CreateVmView(request):
	return render_to_response('edit_Vm.html')