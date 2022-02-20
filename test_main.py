import pytest
import os
import sys

if os.getcwd() not in sys.path:
    sys.path.insert(0,os.getcwd())
from register_manager import Register_manager
from reg import Register, TRAINING_PROCEEDING_TIME, TRIGGER_TIME
from customer import Customer, CustomerA, CustomerB

def test_A_customers_only():
    register_manager = Register_manager()
    register_manager.create_registers('tests/test_A_customers_only.txt')
    t = register_manager.process_input('tests/test_A_customers_only.txt')

    assert t == 7

def test_A_and_B_customers():
    register_manager = Register_manager()
    register_manager.create_registers('tests/test_A_and_B_customers.txt')
    t = register_manager.process_input('tests/test_A_and_B_customers.txt')

    assert t == 13

def test_A_only_same_time():
    register_manager = Register_manager()
    register_manager.create_registers('tests/test_A_only_same_time.txt')
    t = register_manager.process_input('tests/test_A_only_same_time.txt')

    assert t == 6

def test_A_only_same_time_last():
    register_manager = Register_manager()
    register_manager.create_registers('tests/test_A_only_same_time_last.txt')
    t = register_manager.process_input('tests/test_A_only_same_time_last.txt')

    assert t == 9

def test_A_and_B_customers_same_time():
    register_manager = Register_manager()
    register_manager.create_registers('tests/test_A_and_B_customers_same_time.txt')
    t = register_manager.process_input('tests/test_A_and_B_customers_same_time.txt')

    assert t == 11






