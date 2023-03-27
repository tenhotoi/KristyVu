def solution (config_file, port_mappings):
    b = []
    headerconfig_file = []
    headerport_mappings = []
    # temp = []

    # looking for header locations in config_file, and store their indexes
    for l1 in config_file:
        if (l1.count('__')):
            headerconfig_file.append(config_file.index(l1))

    # looking for header locations in port_mappings, and store their indexes
    for l2 in port_mappings:
        if (l2.count('__')):
            headerport_mappings.append(port_mappings.index(l2))

    # WARNING: config_file has more headers than port_mapping
    if len(headerconfig_file) > len(headerport_mappings):
        return ["invalid_arguments_given"]

    # assuming both config_file and port_mapping have same number of headers
    # and their headers are at the same order in the arrays
    # for each header in config_file:
    for tmp in range(1, len(headerconfig_file)): 
        a = []
        l1 = []
        l2 = []
        # for each corresponding port information of current header in config_file
        for l1 in config_file[headerconfig_file[tmp - 1]:headerconfig_file[tmp]]:     
            # dealing with port infomation in config_file     
            if l1.count(':') == 1:
                found = 0
                temp1 = l1.split(":")
                # for each corresponding port information of current header in port_mappings
                for l2 in port_mappings[headerport_mappings[tmp - 1]:headerport_mappings[tmp]]:
                    # dealing with port infomation in port_mappings
                    if l2.count(':') == 1:
                        temp2 = l2.split(":")
                        port = temp2[1]
                        # checking if port in port_mapping is in right format
                        if currentheader.count('|') and port.count('_') == 0:
                            # WARNING: Port in port_mapping is not in the right format.  For ', currentheader, ', ports are expected to be in <source>_<destination> format.'
                            return ["invalid_arguments_given"]
                        # mapping ports, and append to array a
                        if temp2[0] == temp1[0]:
                            a.append(port+':'+temp1[1])
                            found = 1
                    elif l2.count('__'):
                        a.append(l2)
                        currentheader = l2
                    else:
                        # WARNING: the strings in port_mappings have to be in the right format: including '__' for header, ':' for others.
                        return ["invalid_arguments_given"]
                if found == 0:
                    # WARNING: can't find port in port_mappings 
                    return ["invalid_arguments_given"]
            elif l1.count('__'):
                a.append(l1)
            else:
                # WARNING: the strings in config_file have to be in the right format: including '__' for header, ':' for others.
                return ["invalid_arguments_given"]

        # remove duplicates in array a
        a = list(dict.fromkeys(a))  
    
        b = b + a

    # dealing with the last header
    # print("\n CHECK AGAIN, tmp currently is: ", tmp)
    # print(config_file[headerconfig_file[tmp]:])
    a = []
    l1 = []
    l2 = []
    # for each corresponding port information of the last header in config_file
    for l1 in config_file[headerconfig_file[tmp]:]:        
        if l1.count(':') == 1:
            found = 0
            temp1 = l1.split(":")
            # for each corresponding port information of the last header in port_mappings
            for l2 in port_mappings[headerport_mappings[tmp]:]:
                if l2.count(':') == 1:
                    temp2 = l2.split(":")
                    port = temp2[1]
                    # checking if port in port_mapping is in right format
                    if currentheader.count('|') and port.count('_') == 0:
                        # WARNING: Port in port_mapping is not in the right format.  For ', currentheader, ', ports are expected to be in <source>_<destination> format.'
                        return ["invalid_arguments_given"]
                    if temp2[0] == temp1[0]:
                        a.append(port+':'+temp1[1])
                        found = 1
                elif l2.count('__'):
                    a.append(l2)
                else:
                    # WARNING: the string have to be in the right format: including '__' for header, ':' for others.
                    return ["invalid_arguments_given"]
            if found == 0:
                # WARNING: can't find port in port_mapping.
                return ["invalid_arguments_given"]
        elif l1.count('__'):
            a.append(l1)
            currentheader = l1
        else:
            # WARNING: the string have to be in the right format: including '__' for header, ':' for others.
            return ["invalid_arguments_given"]

    # remove duplicates in array a
    a = list(dict.fromkeys(a))

    b = b + a
    return b

config_file = [
"__10.1.1.1|10.2.2.2__",
"portA:enabled=true",
"portB:vlan=10",
"portC:vlan=200",
"__10.3.3.3__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15",
"__10.3.3.4__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15",
"__Switch1A|Switch1B__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15"
]

port_mappings = [
"__10.1.1.1|10.2.2.2__",
"portA:member1_port3",
"portB:member2_port27",
"portC:member1_port14",
"__10.3.3.3__",
"portA:port4",
"portB:port15",
"__10.3.3.4__",
"portA:port4",
"portB:port15",
"__Switch1A|Switch1B__",
"portA:member2_port30",
"portB:member1_port270",
"portC:member2_port140"
]

sol = solution(config_file, port_mappings)

print("\n CONFIG FILE IS: \n", config_file)
print("\n PORT MAPPINGS IS: \n", port_mappings)
print("\n\nFINAL OUTPUT IS: \n \n", sol)
print ("\n", type(sol))
for line in sol:
        print(line) 
        # print(type(line))

# https://documentation.meraki.com/MX/NAT_and_Port_Forwarding/Troubleshooting_Port_Forwarding_and_NAT_Rules

# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU
import time
for i in range(5):
    start = time.time()
    for i in range(1000):
        mergeArray = solution(config_file, port_mappings)
    timetaken = time.time() - start
    print("Time taken: ", timetaken)

def timetrials(trials = 10):
    totaltime = 0
    #start = time.time()
    for i in range(trials):
        start = time.time() # it should be here
        for i in range(1000):
            mergeArray = solution(config_file, port_mappings)        
        totaltime += time.time() - start
    print("average =%10.7f " % (totaltime/trials))

timetrials()