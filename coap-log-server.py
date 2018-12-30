#!/usr/bin/env python
import time
from coapthon import defines
from coapthon.resources.resource import Resource
import getopt
import sys
from coapthon.server.coap import CoAP

__author__ = 'Giacomo Tanganelli, adapted by Marc Kohaupt'


class LogResource(Resource):
    def __init__(self, name="LogResource", coap_server=None):
        super(LogResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Log Resource"

    def render_GET(self, request):
        print("Received GET...")
        return self

    def render_PUT(self, request):
        print("Received PUT...")
        self.payload = request.payload
        return self

    def render_POST(self, request):
#        print("Received POST...")
        res = LogResource()
        res.location_query = request.uri_query
        res.payload = request.payload
#	print("Request: %s" % (request))
#	print("URIPath: %s" % (request.uri_path))
#	print("Payload: %s" % (request.payload))
	print("POST /%s: '%s'" % (request.uri_query, request.payload))
        return res

    def render_DELETE(self, request):
        print("Received DELETE...")
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('log/', LogResource())

        print "CoAP Server start on " + host + ":" + str(port)
        print self.root.dump()


def usage():  # pragma: no cover
    print "coapserver.py -i <ip address> -p <port>"


def main(argv):  # pragma: no cover
    ip = "0.0.0.0"
    port = 5683
    multicast = False
    try:
        opts, args = getopt.getopt(argv, "hi:p:m", ["ip=", "port=", "multicast"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-m", "--multicast"):
            multicast = True

    server = CoAPServer(ip, port, multicast)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
