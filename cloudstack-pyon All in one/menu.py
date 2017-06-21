#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

import logging

import socket

import time

import CloudStack

api = 'http://196.203.216.18:5555/client/api'
##api = 'http://172.16.206.31:8080/client/api'

apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)



# Main menu
def main_menu():
    os.system('cls')
    print "\n ************** Welcome To Jass Team Project ***************\n"
    print "Please choose the menu you want to start:"
    print "1. VM Menu "
    print "2. List VMs"
    print "3. Firewall"
    print "4. PortForwarding"
    print "5. Create Snapshot"
    print "6. Create Template"
    print "7. Socket"
    print "8. Events "
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again :((( "
            menu_actions['main_menu']()
    return

# Menu 1
def VMmenu():
    id='6f1eb0c3-28c1-4555-b388-963e67a108ab'
    request = {
        'id': id,
    }
    print "\n################# Welcome To VM Menu  ###################"
    print "\n########## Create / Delete / Stop / Start  #############"
    print "\nEnter Command"
    
    print "' C 'to Create a new  VM"
    print "' S 'to Start VM"
    print "' P 'to Stop  VM"
    print "' R 'to Reboot  VM"
    print "' D 'to Destroy VM"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    while (choice!='9'):
	if   choice== "S":
            startVm = cloudstack.startVirtualMachine(request)
            print "VM being Starting. vm id = %s" % id
            sleep()
	    break
	
        elif choice== "C":
		print"Choose one Template "
		print "1.CentOS Server"
		print "2.Ubuntu Server"
		print "3.Debian Server"
		choiceofTemplate = raw_input(" >>  ")
		
		
		if choiceofTemplate=='1':
			templateidX='22cff7e4-af82-408f-a400-221b5fb4ae2a'
			print "CentOS Server"
			Vm_name = raw_input(" VM Name >>  ")
			
			
		elif choiceofTemplate=='2':
			templateidX='26dcfbfe-bad9-4bce-924d-9898bb54a5c8'
			print "Ubuntu Server"
			Vm_name = raw_input(" VM Name >>  ")
			
		elif choiceofTemplate=='1':
			templateidX='62a3d073-c843-48fb-a06a-94c5ae6c9987'
			print "Debian Server"
			Vm_name = raw_input(" VM Name >>  ")
			
		else :
			print "Not a valide choice"
			sleeptoback()
			break

		
		#print "ttttttttttttttt"
		
		job = cloudstack.deployVirtualMachine({
		    'serviceofferingid':'98d17394-e6cf-4f9d-b84f-82b3855ea78b',
		    'templateid':templateidX,
		    'zoneid':'95cddc7f-bc1b-4014-a7b4-585dcd684e01',
		    'name' : Vm_name,
		    'networkids': 'a4736f46-c8c8-494c-9a84-aaabaf3055d9',
		})
	
		print "VM being deployed. Job id = %s" % job['jobid']
		
		print "All Jobs:"
		jobs = cloudstack.listAsyncJobs({})
		for job in jobs:
		   print  "%s : %s, status = %s" % (job['jobid'], job['cmd'], job['jobstatus'])

		sleep()
		break
            
        elif choice== "P":
            StopVm = cloudstack.stopVirtualMachine(request)
            print "VM being Stoping. vm id = %s" % id
            sleep()
            break
        elif choice== "R":
            RebootVm = cloudstack.rebootVirtualMachine(request)
            print "VM being Rebooting. vm id = %s" % id
            sleep()
            break
        elif choice== "D":
            DestroyVm = cloudstack.destroyVirtualMachine(request)
            print "VM being Destoyed. vm id = %s" % id
            sleep()
            break
        else :
	    print "Not a valide choice"
	    sleeptoback()
	    break
	
    exec_menu(choice)
    return


# sleep de chargement 
def sleep():
	for i in range(50):
	    sys.stdout.write("\r{0}>".format("="*i))
	    sys.stdout.flush()
	    time.sleep( 0.1 )
#sleep error 	    
def sleeptoback():
	for i in range(10):
	    sys.stdout.write("\r{0}>".format("X"*i))
	    sys.stdout.flush()
	    time.sleep( 0.1)

	    
	

# Liste VM's
def ListVMs():
    networkid='a4736f46-c8c8-494c-9a84-aaabaf3055d9'
    requestNet = {
		  'networkid': networkid,
		  }
    domainid='Root'
    requestDom = {
	    'domainid': domainid,
	    }
    os.system('cls')
    print "\n################# Liste MV Menu  ###################"
    print "\n Enter Command"
    print " A .to List all Virtual Machines"
    print " N. to List Virtual Machines by Network"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    while (choice!='9'):
	     if   choice== "A":
		     vms = cloudstack.listVirtualMachines()
		     print"\n*****************List Of Virtual Machines*************"
	             for vm in vms:
			     print " IDVM : %s\n Name: %s\n State: %s\n Zone: %s\n Creation Date : %s\n IP Address: %s\n High Availability: %s\n Template Name: %s\ CPUs: %s\n CPU Frequency: %s Mhz\n Memory: %s\n"%(vm['id'], vm['name'], vm['state'], vm['zoneid'], vm['created'],vm['nic'][0]['ipaddress'],vm['haenable'],vm['templatename'],vm['cpunumber'],vm['cpuspeed'],vm['memory'])
			     print"\n******************************************************"
		     sleep()	
		     ListVMs() 
                      
	     elif choice== "N": 
		     vmsbynet=cloudstack.listVirtualMachines(requestNet)
		     print"\n**********List Of Virtual Machines* by Network*******"
		     for vmbynet in vmsbynet:
			     print "\n id=%s \n name=%s \n Sate=%s" % (vmbynet['id'], vmbynet['name'], vmbynet['state']  )
			     print"\n******************************************************"

		     sleep()	
		     break 	       
	     else :
		    print "Not a valide choice"
		    sleeptoback()
		    break
    exec_menu(choice)
    return

# Firewall
def Firewall():
    print "\n################# Firewall Menu ###################"
    
    print "Enter the Source CIDR (Format 0.0.0.0/0)"
    CIDR = raw_input("CIDR >>  ")
    print "Choose a Protocol     1.TCP    2.UDP    3.ICMP"
    Pro = raw_input(" Protocol >>  ")
    if Pro=='1':
	    Pro='TCP'
    elif Pro=='2':
	    Pro='UDP'
    elif Pro=='3':
	    Pro='ICMP'
    else :
	    print "Not a valide choice"
	    
    print "Enter a Start Port"
    Sport = raw_input("Start Port >>  ")
    print "Enter an End Port"
    Eport = raw_input("End Port >>  ")

    cloudstack.createFirewallRule({
	    'cidrlist':CIDR,
	    'startport':Sport,
	    'endport':Eport,
	    'ipaddressid':'eb03d24a-d005-4828-b740-20a1b4ce38ba',
	    'protocol':Pro,
	    })

    print "\n Firewall Rule Creating" 
    sleep()
##    print "9. Back"
##    print "0. Quit"
##    choice = raw_input(" >>  ")
##    exec_menu(choice)
    back()
    


# PortForwarding
def PortForwarding():
    print "\n################# Port Forwarding Menu ###################"

    print "Enter a Private Port"
    Priport = raw_input("Private Port >>  ")
    print "Enter a Public Port"
    Pubport = raw_input("Public Port >>  ")


    print "Choose a Protocol     1.TCP    2.UDP   "
    Pro = raw_input(" Protocol >>  ")
    if Pro=='1':
	    Pro='TCP'
    elif Pro=='2':
	    Pro='UDP'
    else :
	    print "Not a valide choice"

    cloudstack.createPortForwardingRule({
	    'ipaddressid':'eb03d24a-d005-4828-b740-20a1b4ce38ba',
            'privateport':Priport,
	    'protocol':Pro,
	    'publicport':Pubport,
	    'virtualmachineid':'d3501a4a-6e6d-4977-858f-05186496d4f3',
	    }
	    )	    

    print "\n Port Forwarding Rule Creating" 
    sleep()
##    print "9. Back"
##    print "0. Quit"
##    choice = raw_input(" >>  ")
##    exec_menu(choice)
##    return
##    brack()
    print "\n9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
    
# createSnapshot
def createSnapshot():
    print "################# Snapshot Menu  #################\n"

    request = {
        
        'volumeid':'37e7bce9-94df-4bfc-9369-8447530c9dd3',
    }
    cloudstack.createSnapshot(request)

    
    print "\n Creating Snapshot for the vm id=%s"%request['volumeid']
    sleep()
    brack()



# createTemplate
def createTemplate():
	print "################# Template Menu  #################\n"
	print "Create A new Template "
	Displaytext = raw_input(" Display Text >>  ")
	print "Template Name "
	Name = raw_input (" Name >>  ")
	print "Bits 1.32  2.64"
	bits = raw_input (" Name >>  ")
	if bits=='1':
	    bits='32'
        elif bits=='2':
	    bits='64'
        else :
	    print "Not a valide choice"

	request = {
		'displaytext': Displaytext,
	        'name':Name,
	        'ostypeid':'a01b94c6-a166-11e4-b2ef-005056847688',
		'volumeid':'37e7bce9-94df-4bfc-9369-8447530c9dd3',
                'bits':bits,
                'isfeatured':'true',
                'ispublic':'true',
		#'snapshotid':'',
	    }
	cloudstack.createTemplate(request)
	print "\n Creating Template for the vm id=%s"%request['volumeid']
	sleep()
	print "\n9. Back"
        print "0. Quit"
        choice = raw_input(" >>  ")
        exec_menu(choice)
        return


# socket
def socket():
	import socket

	host = ''
	port = 8000
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		serversocket.bind((host, port))
	        serversocket.listen(5)
		print "Server Started.."
	except socket.error as e:
		print(str(e))
	def threaded_client(conn):
		while True:
			data = conn.recv(1024)
			reply="Wrong command! Please try again.."
			if data.upper()=="DONE" or data =="":
				break
			elif data.upper()=="HTTPSTATUS":
				import agent.Services.httpd as httpd
	    		        http = httpd.webserver()
				reply=http()
			elif data.upper()=="IPTABLESTATUS":
				import agent.Services.iptables as iptables
				ipt = iptables.iptables()
				reply=ipt()
			print data
			conn.sendall(reply)
		conn.close()
	while True:
	    #serversocket.accept()
	    conn,addr = serversocket.accept()
	    print "Connected to "+str(addr[0])+":"+str(addr[1])
	    conn.send("Welcome, enter your command:")
	    threaded_client(conn);

    
    	back()


# Events
def Events():

    

    print "################# Events Menu  #################\n"
    print "Inter a Start Date (format 'yyyy-MM-dd' or 'yyyy-MM-dd HH:mm:ss'"
    Sdate = raw_input(" Startdate>>  ")

    events= cloudstack.listEvents({
        'startdate': Sdate,
        })
    LOG_FILENAME = 'Events_%s.log'%Sdate
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.debug("\nAccount \tCreated  \tDomain  \tType \tDescription \tLevel")
    print "\nAccount \tCreated  \tDomain  \Ttype \tDescription \tLevel"
    for event in events:
        logging.debug("\n%s %s %s %s %s %s" % ( event['account'],event['created'],event['domain'],event['type'],event['description'],event['level']))
        print "\n%s %s %s %s %s %s" % ( event['account'],event['created'],event['domain'],event['type'],event['description'],event['level'])
        
    print "\n9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
    
    
# Menu 2
def menu2():
    print "Hello Menu 2 !\n"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': VMmenu ,
    '2': ListVMs,
    '3': Firewall,
    '4': PortForwarding,
    '5': createSnapshot,
    '6': createTemplate,
    '7': socket,
    '8': Events,
    '9': back,
    '0': exit,
}

 

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
