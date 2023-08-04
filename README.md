okay, this is my first method, i used a decorator:
def insert_decorator(func):
    def wrapper(content,*arg):
        # wrap
        insert_text, task = func(content, *arg)
        # vị trí insert
        insert_index = content.find(task)

        modified_content = (
            content[:insert_index + len(task)]
            + '\n// Tool\n' + insert_text + '\n//'
            + content[insert_index + len(task):]
        )
        return modified_content
    return wrapper

class TaskInsert:
    taskName = {
        0: 'procs[] = {',
        1: 'void sycFunction();',
        2: 'SEDGe_Pre_Proc_10ms();',
        3: 'SEDGe_Pre_Proc_INI();',
    }
    @staticmethod
    @insert_decorator
    def insert_sycFunction(content, task=taskName[1]):
        insert_text = '\n'.join(run_list)
        return insert_text, task

    @staticmethod
    @insert_decorator
    def insert_execute10msTask(content, task=taskName[2]):
        insert_text = '\t'+'\n\t'.join(run_list)
        return insert_text, task

now if i switch to the 2nd method and use an interface like this:
class ICyclicTask(ABC):
    @abstractmethod
    def insert_task(self, content, task) -> str: ...
how do you think the rest of my code should be ?
