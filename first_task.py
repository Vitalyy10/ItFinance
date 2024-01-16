from urllib.parse import urlparse, parse_qs
import validators


class LinkParser:
    @staticmethod
    def is_link(url: str):
        """
        Проверяет, является ли переданная строка валидным URL.

        :param url: Ссылка, которую необходимо проверить на корректность.
        :return: True, если передан корректный формат ссылки.
        :raise ValueError: Если проверка не пройдена.
        """
        if not isinstance(url, str) or not validators.url(url):
            raise ValueError(f"Некорректный URL: {url}")
        return True

    @staticmethod
    def get_query_params(url: str) -> dict:
        """
        Возвращает словарь, содержащий параметры и их значения из url

        :param url: Ссылка, из которой необходимо достать параметры и их значения.
        :return: Словарь, где key: str - название параметра, value: list of str, - значение параметра списком.
        """
        LinkParser.is_link(url)
        parsed_url = urlparse(url)
        # Получаем строку запроса
        query_string = parsed_url.query
        # Разбираем строку запроса на параметры
        query_params = parse_qs(query_string)
        return query_params

    @staticmethod
    def get_param_value(url: str, attribute: str) -> str:
        """
        Возвращает значение аттрибута в ссылке

        :param url: Ссылка, из которой необходимо вытащить значение аттрибута.
        :param attribute: Аттрибут, значение которого необходимо вытащить.
        :return: Значение заданного аттрибута.
        :raise ValueError: Если заданного аттрибута нет в ссылке.
        """
        query_params = LinkParser.get_query_params(url)
        # Получаем значение нужного параметра
        param_value = query_params.get(attribute)
        if param_value is None:
            raise ValueError(f'В ссылке отсутствует параметр {attribute}')
        else:
            param_value_string = ''.join(param_value)
            return param_value_string


urls = 'https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE'
class_instance = LinkParser()
attrib = 'clickid'
print(class_instance.get_param_value(url=urls, attribute=attrib))
