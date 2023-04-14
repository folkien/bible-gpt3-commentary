'''
    Dataclass of posts database in directory 'database' with
    every post named with date.
'''
from dataclasses import asdict, dataclass, field
import dataclasses
from datetime import date, timedelta
import datetime
import json
import os

from models.Post import Post


class EnhancedJSONEncoder(json.JSONEncoder):
    '''Enhanced JSON encoder with dataclasses support.'''

    def default(self, o):
        ''' Method to default dataclass.'''
        # Set : Json
        if (isinstance(o, (set))):
            return list(o)

        # Dataclass : Json.
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)

        # Datetime : Json
        if (isinstance(o, (datetime, date))):
            return o.isoformat()

        # Timedelta : Json
        if (isinstance(o, timedelta)):
            return str(o.total_seconds())

        return super().default(o)


@dataclass
class PostDatabase:
    ''' Dataclass of posts database in directory 'database' with
        every post named with date. '''
    path: str = 'database'

    def __post_init__(self):
        ''' Post init. '''
        # Check if path exists
        if (not os.path.exists(self.path)):
            # Create path
            os.makedirs(self.path)

    def __createdPostName(self, date: date) -> str:
        ''' Get created post filename. '''
        return f'Created{date}.json'

    def __postedPostName(self, date: date) -> str:
        ''' Get posted post filename. '''
        return f'Posted{date}.json'

    def IsCreated(self, date: date) -> bool:
        ''' Get post by date. '''
        # Created post filename
        createdPostPath = os.path.join(self.path, self.__createdPostName(date))
        # Posted post filename
        postedPostPath = os.path.join(self.path, self.__postedPostName(date))

        return os.path.exists(createdPostPath) or os.path.exists(postedPostPath)

    def IsPosted(self, date: date) -> bool:
        ''' Get post by date. '''
        # Posted post filename
        postedPostPath = os.path.join(self.path, self.__postedPostName(date))
        return os.path.exists(postedPostPath)

    def GetPost(self, date: date) -> Post:
        ''' Get post by date. '''
        # Get file path
        filePath = os.path.join(self.path, self.__createdPostName(date))

        # Check if file exists
        if (not os.path.exists(filePath)):
            # Return None
            return None

        # Load file
        with open(filePath, 'r') as fileObject:
            # Load json
            data = json.load(fileObject)

        # Return post
        return Post(**data)

    def AddCreated(self, post: Post) -> bool:
        ''' Save post. '''
        # Get file path
        filePath = os.path.join(self.path, self.__createdPostName(post.date))

        # Save file
        with open(filePath, 'w') as fileObject:
            json.dump(asdict(post), fileObject,
                      indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder)

        # Return success
        return True

    def AddPosted(self, post: Post) -> bool:
        ''' Save post. '''
        # Get file path
        filePath = os.path.join(self.path, self.__postedPostName(post.date))

        # Save file
        with open(filePath, 'w') as fileObject:
            # Dump post as json
            json.dump(asdict(post), fileObject, indent=4,
                      ensure_ascii=False,  cls=EnhancedJSONEncoder)

        # Return success
        return True
