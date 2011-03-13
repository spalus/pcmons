
#Configurations used in the Controller.py
ADMINS = (
     ('Shirlei', 'shirlei@gmail.com'),
     ('Rafael', 'rafael.uriarte@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default':{
		'ENGINE':'mysql',
		'NAME':'manager',
		'USER':'manager',
		'PASSWORD':'cloudmanager',
		'HOST':'localhost',
		'PORT':3306,  #don't put between '' cause this will cause mysql connect error from python, saying that an integer is required!!
	}
}

#Key given by the Cloud provider(on eucalyptus you can get on the web interface)
AWS_ACCESS_KEY_ID = 'wgD8HAlfoLr9frjUjS1Q8xErIHulRKG4gVGw'
#Key given by the Cloud provider(on eucalyptus you can get on the web interface)
AWS_SECRET_ACCESS_KEY = 'LnXDoigLgfHUsEMVyZBLBXsOqeXZjPrZrR5kfQ'
#Path to the ec2 service
PATH_TO_EC2_SERVICE = '/services/Eucalyptus'

#Ip from the cloud provider, where the ec2 interface is accessible(on eucalyptus from the cloud controller)
IP_CLOUD_CONTROLLER = "150.162.63.25"
#Interface on this provider
EC2_INTERFACE_PORT_ON_CLOUD_CONTROLLER = 8773

#Configurations file of Eucalyptus server, must be accessible by this server
PATH_TO_EUCALYPTUS_CONFIG_FILE = "/etc/eucalyptus/eucalyptus.conf"

#Configured port on the clients that respond the currently running vms on each node
PORT_PLUGINS_ON_NODES = "60000"

#The patch must be writable
PATH_TO_LOG_FILE = "/var/log/Monitoring_Cloud_Server.log"

#Configurations used in the DB_Connector.py
#Table on the database
VM_TABLE = 'vmmonitor_vm'

#Configurations used in the Generate_VMs_Nagios_Conf.py
NAGIOS_TEMP_CONF='/tmp/vms_nagios'
COMMAND_TO_RELOAD_NAGIOS='/etc/init.d/nagios reload'
#place where the software will generate the configuration file for the Nagios(the place where the nagios should read this conf and apply the changes)
VMS_NAGIOS_FILE='/etc/nagios/cloud/vms_nagios.cfg'

#Using nagios grapher 
USING_NAGIOSGRAPHER=True

#If yes, what the path to the serviceext
PATH_SERVICEEXT_NAGIOSGRAPHER='/etc/nagios/serviceext'

#Nagios passive Checks
#Current ip of the interface listening to requests
LISTEN_IP = '150.162.63.25'

#Port where this client will listen to requests
LISTEN_PORT = 60001

INTERFACE="nagios"
