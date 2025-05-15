import os
import pandas as pd

class DataProcessing:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def check_file_existence(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Ошибка: Файл '{self.file_path}' не найден.")

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except pd.errors.EmptyDataError:  #  если файл пуст
            raise ValueError("Ошибка: Файл пуст")
        except Exception:
            raise IOError(f"Ошибка загрузки файла '{self.file_path}'")

    def validate_data_types(self, df):
        for col in df.columns:
            actual_type = df[col].dtype

            # Определяем ожидаемый тип (числовой или строковый)
            if pd.api.types.is_numeric_dtype(df[col]):
                expected_type = "numeric"
            else:
                expected_type = "string"

            # Проверяем соответствует ли фактический тип ожидаемому
            if expected_type == "numeric" and not pd.api.types.is_numeric_dtype(df[col]):
                raise TypeError(f"Ошибка: Ожидался числовой тип для '{col}', но получен {actual_type}")
            elif expected_type == "string" and not pd.api.types.is_string_dtype(df[col]):
                raise TypeError(f"Ошибка: Ожидался строковый тип для '{col}', но получен {actual_type}")

    def process(self):
        try:
            self.check_file_existence()
            df = self.load_data()
            self.validate_data_types(df)
            print(" Чтение и проверка датафрейма завершены успешно.")
        except (FileNotFoundError, IOError, ValueError, TypeError) as e:
            print(f" {e}")


