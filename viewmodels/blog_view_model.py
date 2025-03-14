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
        """Property to get all blog items."""
        return self.__blog_items

    def add_blog_item(self, blog: BlogModel):
        """Method to add blog item."""
        self.__blog_items.append(blog)

    # REGION: Create
    def add_blog(self, author, title, content, notes=""):
        """Method to add blog."""
        blog_id = next(self.id_counter)
        blog = BlogModel(blog_id=blog_id,
                         author=author,
                         title=title,
                         content=content,
                         notes=notes)
        self.add_blog_item(blog)

    # END REGION

    # REGION: Read
    def init_existing_blog(self):
        """Method to initialize the Blog from existing blogs.json"""
        # read existing blog json if exists
        file_path = config.DEFAULT_BLOG_FILE_PATH
        if os.path.exists(file_path):
            try:
                # read the default blog
                blog_list = JsonFileHelper.read_data(file_path)
                if not isinstance(blog_list, list):
                    raise ValueError("Invalid blog data format. Expected a list of dictionaries.")

                # Get thre valid keys dynamically
                valid_keys = BlogModel.get_class_properties()
                blog_objects = [BlogModel(**{k: v for k, v in blog_item.items() if k in valid_keys})
                                for blog_item in blog_list]

                self.__blog_items = blog_objects
                max_id_count = max(blog.blog_id for blog in self.__blog_items) + 1
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

    # END REGION

    # REGION: Update
    def update(self,
               post_id: int,
               author: str,
               title: str,
               content: str,
               notes: str = ""):
        """Method to update the blog with"""
        try:
            for blog in self.__blog_items:
                if blog.blog_id == post_id:
                    blog.author = author
                    blog.title = title
                    blog.content = content
                    blog.notes = notes
                    break
        except ValueError as e:
            raise e

    def update_likes(self,
                     post_id: int):
        """Method to add the likes for blog."""
        try:
            likes = 0
            for blog in self.__blog_items:
                if blog.blog_id == post_id:
                    blog.likes += 1
                    likes = blog.likes
                    break
            return likes
        except ValueError as e:
            raise e
    # END REGION

    # REGION: Delete
    def delete(self, post_id):
        """Method to delete the blog with"""
        try:
            blog = self.find_blog_item_by_id(post_id)
            if blog:
                self.__blog_items.remove(blog)
        except ValueError as e:
            raise e

    # END REGION

    # REGION: Blog Helpers
    def find_blog_item_by_id(self, post_id):
        """Method to find the blog item by id"""
        try:
            filtered_blogs = list(filter(lambda blog: blog.blog_id == post_id, self.__blog_items))
            if not filtered_blogs:
                raise ValueError(f"Blog with ID {post_id} ")

            return filtered_blogs[0]
        except ValueError as e:
            raise e
        except Exception as e:
            raise e
    # END REGION
