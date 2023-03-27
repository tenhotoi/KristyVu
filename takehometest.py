def remove_dup(a):
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1
    return a

def solution (config_file, port_mappings):
    a = []
    b = []
    headerconfig_file = []
    headerport_mappings = []
    temp = []

    # looking for header locations in lists
    for l1 in config_file:
        if (l1.count('__')):
            headerconfig_file.append(config_file.index(l1))

    for l2 in port_mappings:
        if (l2.count('__')):
            headerport_mappings.append(port_mappings.index(l2))

    print(headerconfig_file)
    print(headerport_mappings)

    for l1 in config_file[headerconfig_file[0]:headerconfig_file[1]]:
        # print(l1)
        if l1.count(':') == 1:
            temp1 = l1.split(":")
            for l2 in port_mappings[headerport_mappings[0]:headerport_mappings[1]]:
                if l2.count(':') == 1:
                    temp2 = l2.split(":")
                    if temp2[0] == temp1[0]:
                        a.append(temp2[1]+':'+temp1[1])
                else:
                    a.append(l2)
        else:
            a.append(l1)

    i = 0              
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1

    # for line in a:
    #    print(line)

    for l1 in config_file[headerconfig_file[1]:]:
        # print(l1)
        if l1.count(':') == 1:
            temp1 = l1.split(":")
            for l2 in port_mappings[headerport_mappings[1]:]:
                if l2.count(':') == 1:
                    temp2 = l2.split(":")
                    if temp2[0] == temp1[0]:
                        b.append(temp2[1]+':'+temp1[1])
                else:
                    b.append(l2)
        else:
            b.append(l1)

    i = 0                
    while i < len(b):
        j = i + 1
        while j < len(b):
            if b[i] == b[j]:
                del b[j]
            else:
                j += 1
        i += 1

    # for line in b:
    #    print(line)

    for line in a + b:
        print(line)    

    # Converting string into dictionary
    # using dict comprehension
    res1 = dict(item.split(":") for item in config_file if item.count(':') == 1)
    res2 = dict(item.split(":") for item in port_mappings if item.count(':') == 1)
 
    # Printing resultant string
    # print("Resultant dictionary from a: ", str(res1))
    # print("Resultant dictionary from b: ", str(res2))

    return [a + b]

config_file = [
"__10.1.1.1|10.2.2.2__",
"portA:enabled=true",
"portB:vlan=10",
"portC:vlan=200",
"__10.3.3.3__",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15"
]

port_mappings = [
"__10.1.1.1|10.2.2.2__",
"portA:member1_port3",
"portB:member2_port27",
"portC:member1_port14",
"portB:port15"
"__10.3.3.3__",
"portA:port4",
"portB:port15"
]



sol = solution(config_file, port_mappings)

print("\n CONFIG FILE IS: \n", config_file)
print("\n PORT MAPPINGS IS: \n", port_mappings)
print("\n\nFINAL OUTPUT IS: \n", sol)

"""
print("Combine 2 lists: ")
for row in list(dict.fromkeys(config_file + port_mappings)):
    print(row)
"""

