from jinja2 import Template
import os


def render(template_name,  **kwargs):
    """

    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """
    file_path = os.path.abspath(template_name)

    with open(file_path, encoding='utf-8') as temp_file:
        template = Template(temp_file.read())
    return template.render(**kwargs)
