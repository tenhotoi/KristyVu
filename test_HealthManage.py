import os
import unittest 
from unittest import mock
from unittest import TestCase
import HealthManagementSystem

class TestHealthManagement(unittest.TestCase):
    @mock.patch('HealthManagementSystem.input', create=True)
    def testing_healthManagement_case1(self, mocked_input):
        try:
            os.remove('KristyFood.txt')
            os.remove('KristyExercise.txt')
        except IOError as io:
            print(io)

        manage = HealthManagementSystem.HealthManagement()
        mocked_input.side_effect = ['Kristy', 3, 2, 2, 3, 1, 1, 'dkdkdk', 3, 2, 1, 3, 1, 2, 'cncncncn', 3, 3]
        # mocked_input.side_effect = ['Kristy', 3, 2, 2]
        manage.addname()  
        namevar = manage.selectname()
        file_action = manage.select_file_action()
        task = manage.select_task()
        result1 = manage.action(namevar, file_action, task)
        self.assertEqual('No such file or directory' in result1, True)

    # @mock.patch('HealthManagementSystem.input', create=True)
    # def testing_healthManagement_case2(self, mocked_input): 
        # manage = HealthManagementSystem.HealthManagement()
        mocked_input.side_effect = [3, 1, 1, 'dkdkdk']
        namevar = manage.selectname()
        file_action = manage.select_file_action()
        task = manage.select_task()
        result2 = manage.action(namevar, file_action, task)
        self.assertEqual(result2, "Successfully written.")

    # @mock.patch('HealthManagementSystem.input', create=True)
    # def testing_healthManagement_case3(self, mocked_input): 
        # manage = HealthManagementSystem.HealthManagement()
        mocked_input.side_effect = [3, 2, 1]
        namevar = manage.selectname()
        file_action = manage.select_file_action()
        task = manage.select_task()
        result3 = manage.action(namevar, file_action, task)
        self.assertEqual(result3, "Succesfully read file.")

    # @mock.patch('HealthManagementSystem.input', create=True)
    # def testing_healthManagement_case4(self, mocked_input): 
        # manage = HealthManagementSystem.HealthManagement()
        mocked_input.side_effect = [3, 1, 2, 'cncncncn']
        namevar = manage.selectname()
        file_action = manage.select_file_action()
        task = manage.select_task()
        result4 = manage.action(namevar, file_action, task)
        self.assertEqual(result4, "Successfully written.")  

    # @mock.patch('HealthManagementSystem.input', create=True)
    # def testing_healthManagement_case5(self, mocked_input): 
        # manage = HealthManagementSystem.HealthManagement()
        mocked_input.side_effect = [3, 3]
        namevar = manage.selectname()
        # file_action = manage.select_file_action()
        with self.assertRaises(SystemExit) as cm:
            file_action = manage.select_file_action()
        self.assertEqual(cm.exception.code, 'Invalid entry.')
        # task = manage.select_task()
        # result5 = manage.action(namevar, file_action, task)               

        
        
        
        


if __name__ == '__main__':
    unittest.main()