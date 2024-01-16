from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageChemicalElements:
    @staticmethod
    def get_all_chemical_elements(driver) -> list:
        """
        Получает список всех химических элементов на веб-странице.
        Указано явное ожидание в 10 секунд.

        :param driver: Экземпляр WebDriver.
        :return: Список экземпляров WebElement
        """
        wait = WebDriverWait(driver, 10)
        locator = "[id='Ptable'][class^= 'Hover']  li[tabindex='0']"
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element = driver.find_elements(By.CSS_SELECTOR, locator)
        return element

    @staticmethod
    def get_list_of_attribute(driver):
        """
        Создает список объектов ChemicalElement на основе данных, извлеченных со страницы.
        Для каждого химического элемента, представленного на странице, извлекает атомный номер, название и атомную массу.

        :param driver: Экземпляр WebDriver
        :return:
        """
        name_addable_locator = "em"
        weight_addable_locator = "data"
        atomic_param = "data-atomic"
        weight_param = "data-abridged"
        atomics, names, weights = [], [], []

        elements = PageChemicalElements.get_all_chemical_elements(driver)
        if elements:
            for i in elements:
                atomic = i.get_attribute(atomic_param)
                atomics.append(atomic)
                name = i.find_element(By.CSS_SELECTOR, name_addable_locator).text
                names.append(name)
                weight = i.find_element(By.CSS_SELECTOR, weight_addable_locator).get_attribute(weight_param)
                weights.append(weight)
            if len(atomics) == len(names) == len(weights):
                return [ChemicalElement(atomic=a, name=n, weight=w) for a, n, w in zip(atomics, names, weights)]
        return []


class ChemicalElement:
    def __init__(self, atomic, name, weight):
        self.atomic = atomic
        self.name = name
        self.weight = weight



