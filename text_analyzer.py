class TextAnalyzer:
    """
    Утилита для анализа текстовых данных.
    Предоставляет статические методы для подсчета количества символов и слов в тексте.
    """

    @staticmethod
    def count_words(text: str) -> int:
        """
        Подсчитывает количество слов в переданной строке текста.
        
        :param text: Анализируемый текст.
        :type text: str
        :return: Количество слов (разделенных пробелами).
        :rtype: int
        """
        if not text:
            return 0
        return len(text.split())

    @staticmethod
    def count_characters(text: str, ignore_spaces: bool = False) -> int:
        """
        Подсчитывает количество символов в тексте.
        
        :param text: Анализируемый текст.
        :type text: str
        :param ignore_spaces: Не учитывать пробелы при подсчете (по умолчанию False).
        :type ignore_spaces: bool
        :return: Общее количество символов.
        :rtype: int
        """
        if ignore_spaces:
            text = text.replace(" ", "")
        return len(text)

# Пример использования (для тестов)
if __name__ == "__main__":
    sample_text = "Привет, мир! Это тестовый скрипт."
    print(f"Слов: {TextAnalyzer.count_words(sample_text)}")
    print(f"Символов (с пробелами): {TextAnalyzer.count_characters(sample_text)}")
    print(f"Символов (без пробелов): {TextAnalyzer.count_characters(sample_text, ignore_spaces=True)}")
