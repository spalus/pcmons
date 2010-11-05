import commands, logging, sys
from SimpleXMLRPCServer import SimpleXMLRPCServer 
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
sys.path.append('/opt/pcmons/')
from running_vms.cluster.Mysql_Db_Connector import Db_Connector
import running_vms.cluster.cluster_config

class Server_Passive_Checks:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filename=running_vms.cluster.cluster_config.PATH_TO_LOG_FILE)
        self.db = Db_Connector()
        server = SimpleXMLRPCServer((running_vms.cluster.cluster_config.LISTEN_IP, running_vms.cluster.cluster_config.LISTEN_PORT), logRequests=True, requestHandler=RequestHandler)
        server.register_function(self.get_data_from_vm_plugin)
        try:
            server.serve_forever()
        except:
            e = sys.exc_info()[1]
            logging.error("server execution error in server_passive_checks: %s"%e)

    def register_passive_check(self, hostname, service, status, number):
        print './passive_check.sh %s %s %s %s'%(hostname,service,status,number) 
        status, output = commands.getstatusoutput('./send_passive_check_nagios.sh %s %s %s %s'%(hostname,service,status,number) )
        print 'status: ',status
        print 'output: ',output
        if status == 0:
            print 'ok'
        else:
            print'error'


    def get_data_from_vm_plugin(self,data):
        instance_id = self.db.get_id_by_ip(ipAddress[0])
        vm = self.db.get_vm_info(instance_id['instance_id'])
        hostname = "%s_%s_%s"%(vm['user'],vm['instance_id'],vm['node_hostname'])

        #1st inf = -/+ buffers/cache:       1478        280  - 2nd inf = 0.14 0.13 0.15 2/328 7216

        memUsed  = data[0].split()[2]
        print data[0].split()[2]
        memFree = data[0].split()[3]
        print data[0].split()[3]
        memTotal = (int(memFree)+int(memUsed))
        memPercentage = int( 100*(int(memUsed)/float(memTotal)))
        self.register_passive_check(hostname, 'RAM', 0, '"'+str(memPercentage) + ';'+str(memUsed)+'/'+str(memTotal)+'"')

        #CPU
        self.register_passive_check(hostname, 'Cpu_Load', 0, '"'+data[1]+'"')
        
        #HTTP Connections
        self.register_passive_check(hostname, 'HTTP_Connections', 0, '"'+data[2]+'"')

        return ''


class RequestHandler(SimpleXMLRPCRequestHandler):
    def __init__(self, request, client_address, server):
            global ipAddress
            ipAddress = client_address
            SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)

if __name__ == "__main__":
    server = Server_Passive_Checks()
