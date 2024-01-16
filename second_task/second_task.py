import pytest
from page.page_chemical_elements import PageChemicalElements

class TestChemicalElementInstance:
    """
    Класс предназначен для проверки экземпляров ChemicalElement.
    """
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_chemical_element_instance(self, browser):
        """
        Проверяет количество химических элементов (экземпляров ChemicalElement)

        :param browser: Фикстура pytest, предоставляющая экземпляр WebDriver
        """
        link = "https://ptable.com/?lang=ru"
        browser.get(link)
        elements = PageChemicalElements.get_list_of_attribute(browser)
        # Предполагая, что кол-во химических элементов 'редко' меняется, проверяю явно.
        assert len(elements) == 118, f"Количество химических элементов, представленных на странице {link} не равно 118." \
                                     f"Представлено {len(elements)}"
        for element in elements:
            print(element.atomic, element.name, element.weight)
