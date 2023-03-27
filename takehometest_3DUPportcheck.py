def solution (config_file, port_mappings):
    b = []
    headerconfig_file = []
    headerport_mappings = []
    temp = []

    # return with error if duplicate port is found

    # looking for header locations in lists
    for l1 in config_file:
        if (l1.count('__')):
            headerconfig_file.append(config_file.index(l1))

    for l2 in port_mappings:
        if (l2.count('__')):
            headerport_mappings.append(port_mappings.index(l2))

    # print(headerconfig_file)
    # print(headerport_mappings)

    if len(headerconfig_file) != len(headerport_mappings):
        print("WARNING: config_file and port_mapping don't have the same number of headers.")
        return ["invalid_arguments_given"]

    # assuming both config_file and port_mapping have same number of headers
    # and their headers are at the same order in the arrays
    for tmp in range(1, len(headerconfig_file)): 
        a = []
        l1 = []
        l2 = []
        for l1 in config_file[headerconfig_file[tmp - 1]:headerconfig_file[tmp]]:           
            if l1.count(':') == 1:
                found = 0
                temp1 = l1.split(":")
                for l2 in port_mappings[headerport_mappings[tmp - 1]:headerport_mappings[tmp]]:
                    if l2.count(':') == 1:
                        temp2 = l2.split(":")
                        port = temp2[1]
                        # looking for and return error if duplicate ports found in port_mapping (only need to check once in the whole scripts)
                        dup = [s for s in port_mappings if port in s and s.endswith(port)]
                        if len(dup) > 1:
                            print('WARNING: In port_mapping, duplicated ports found!')
                            print(dup)
                            return ["invalid_arguments_given"]
                        # checking if port in port_mapping is in right format
                        if currentheader.count('|'):
                            if port.count('_'):
                                temp3 = port.split("_")
                                port2 = temp3[1]
                                # looking for and return error if duplicate ports found in port_mapping (only need to check once in the whole scripts)
                                dup2 = [s for s in port_mappings if port2 in s and s.endswith(port2)]
                                if len(dup2) > 1:
                                    print('WARNING: In port_mapping, duplicated ports found!')
                                    print(port2, ' is duplicated in: ', dup2)
                                    return ["invalid_arguments_given"]
                            else:
                                print('Port in port_mapping is not in the right format.  For ', currentheader, ', ports are expected to be in <source>_<destination> format.')
                                return ["invalid_arguments_given"]

                        # mapping ports
                        if temp2[0] == temp1[0]:
                            a.append(port+':'+temp1[1])
                            found = 1
                    elif l2.count('__'):
                        a.append(l2)
                        currentheader = l2
                    else:
                        print("WARNING: the string have to be in the right format: including '__' for header, ':' for others.")
                        return ["invalid_arguments_given"]
                if found == 0:
                    print("WARNING: can't find ", temp1[0], "in port_mappings for ", currentheader)
                    return ["invalid_arguments_given"]
            elif l1.count('__'):
                a.append(l1)
            else:
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
    for l1 in config_file[headerconfig_file[tmp]:]:        
        if l1.count(':') == 1:
            found = 0
            temp1 = l1.split(":")
            # print(port_mappings[headerport_mappings[tmp]:])
            for l2 in port_mappings[headerport_mappings[tmp]:]:
                # print("temp1 is: ", temp[0])
                if l2.count(':') == 1:
                    temp2 = l2.split(":")
                    port = temp2[1]
                    # checking if port in port_mapping is in right format
                    if currentheader.count('|') and port.count('_') == 0:
                        print('Port in port_mapping is not in the right format.  For ', currentheader, ', ports are expected to be in <source>_<destination> format.')
                        print('Right now it is: ', port)
                        return ["invalid_arguments_given"]
                    if temp2[0] == temp1[0]:
                        a.append(port+':'+temp1[1])
                        found = 1
                elif l2.count('__'):
                    a.append(l2)
                else:
                    return ["invalid_arguments_given"]
            if found == 0:
                print("WARNING: can't find ", temp1[0], "in port_mapping")
                return ["invalid_arguments_given"]
        elif l1.count('__'):
            a.append(l1)
            currentheader = l1
        else:
            return ["invalid_arguments_given"]

    # remove duplicates in array a
    a = list(dict.fromkeys(a))  # Or [*dict.fromkeys(a)] if you prefer

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
        print(type(line))

testing = set(config_file) - set(port_mappings)
print('testing output is: ', testing)

headers = [x for x in config_file if x in port_mappings]
print('headers are: ', headers)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
# Output True, since, s2 elements in s1
print(s2.issubset(s1))

print(headers.issubset(config_file))
print(headers.issubset(port_mappings))