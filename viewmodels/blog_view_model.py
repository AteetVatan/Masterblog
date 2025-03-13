"""Module for Blog Business logic (handles new blog addition)"""
import itertools
import os

import config
from helpers import PrintHelper, JsonFileHelper
from models import BlogModel


class BlogViewModel:
    """# Business logic (handles new blog addition)"""
    def __init__(self):
        self.__blog_items = []
        self.id_counter = itertools.count(start=1)
        self.init_existing_blog()


    @property
    def blog_items(self):
        return self.__blog_items


    def add_blog_item(self, blog: BlogModel):
        self.__blog_items.append(blog)

    # REGION: Create
    def add_blog(self, title, author, content, notes=""):
        blog_id = next(self.id_counter)
        blog = BlogModel(blog_id, title, author, content, notes)
        self.add_blog_item(blog)

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
