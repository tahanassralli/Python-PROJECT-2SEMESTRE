from django.conf.urls import patterns, include, url
import vmm.views
import pw.views
from backend import vmcrud
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newproj.views.home', name='home'),
    # url(r'^newproj/', include('newproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', vmm.views.ListVmView.as_view(),
      #  name='Vms-list',),
   # url(r'^newvm$', vmm.views.CreateVmView.as_view(),name='Vm-new',),
   # url(r'^create$',vmcrud.deployvm,name='create-vm',),
   url(r'^ListPW/$',pw.views.ListVmView,name="form-list-vm",),
	url(r'^FormCreateVm/$',vmm.views.CreateVmView,name="form-create-vm",),
	url(r'^createVM/$',vmcrud.deployvm,),
	url(r'^FormCreatePw/$',pw.views.CreateVmView,name="form-create-vm",),
	url(r'^createPw/$',vmcrud.deploypw,),
)
