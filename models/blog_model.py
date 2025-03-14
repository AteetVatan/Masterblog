"""Module for Blog Model."""
import inspect
from typing import Optional


class BlogModel:
    """Class for Blog Data structure."""
    __blog_id: int
    __author: str
    __title: str
    __content: str
    __notes: Optional[str] = None
    __likes: int = 0

    def __init__(self,
                 blog_id,
                 author,
                 title,
                 content,
                 notes="",
                 likes=0):
        self.blog_id = blog_id
        self.author = author
        self.title = title
        self.content = content
        self.notes = notes
        self.likes = likes

    @property
    def blog_id(self):
        """The Unique Blog Id property getter."""
        return self.__blog_id

    @blog_id.setter
    def blog_id(self, val):
        """The Unique Blog Id property setter."""
        if not isinstance(val, int) or val <= 0:
            raise ValueError("ID must be a positive integer.")
        self.__blog_id = val

    @property
    def author(self):
        """The Blog author property getter."""
        return self.__author

    @author.setter
    def author(self, val):
        """The Blog author property setter."""
        val = val.strip()
        if not val:
            raise ValueError("Author name cannot be empty.")
        self.__author = val

    @property
    def title(self):
        """The Blog title property getter."""
        return self.__title

    @title.setter
    def title(self, val):
        """The Blog title property setter."""
        val = val.strip()
        if not val:
            raise ValueError("Title cannot be empty.")
        self.__title = val

    @property
    def content(self):
        """The Blog content property getter."""
        return self.__content

    @content.setter
    def content(self, val):
        """The Blog content property setter."""
        if not val.strip():
            raise ValueError("Content cannot be empty.")
        self.__content = val

    @property
    def notes(self):
        """The Blog notes property getter."""
        return self.__notes

    @notes.setter
    def notes(self, val):
        """The Blog notes property setter."""
        self.__notes = val

    @property
    def likes(self):
        """The Blog notes property getter."""
        return self.__likes

    @likes.setter
    def likes(self, val):
        """The Blog notes property setter."""
        if  not isinstance(val,(int,float)):
            raise ValueError("Blog likes should be a number")
        self.__likes = int(val)

    @classmethod
    def get_class_properties(cls):
        """Returns a list of property names in a class."""
        return [name for name, attr in inspect.getmembers(cls, lambda x: isinstance(x, property))]
