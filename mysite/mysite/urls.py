from django.conf.urls import include, url
from django.contrib import admin
import vmm.views
from backend import vmcrud

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', vmm.views.ListVmView.as_view(),
        name='Vms-list',),
    url(r'^newvm$', vmm.views.CreateVmView.as_view(),name='Vm-new',),
    url(r'^create$',vmcrud.deployvm,name='create-vm',),
]
