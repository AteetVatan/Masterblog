import os
from typing import Dict

from models.blog_model import BlogModel
import itertools
import config
from helpers import JsonFileHelper, PrintHelper


class BlogsModel:
    __blog_items: Dict[int, BlogModel]

    def __init__(self, blog_file=""):
        self.__blog_items = dict()
        self.id_counter = itertools.count(start=1)
        self.init_existing_blog()

    @property
    def blog_id(self):
        return self.__id

    @property
    def blog_items(self):
        return self.__blog_items

    @blog_items.setter
    def blog_items(self, val: BlogModel):
        self.__blog_items.update({val.id, val})

    # REGION: Create
    def init_existing_blog(self):
        # read existing blog json if exists

        file_path = config.DEFAULT_BLOG_FILE_PATH
        if os.path.exists(file_path):
            try:
                # read the default blog
                blog_list = JsonFileHelper.read_data(file_path)

                # Ensure blog_list is a list
                if not isinstance(blog_list, list):
                    raise ValueError("Invalid blog data format. Expected a list of dictionaries.")

                # Get valid keys dynamically
                valid_keys = BlogModel.get_class_properties()

                # blog_objects = []
                # for blog_item in blog_list:
                #     blog_objects.append(Blog(**{k:v for k,v in blog_item.items() if k in valid_keys}))

                blog_objects = [BlogModel(**{k: v for k, v in blog_item.items() if k in valid_keys})
                                for blog_item in blog_list]

                self.__blog_items = blog_objects
                max_id_count = max(blog.id for blog in self.__blog_items) + 1
                self.id_counter = itertools.count(start=max_id_count)  # set the unique ID counter
            except ValueError as e:
                PrintHelper.pr_error(e.args[0])
            except (FileNotFoundError, IOError) as f:
                PrintHelper.pr_error(f)
        else:
            PrintHelper.pr_menu("No existing blog file found. Initializing empty blog list.")

        if not self.__blog_items:
            self.__blog_items = []
            self.id_counter = itertools.count(start=1)

    def add(self, author: str, title: str, content: str, notes: str = None):
        try:
            blog_id = next(self.id_counter)  # id must be unique
            blog = BlogModel(blog_id,
                             author=author,
                             title=title,
                             content=content,
                             notes=notes)
            self.__blog_items.update({blog_id, blog})
        except ValueError as e:
            PrintHelper.pr_error(e.args[0])

    # END REGION

    # REGION: Read

    # END REGION

    # REGION: Update

    # END REGION

    # REGION: Delete

    # END REGION
