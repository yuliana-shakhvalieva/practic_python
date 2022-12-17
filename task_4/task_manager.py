class Task:
    def __init__(self, id, name, description, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'id: {self.__id}\nname: {self.__name}\ndescription: {self.__description}\nstatus: {self.status}'


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id

    def __str__(self):
        return super().__str__() + f'\nparent_id: {self.parent_id}'


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks

    def __str__(self):
        result = ''
        for subtask in self.subtasks:
            result += f'\n{subtask}'
        return super().__str__() + result


class TaskManager:
    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description, status):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description, status)
        self.tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, status, parent_id):
        current_id = self.__get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, status, parent_id)
        self.subtasks[current_id] = new_subtask
        return new_subtask

    def create_complex_task(self, name, description, status, subtasks):
        current_id = self.__get_and_increment_id()
        new_complex_task = ComplexTask(current_id, name, description, status, subtasks)
        self.complex_tasks[current_id] = new_complex_task
        return new_complex_task

    def get_tasks(self):
        for key, value in self.tasks.items():
            print(f'{value}\n')

    def get_subtasks(self):
        for key, value in self.subtasks.items():
            print(f'{value}\n')

    def get_complex_tasks(self):
        for key, value in self.complex_tasks.items():
            print(f'{value}\n')

    def get_tasks_by_id(self, id):
        print(self.tasks[id])

    def get_subtasks_by_id(self, id):
        print(self.subtasks[id])

    def get_complex_tasks_by_id(self, id):
        print(self.complex_tasks[id])

    def remove_tasks(self):
        self.tasks = {}

    def remove_subtasks(self):
        self.subtasks = {}

    def remove_complex_tasks(self):
        self.complex_tasks = {}

    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        self.subtasks.pop(id)

    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id)

    def update_status(self, id, new_status):
        self.tasks[id].status = new_status

