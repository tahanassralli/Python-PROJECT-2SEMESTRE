from django.conf.urls import patterns, include, url
import vmm.views
import person.views
import template.views 
from Cloudstack import menu
from backend import vmcrud


urlpatterns = patterns('',
	url(r'^allVms/$',menu.listAllVMs,name="all-vms",),
	url(r'^users/$',person.views.showUsers,name="all-users",),
	url(r'^log/$',vmm.views.log,name="log",),
	url(r'^deleteevent/(?P<eventid>\d+)/$',vmm.views.deleteevent,name="delete-log",),
	url(r'^vm/(?P<vm_id>\d+)/$',vmm.views.getVmById,name="get-vm",),
	url(r'^destroyvm/(?P<id>\d+)/$',menu.destroyVM,),
	url(r'^startVm/(?P<id>\d+)/$',menu.startVM),
	url(r'^restartVM/(?P<id>\d+)/$',menu.restartVM),
	url(r'^stopVM/(?P<id>\d+)/$',menu.stopVM),
	url(r'^restoreVM/(?P<id>\d+)/$',menu.restartVM),
	url(r'^FormCreateVm/$',vmm.views.CreateVmView,name="form-create-vm",),
	url(r'^createVM/$',menu.createVM,),
	
	url(r'^FormCreatePw/$',vmm.views.CreatePwView,name="form-create-pw",),
	url(r'^createPw/$',vmcrud.deploypw,),
	
	url(r'^FormCreateFw/$',vmm.views.CreateFwView,name="form-create-fw",),
	url(r'^createFw/$',vmcrud.deployvm,),

	
	
	url(r'^allTemplates/$',template.views.ListTemplateView,name="all-templates",),
	url(r'^createTemplate/$',template.views.createTemplate,name="create-template",),
	url(r'^createTemplateLogic/$',template.views.createTemplateLogic,),
	
	url(r'^login/$',person.views.login,name="login",),
	url(r'^logout/$',person.views.logout,name="logout",),
	url(r'^verification/$',person.views.verification,name="verification",),
	url(r'^createAccount/$',person.views.createAccount,),
	url(r'^createAccountLogic/$',person.views.createAccountLogic,name="createAccountLogic",),
	
)
'''

url(r'^accounts/login/$',views.login),
	url(r'^accounts/auth/$',views.auth_view),
	url(r'^accounts/logout/$',views.logout),	
	url(r'^accounts/loggedin/$',views.loggedin),
	url(r'^accounts/invalid/$',views.invalid_login),
	url(r'^session/(?P<username>[a-z\-]+)/$',menu.userSession,),
'''
