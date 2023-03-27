import unittest
from takehome_solution import solution1, solution2
from hashtable_takehomesolution import solution3
from dictionarytesting2 import testingStr
from listStackQueue import ListQueue

class TestSolution(unittest.TestCase):
    def testing_solution1(self):
        config_file = ["1","2","3"]
        port_mappings = ["4","5","6"]
        mergeArray = solution1(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['invalid_arguments_given'])

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
        mergeArray = solution1(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['__10.1.1.1|10.2.2.2__', 'member1_port3:enabled=true', 'member2_port27:vlan=10', 'member1_port14:vlan=200', '__10.3.3.4__', 'port40:enabled=true', 'port40:poe=false', 'port40:speed=100mbps', 'port150:vlan=15', '__10.3.3.3__', 'port4:enabled=true', 'port4:poe=false', 'port4:speed=100mbps', 'port15:vlan=15', '__Switch1A|Switch1B__', 'member2_port30:enabled=true', 'member2_port30:poe=false', 'member2_port30:speed=100mbps', 'member1_port270:vlan=15'])

    def testing_solution2(self):
        config_file = ["1","2","3"]
        port_mappings = ["4","5","6"]
        mergeArray = solution2(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['invalid_arguments_given'])

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
        mergeArray = solution2(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['__10.1.1.1|10.2.2.2__', 'member1_port3:enabled=true', 'member2_port27:vlan=10', 'member1_port14:vlan=200', '__10.3.3.4__', 'port40:enabled=true', 'port40:poe=false', 'port40:speed=100mbps', 'port150:vlan=15', '__10.3.3.3__', 'port4:enabled=true', 'port4:poe=false', 'port4:speed=100mbps', 'port15:vlan=15', '__Switch1A|Switch1B__', 'member2_port30:enabled=true', 'member2_port30:poe=false', 'member2_port30:speed=100mbps', 'member1_port270:vlan=15'])

    def testing_solution3(self):
        config_file = ["1","2","3"]
        port_mappings = ["4","5","6"]
        mergeArray = solution3(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['invalid_arguments_given'])

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
        mergeArray = solution3(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['__10.1.1.1|10.2.2.2__', 'member1_port3:enabled=true', 'member2_port27:vlan=10', 'member1_port14:vlan=200', '__10.3.3.4__', 'port40:enabled=true', 'port40:poe=false', 'port40:speed=100mbps', 'port150:vlan=15', '__10.3.3.3__', 'port4:enabled=true', 'port4:poe=false', 'port4:speed=100mbps', 'port15:vlan=15', '__Switch1A|Switch1B__', 'member2_port30:enabled=true', 'member2_port30:poe=false', 'member2_port30:speed=100mbps', 'member1_port270:vlan=15'])
    
    def testing_solutionAll(self):
        config_file = ["1","2","3"]
        port_mappings = ["4","5","6"]
        mergeArray = solution3(config_file, port_mappings)
        print(mergeArray)
        self.assertEqual(mergeArray, ['invalid_arguments_given'])

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
        
        for i in range(3):
            solName = 'solution'+str(i + 1)
            mergeArray = eval(solName + '(config_file, port_mappings)')
            print('FINAL mergeArrya for {} IN SOLUTION ALL: {}'.format(solName, mergeArray))
            self.assertEqual(mergeArray, ['__10.1.1.1|10.2.2.2__', 'member1_port3:enabled=true', 'member2_port27:vlan=10', 'member1_port14:vlan=200', '__10.3.3.4__', 'port40:enabled=true', 'port40:poe=false', 'port40:speed=100mbps', 'port150:vlan=15', '__10.3.3.3__', 'port4:enabled=true', 'port4:poe=false', 'port4:speed=100mbps', 'port15:vlan=15', '__Switch1A|Switch1B__', 'member2_port30:enabled=true', 'member2_port30:poe=false', 'member2_port30:speed=100mbps', 'member1_port270:vlan=15'])

    def testing_string(self):
        testingStr()
"""
class TestListQueue(unittest.TestCase):
    def testinit(self):
        q = ListQueue()
    def testaddandremoveoneitem(self):
        q = ListQueue()
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 3)
    def testalternatingaddremove(self):
        q = ListQueue()
        for i in range(1000):
            q.enqueue(i)
            self.assertEqual(q.dequeue(), i)
    def testmanyoperations(self):
        q = ListQueue()
        for i in range(10):
            q.enqueue(2 * i + 3)
        for i in range(10):
            self.assertEqual(q.dequeue(), 2 * i + 3)
    def testlength(self):
        q = ListQueue()
        self.assertEqual(len(q), 0)
        for i in range(10):
            q.enqueue(i)
            self.assertEqual(len(q), 10)
        for i in range(10):
            q.enqueue(i)
            self.assertEqual(len(q), 20)
        for i in range(15):
            q.dequeue()
            self.assertEqual(len(q), 5)
"""

if __name__ == '__main__':
    unittest.main()
