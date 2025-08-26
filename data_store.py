class DataStore:

    def __init__(self, *args):
        self._cover = args[0]
        self._num = args[1]
        self._revision = args[2]
        self._created_time = args[3]
        self._revised_time = args[4]
        self._title = args[5]
        self._file_name = args[6]
        
    @property
    def cover(self):
        return self._cover
    
    @property
    def number(self):
        return self._num
    
    @property
    def revision(self):
        return self._revision
    
    @property
    def created(self):
        return self._created_time
    
    @property
    def revised(self):
        return self._revised_time
    
    @property
    def title(self):
        return self._title
    
    @property
    def file(self):
        return self._file_name

    


