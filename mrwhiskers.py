#!/usr/bin/env python

import json
import urllib2
import ssl
import subprocess
import sys
import time
import random

#TODO make the hostname an argument
puppet_url = 'https://glsn1-mom:8140/status/v1/services/pe-jruby-metrics?level=debug'
fib = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
threshold = 80

# first sleep a random amount
time.sleep(random.randint(0,30))

while True:
  for x in fib:
    # First get a connection to the JSON endpoint, keep trying in case of errors
    connected = False
    while (!connected):
      try:
        response = urllib2.urlopen(puppet_url)
      except URLError as e:
        print e
        time.sleep(10)
        continue
      connnected = True

    data     = response.read()
    rdata    = json.loads(data)
    reqs     = len(rdata['status']['experimental']['metrics']['requested-instances'])
  
    if reqs < threshold:
      print "Requested JRubies below threshold, launching Puppet"
      # Launch and exit
      #subprocess.call('rm -rf ~/.puppetlabs/opt/puppet/cache',shell=True)
      #sys.exit(subprocess.call('puppet agent -t',shell=True))
      subprocess.call('puppet agent -t',shell=True)
      #time.sleep(random.randint(0,10))
      time.sleep(5)
      break

    q = random.choice(fib)
    print "sleeping %s" % q
    time.sleep(q)

  # If we get here, we've run out of retries
  if x == 987:
    print "Launching process unsuccessful"
    sys.exit(1)

#print len(rdata['status']['experimental']['metrics']['requested-instances'])
