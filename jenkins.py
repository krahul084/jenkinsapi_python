#!/bin/python
from jenkinsapi import jenkins

def get_server_instance():
    return jenkins.Jenkins('http://192.168.10.13:8080', 'krahul', 'ebbd7121de324db16ccdc304111be3d4',timeout=10)

def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    print "Total number of plugins installed: %s" % (len(server.get_plugins().keys()))
    for plugin in server.get_plugins().values():
        print "Short Name:%s" % (plugin.shortName)
        print "Long Name:%s" % (plugin.longName)
        print "Version:%s" % (plugin.version)
        print "URL:%s" % (plugin.url)
        print "Active:%s" % (plugin.active)
        print "Enabled:%s" % (plugin.enabled)
get_plugin_details()
