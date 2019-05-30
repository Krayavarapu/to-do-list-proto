class ToDoList:
    my_list = []
    def __init__():
        #my_list = []
        flag = False

    def add_to_list(self, task):
        self.my_list.append(task)
        return

    def completed_task(self):
        my_list.pop(0)

    def display_tasks(self):
        i = 0
        while i < len(my_list):
            print(my_list[i])
            i = i + 1
    


def main():
    num_task = input("How many tasks?")

    i = 0
    while i < int(num_task):
        task = input("Enter a task")
        add_to_list(task)
        i = i + 1
    
    display_tasks()
    completed_task()
    display_tasks()

if __name__ == "__main__":
    main()
        
    