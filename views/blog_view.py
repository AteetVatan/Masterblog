"""Module for Blog Flask Blueprint to handle routes."""
import json

from flask import request, Blueprint, render_template, redirect, url_for, jsonify
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
        """blue_print_name property."""
        return self.__blue_print_name

    @property
    def blue_print(self):
        """The Blueprint instance property."""
        return self.__blue_print

    @property
    def blog_view_model(self):
        """The blog_view_model instance property."""
        return self.__blog_view_model

    def add_routes(self):
        """Method to add HTTP Routes."""

        # REGION: Create
        @self.blue_print.route('/add', methods=['GET', 'POST'])
        def add_blog():
            """Api end point to ADD Blog."""
            if request.method == 'POST':
                try:
                    # User has added a Blog else read existing Blog.
                    title = request.form.get("title", "").strip()
                    author = request.form.get("author", "").strip()
                    content = request.form.get("content", "").strip()
                    notes = request.form.get("notes", "").strip()
                    self.blog_view_model.add_blog(author=author,
                                                  title=title,
                                                  content=content,
                                                  notes=notes)
                    return redirect_to_home()
                except ValueError as e:
                    return f"Problem while adding Blog : {e.args[0]}", 404

            return render_template('add.html')

        # END REGION

        # REGION: Read
        @self.blue_print.route('/blogs', methods=["GET"])
        def get_all_blogs():
            """Return all blogs"""
            blogs = self.blog_view_model.blog_items
            add_end_point = f"{self.blue_print_name}.add_blog"
            update_end_point = f"{self.blue_print_name}.update_blog"
            delete_end_point = f"{self.blue_print_name}.delete_blog"

            return render_template('index.html',
                                   add_blog=add_end_point,
                                   update_blog=update_end_point,
                                   delete_blog=delete_end_point,
                                   posts=blogs)

        # END REGION

        # REGION: Update
        @self.blue_print.route('/update/<int:post_id>', methods=['GET', 'POST'])
        def update_blog(post_id):
            """Api end point to update Blog."""
            try:
                # User has added a Blog else read existing Blog.
                if request.method == 'POST':
                    title = request.form.get("title", "").strip()
                    author = request.form.get("author", "").strip()
                    content = request.form.get("content", "").strip()
                    notes = request.form.get("notes", "").strip().strip()
                    self.blog_view_model.update(post_id=post_id,
                                                author=author,
                                                title=title,
                                                content=content,
                                                notes=notes)
                    return redirect_to_home()
                blog = self.__blog_view_model.find_blog_item_by_id(post_id)
                update_end_point = f"{self.blue_print_name}.update_blog"
                return render_template('update.html',
                                       update_blog=update_end_point,
                                       blog=blog)
            except ValueError as e:
                return f"Problem while updating Blog : {e.args[0]}", 404

        @self.blue_print.route('/update_likes', methods=['POST'])
        def update_likes():
            """Handles like button clicks and returns updated like count."""
            try:
                data = json.loads(request.data)
                post_id = int(data.get("post_id", 0))
                like_count = self.__blog_view_model.update_likes(post_id)
                return jsonify({"post_id": post_id, "likes": like_count})
            except ValueError as e:
                return f"Problem while updating Blog likes : {e.args[0]}", 404

        # END REGION

        # REGION: Delete
        @self.blue_print.route('/delete/<int:post_id>', methods=["POST"])
        def delete_blog(post_id):
            """Api end point to delete Blog."""
            try:
                self.__blog_view_model.delete(post_id)
                return redirect_to_home()
            except ValueError as e:
                return f"Problem with Blog ID {post_id}: {e.args[0]}"

        # END REGION

        # REGION: Helper
        def redirect_to_home():
            """Method to redirect to Home page."""
            end_point = f"{self.blue_print_name}.get_all_blogs"
            return redirect(url_for(end_point))
        # END REGION
