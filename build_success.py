#!/bin/python
from jenkinsapi import jenkins
job = 'Java-Freestyle'

def get_jenkins():
    return jenkins.Jenkins('http://192.168.10.13:8080', 'krahul', 'ebbd7121de324db16ccdc304111be3d4',timeout=10)

def assign_build_category(myjob):
    builds = {'success':[],'failure':[]}
    for build_id in myjob.get_build_ids():
        build_status = myjob.get_build(build_id).get_status()
	if build_status == 'SUCCESS':
	    builds['success'].append(build_id)
	else:
	    builds['failure'].append(build_id)
    return builds

server = get_jenkins()
myjob = server.get_job(job)
builds = assign_build_category(myjob)

print "Successfull builds are %s" % (builds['success'])

print "Failure Builds are %s" % (builds['failure'])
