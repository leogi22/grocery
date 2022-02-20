
import sys
from reg import TRAINING_PROCEEDING_TIME, TRIGGER_TIME, Register
from customer import CustomerA, Customer, CustomerB
import customer_queue
import pandas as pd

'''Register_manager is the main class responsible for creating the other classes and runnig the main algo'''

class Register_manager:
    def __init__(self):
        self.register_count = 0
        self.register_list = []

    def create_registers(self, filename):
        # create registers
        lines = pd.read_csv(filename, nrows=1, header=None, sep=' ')
        self.register_count = int(lines.iloc[0].iloc[0])
        for _ in range(self.register_count - 1):
            self.register_list.append(Register())
        self.register_list.append(Register(TRAINING_PROCEEDING_TIME))

    def process_input(self, filename):
        total_time = 0
        actions = pd.read_csv(filename, index_col=False, skiprows=1, header=None, sep=' ')
        actions.columns = ['type', 'time', 'items']
        actions.sort_values(['time', 'items', 'type'], inplace=True)

        for idx, action in actions.iterrows():
            # tell the registers to do some work
            for reg in self.register_list:
                reg.process(int(action['time']))

            if action['type'] == 'A': c = CustomerA(action['time'], action['items'])
            else:                     c = CustomerB(action['time'], action['items'])
            c.choose_register(self.register_list)

        for reg in self.register_list:
            reg_time = reg.process(TRIGGER_TIME)
            total_time = max(total_time, reg_time)

        return total_time


if __name__ == "__main__":
    register_manager = Register_manager()
    if len(sys.argv) != 2:
        print("please provide an input file name")
        exit(-1)
    register_manager.create_registers(sys.argv[1])
    t = register_manager.process_input(sys.argv[1])
    print(f"Finished at: t={t} minutes")
