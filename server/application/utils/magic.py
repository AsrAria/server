# -*- coding: utf-8 -*-

# python imports
import magic


class NotAllowedExtension(Exception):
    pass


class Magic:
    def __init__(self, app=None):
        self.magic = magic.Magic(mime=True, uncompress=True)
        self.allowed_extensions = None
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.allowed_extensions = app.config.get('MAGIC_ALLOWED_EXTENSIONS')
        self.app = app

    def get_extension(self, buff, type):
        if not self.allowed_extensions:
            return ''

        for ext in self.allowed_extensions[type]:
            try:
                if ext.lower() in self.magic.from_buffer(buff).lower():
                    return ext
            except Exception:
                pass

        raise NotAllowedExtension('allowed types are %s.'
                                  % (', '.join(self.allowed_extensions[type]), ))
