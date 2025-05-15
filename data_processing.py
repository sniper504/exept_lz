import os
import pandas as pd

class DataProcessing:
    def __init__(self, file_path: str, expected_columns: list):
        self.file_path = file_path
        self.expected_columns = expected_columns

    def check_file_existence(self):# проверяем есть ли такой файл 
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Ошибка: Файл '{self.file_path}' не найден.")

    def load_data(self):# загружаем датафрейм и проверяем нужного ли он формата
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            raise IOError(f"Ошибка загрузки файла '{self.file_path}'")
        
    def validate_structure(self, df):# проверяем структуру датафреймя и пустой ли он
        if df.empty:
            raise ValueError("Ошибка: Загруженный датасет пуст.")

        missing_columns = [col for col in self.expected_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Ошибка: В файле отсутствуют ожидаемые столбцы: {missing_columns}")

    def process(self):
        try:
            self.check_file_existence()
            df = self.load_data()
            self.validate_structure(df)
            print("Чтение датафрейма завершено успешно")
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")


file_path = "Проверка на формат.docx"
expected_columns = ["Тип операции", "Сумма операции", "Вид расчета"]
processor = DataProcessing(file_path, expected_columns)
processor.process()
