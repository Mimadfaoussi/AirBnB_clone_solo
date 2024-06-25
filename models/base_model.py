#!/usr/bin/python3
""" BaseModel module """ 


class BaseModel:
    """ define all common attributes for other classes """ 
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance , this represent the constructor 
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of an instance
        """
        return ('[{}] [{}] [{}]'.format(self.__class__))

    def save(self):
        """ 
        Update : updated at a certain time 
        """
        self.updated_at = datetime.now()

