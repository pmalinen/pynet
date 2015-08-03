#!/usr/bin/env python


from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
#print cisco_cfg

crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for cmap in crypto_maps:
    print cmap.text
    for child in cmap.children:
        print child.text
