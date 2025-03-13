"""Module for Blog Flask Blueprint to handle routes."""
from flask import request, Blueprint, render_template, redirect, url_for

from viewmodels import BlogViewModel


class BlogView:
    """Class for Flask Blueprint (handles routes)"""
    __blue_print_name = "blog"
    __blue_print: Blueprint
    __blog_view_model: BlogViewModel

    def __init__(self):
        self.__blog_view_model = BlogViewModel()
        self.__blue_print = Blueprint(self.blue_print_name, __name__)
        self.add_routes()

    @property
    def blue_print_name(self):
        return self.__blue_print_name

    @property
    def blue_print(self):
        return self.__blue_print

    @property
    def blog_view_model(self):
        return self.__blog_view_model

    def add_routes(self):
        @self.blue_print.route('/blogs', methods=["GET"])
        def get_all_blogs():
            """Return all blogs"""
            blogs = self.blog_view_model.blog_items
            end_point = f"{self.blue_print_name}.add_blog"
            return render_template('index.html', add_blog=end_point, posts=blogs)

        @self.blue_print.route('/add', methods=['GET', 'POST'])
        def add_blog():
            if request.method == 'POST':
                # User has added a Blog else read existing Blog.
                title = request.form.get("title", "")
                author = request.form.get("author", "")
                content = request.form.get("content", "")
                notes = request.form.get("notes", "").strip()
                self.blog_view_model.add_blog(title, author, content, notes)
                end_point = f"{self.blue_print_name}.get_all_blogs"
                return redirect(url_for(end_point))

            return render_template('add.html')
