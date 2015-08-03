#!/usr/bin/env python


import re
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
#print cisco_cfg

crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                             childspec=r'AES')

print "\nCrypto maps not using AES:"
for cmap in crypto_maps:
    #print cmap.text
    for child in cmap.children:
        if 'transform' in child.text:
        #    print child.text
            match = re.search(r"set transform-set (.*)$", child.text)
            encryption = match.group(1)
    print "  {0} >>> {1}".format(cmap.text.strip(), encryption)
