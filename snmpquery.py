from pysnmp.hlapi import *
import sys


def walk(host, oid):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(),
                                                                        CommunityData('public'),
                                                                        UdpTransportTarget((host, 161)),
                                                                        ContextData(),
                                                                        ObjectType(ObjectIdentity(oid)),
                                                                        lexicographicMode=False):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'),
                  file=sys.stderr)
            break
        else:
            for varBind in varBinds:
                # print(varBind)
                return varBind


Useless: str
Value01: str
Value02: str

if len(sys.argv) == 2:
    ipaddress = sys.argv[1]
    # sysDescr
    (Useless, Valore_1) = str(walk(ipaddress, '1.3.6.1.2.1.1.1')).split(' = ')

    # sysUpTime
    (Useless, Valore_2) = str(walk(ipaddress, '1.3.6.1.2.1.1.3')).split(' = ')
    # print(ipaddress)
    print("Uptime: " + str(int(Valore_2) / 100) + " Secondi")

    # Scrive tutto (invertire nella funzione il commento da print a return).
    # print(str(walk('ipaddress', '1.3.6.1.2.1.1.1')))
