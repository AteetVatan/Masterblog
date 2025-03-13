"""Package for presentation Flask routes (API endpoints)"""
from .blog_view import BlogView
from .app_view import AppView

__all__ = ["AppView", "BlogView"]
