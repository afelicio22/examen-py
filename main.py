
import time
import datetime


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():

    name = None
    priority = -1
    period = -1
    execution_time = -1
    next_ready_time = -1
    state = "SLEEPING"

        ############################################################################
    def __init__(self, name, priority, period, execution_time, oilfill, oilconsume):

        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time
        self.next_ready_time = datetime.datetime.now()
        self.state = "WAITING"
        self.oilfill = oilfill
        self.oilconsume = oilconsume

    	############################################################################
    def update_state(self):
        
        if self.next_ready_time < datetime.datetime.now() :
            
            current_task.state = "WAITING"

        print("\t" + self.name + " : " + self.state + "\t(Deadline = " + self.next_ready_time.strftime("%H:%M:%S") + ", Priority = " + str(self.priority) + ")")


    	############################################################################
    def run(self):

        # Update execution_time
        self.next_ready_time  += datetime.timedelta(seconds=self.period)

        # Start task
        print("\t" + self.name + " : Starting (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
        
        self.state = "RUNNING"
        
        time.sleep(self.execution_time)

        # Stop task
        print("\t" + self.name + " : Ending (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
        
        self.state = "WAITING"

    def tank(self):
        tankMax = 50
        tankValue = 0 
        if(self.oilconsume > 0) & (tankValue == 0):
            print("No oil")
            self.state = "BLOCKED" 
        elif(self.oilfill > 0) & (tankMax == 50):
            print("Tank already full")
            self.state = "BLOCKED" 
        else:
            self.state = "OK"
        


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

	# Instanciation of task objects
    task_list = []
    task_list.append(my_task(name="pump_1", priority = 1, period = 5, execution_time = 2, oilfill=10, oilconsume=0))
    task_list.append(my_task(name="pump_2", priority = 3, period = 15, execution_time = 3, oilfill=20, oilconsume=0))
    task_list.append(my_task(name="machine_1", priority = 4, period = 5, execution_time = 5, oilfill=0, oilconsume=25))
    task_list.append(my_task(name="machine_2", priority = 2, period = 5, execution_time = 3, oilfill=0, oilconsume=5))

    while(1):

        time_now = datetime.datetime.now()
		
        print("\nScheduler : " + time_now.strftime("%H:%M:%S"))


		# Update task state : SLEEPING => READY
        for current_task in task_list:
				
            current_task.update_state()



		# Search for task with higher priority
        task_to_run = None
        task_higher_priority = 0

        for current_task in task_list:
		
            if (current_task.state == "WAITING") & (current_task.priority > task_higher_priority) :
			
                task_higher_priority = current_task.priority
                task_to_run = current_task
                if(current_task.tank() == "OK"):

                        # Start task
                    if task_to_run == None :
                        time.sleep(5)

                    else :
                        task_to_run.run()


