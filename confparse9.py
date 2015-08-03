#!/usr/bin/env python


from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
#print cisco_cfg

crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',
                                             childspec=r'pfs group2')

print "\nCrypto Maps using PFS group2:"
for cmap in crypto_maps:
    print cmap.text
