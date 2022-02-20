from customer_queue import queue

REGULAR=1
TRAINING=2
NORMAL_PROCEEDING_TIME=1
TRAINING_PROCEEDING_TIME=2
TRIGGER_TIME=999999

''' this defines the register class that is responsible for processing the customers and managing 
 its customer queue '''

class Register:
    def __init__(self, type=REGULAR):
        self.type = type
        self.time_to_proceed_1_item = NORMAL_PROCEEDING_TIME if type==REGULAR else TRAINING_PROCEEDING_TIME
        self.queue = queue(max_size = 50)
        self.current_customer_start_time = 0
        self.current_customer_serviced = None
        self.register_idle_time = 0

    def process(self, time):
        if self.current_customer_serviced == None and self.queue.isEmpty():
            return
        if self.current_customer_serviced != None:
            if time >= self.register_idle_time + self.time_to_proceed_1_item*self.current_customer_serviced.items:
                # enough time to proceed
                self.register_idle_time += self.time_to_proceed_1_item*self.current_customer_serviced.items
                self.current_customer_serviced = None
                self.queue.dequeue()
        if self.current_customer_serviced == None:
            # we're here because time was sufficient to process current customer or there were no customer being taken care of at that time
            while self.queue.isEmpty() == False:
                self.current_customer_serviced = self.queue.queue[self.queue.front]

                if self.register_idle_time < self.current_customer_serviced.time:
                    self.register_idle_time = self.current_customer_serviced.time  # update our idle_time with queue_time
                if time >= self.register_idle_time + self.time_to_proceed_1_item * self.current_customer_serviced.items:
                    # do we have time to process this new one?
                    self.register_idle_time += self.time_to_proceed_1_item * self.current_customer_serviced.items
                    self.queue.dequeue()
                else:
                    break

        return(self.register_idle_time)
