class todo_validate:
    def __init__(self, name, completed):
        self._name = name
        self._completed = completed
        self.errors = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def completed(self):
        return self.completed
    
    @completed.setter
    def completed(self, value):
        self._completed = value