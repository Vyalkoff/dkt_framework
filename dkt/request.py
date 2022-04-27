class PostRequest:
    def __init__(self, environ):
        self.env = environ

    def get_post(self):
        content_length_str = self.env.get('CONTENT_LENGTH')
        content_length_int = int(content_length_str) if content_length_str else 0
        data = self.env['wsgi.input'].read(content_length_int) if content_length_int > 0 else b''
        return data
