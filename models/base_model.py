#!/usr/bin/python3

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        timeForm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if len(kwargs) != 0:
        	for i, v in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def dictionary (self):
        """Return dictionary representation of BaseModel"""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = type(self).__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

