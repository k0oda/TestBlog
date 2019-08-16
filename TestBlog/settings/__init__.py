try:
    from TestBlog.settings.prod import *
except ImportError:
    from TestBlog.settings.common import *
