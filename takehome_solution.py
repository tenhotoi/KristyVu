def solution1(config_file, port_mappings):
    value = [] 
    dic = {}
    # Creating dictionary from port_mappings
    for item in port_mappings[::-1]:
        if item.count('__'):
            dic.update({item:value})
            value = []                   
        elif item.count(':'):
            value.append(item)
        else:
            return ["invalid_arguments_given"]

    # Merge arrays
    mergearr = []
    for each in config_file:
        if each.count('__'):
            mapvalues = dic[each]
            mergearr.append(each)
        elif each.count(':'):
            spliteach = each.split(':')
            for val in mapvalues:
                splitval = val.split(':')
                if spliteach[0] == splitval[0]:
                    mergearr.append(splitval[1]+':'+spliteach[1])
        else:
            return ["invalid_arguments_given"]
    return mergearr

def solution2(config_file, port_mappings):
    value = {}
    dic = {}
    # Creating dictionary from port_mappings
    for item in port_mappings[::-1]:
        if item.count('__'):
            dic[item] = value        
            value = {}                   
        elif item.count(':'):
            splititem = item.split(":")
            value[splititem[0]] = splititem[1]
        else:
            return ["invalid_arguments_given"]

    # Merge arrays
    mergearr = []
    for each in config_file:
        if each.count('__'):
            mapvalues = dic[each]
            mergearr.append(each)
        elif each.count(':'):
            spliteach = each.split(':')
            if mapvalues[spliteach[0]]:
                    mergearr.append(mapvalues[spliteach[0]]+':'+spliteach[1])
            else:
                return ["invalid_arguments_given"]
        else:
            return ["invalid_arguments_given"]
    
    return mergearr

if __name__ == '__main__':
    config_file = ["1","2","3"]
    port_mappings = ["4","5","6"]
    mergeArray = solution(config_file, port_mappings)
    print(mergeArray)

    port_mappings = [
        "__10.1.1.1|10.2.2.2__",
        "portA:member1_port3",
        "portB:member2_port27",
        "portC:member1_port14",
        "__10.3.3.3__",
        "portA:port4",
        "portB:port15",
        "__10.3.3.4__",
        "portA:port40",
        "portB:port150",
        "__Switch1A|Switch1B__",
        "portA:member2_port30",
        "portB:member1_port270",
        "portC:member2_port140"
        ]

    config_file = [
        "__10.1.1.1|10.2.2.2__",
        "portA:enabled=true",
        "portB:vlan=10",
        "portC:vlan=200",
        "__10.3.3.4__",
        "portA:enabled=true",
        "portA:poe=false",
        "portA:speed=100mbps",
        "portB:vlan=15",
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
    mergeArray = solution(config_file, port_mappings)
    print(mergeArray)

    # https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU
    import time
    for i in range(5):
        start = time.time()
        for i in range(1):
            mergeArray = solution(config_file, port_mappings)
        timetaken = time.time() - start
        print("Time taken: ", timetaken)

    def timetrials(trials = 1):
        totaltime = 0
        #start = time.time()
        for i in range(trials):
            start = time.time() # it should be here
            for i in range(1):
                mergeArray = solution(config_file, port_mappings)        
            totaltime += time.time() - start
        print("average =%10.7f " % (totaltime/trials))

    timetrials()

