class PostRequest:
    def __init__(self, environ):
        self.env = environ

    def post(self):
        content_length_str = self.env.get('CONTENT_LENGTH')
        content_length_int = int(content_length_str) if content_length_str else 0
        data = self.env['wsgi.input'].read(content_length_int) if content_length_int > 0 else b''
        return data

    @staticmethod
    def parse_decode(data):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    def post_decode(self, data):
        result = {}
        if data:
            data_decode = data.decode(encoding='utf-8')
            result = self.parse_decode(data_decode)
        return result

    def request_params(self):
        post = self.post()
        post = self.post_decode(post)
        return post
