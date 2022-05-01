import quopri


class ParseDecode:
    @staticmethod
    def parse_str(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data


class GetRequest:

    @staticmethod
    def get_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = ParseDecode.parse_str(query_string)
        return request_params


class PostRequest:
    def __init__(self, environ):
        self.env = environ

    def post(self):
        content_length_str = self.env.get('CONTENT_LENGTH')
        content_length_int = int(content_length_str) if content_length_str else 0
        data = self.env['wsgi.input'].read(content_length_int) if content_length_int > 0 else b''
        return data

    @staticmethod
    def post_decode(data: bytes) -> dict:
        result = {}
        if data:
            data_decode = data.decode(encoding='utf-8')
            result = ParseDecode.parse_str(data_decode)
        return result

    def request_params(self):
        post_length = self.post()
        post = self.post_decode(post_length)
        return ParseDecode.decode_value(post)



