import os
import pandas as pd

class DataProcessing:
    def __init__(self, file_path: str, expected_columns: list):
        """
        Инициализация класса с путем к файлу и ожидаемыми столбцами.
        :param file_path: Путь к файлу.
        :param expected_columns: Список ожидаемых колонок.
        """
        self.file_path = file_path
        self.expected_columns = expected_columns

    def check_file_existence(self):
        """Проверяет, существует ли файл в директории."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Ошибка: Файл '{self.file_path}' не найден.")

    def load_data(self):
        """Пытается загрузить датасет."""
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            raise IOError(f"Ошибка загрузки файла '{self.file_path}': {str(e)}")

    def validate_structure(self, df):
        """Сверяет структуру датасета с ожидаемой."""
        missing_columns = [col for col in self.expected_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Ошибка: В файле отсутствуют ожидаемые столбцы: {missing_columns}")

    def process(self):
        """Основной метод обработки датасета."""
        try:
            self.check_file_existence()
            df = self.load_data()
            self.validate_structure(df)
            print("✅ Все успешно выполнено!")
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

# Пример использования:
file_path = "var2.csv"
expected_columns = ["column1", "column2", "column3"]
processor = DataProcessing(file_path, expected_columns)
processor.process()
