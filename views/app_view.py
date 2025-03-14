"""Module for App Flask to initialize and handle routes."""

from flask import Flask, redirect, url_for, jsonify
from views.blog_view import BlogView


class AppView:
    """Class for App Flask to initialize and handle routes."""

    def __init__(self, app: Flask):
        self.app = app
        view = self.start_blog()
        self.add_routes(view)

    def start_blog(self):
        """Method to start the blog."""
        view = BlogView()
        self.app.register_blueprint(view.blue_print)
        return view

    def add_routes(self, view):
        """Method to handel HTTP Routes."""

        @self.app.route('/')
        def index():
            # add code here to fetch the job posts from a file
            end_point = f"{view.blue_print_name}.get_all_blogs"
            return redirect(url_for(end_point))

        @self.app.errorhandler(404)
        def not_found_error(error):
            return jsonify({"error": "Not Found"}), 404

        @self.app.errorhandler(405)
        def method_not_allowed_error(error):
            return jsonify({"error": "Method Not Allowed"}), 405
