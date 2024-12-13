import json
import os
from typing import List

from src.products import Category, Product


def load_data_from_json(filepath: str) -> List[Category]:
    """Загружает данные о категориях и товарах из JSON-файла."""
    full_path = os.path.abspath(filepath)
    categories = []
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for category_data in data:
            try:
                products = [
                    Product(product["name"], product["description"], product["price"], product["quantity"])
                    for product in category_data["products"]
                ]
                category = Category(category_data["name"], category_data["description"], products)
                categories.append(category)
            except (KeyError, TypeError, ValueError) as e:
                print(f"Ошибка при обработке данных категории: {category_data}, Ошибка: {e}")

        return categories

    except FileNotFoundError:
        print(f"Ошибка: Файл {full_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON-файл {full_path}.")
        return []


filepath = "../data/products.json"  # Замените на путь к вашему файлу

categories = load_data_from_json(filepath)

if __name__ == "__main__":
    if categories:
        for category in categories:
            print(category)
            for product in category.products:
                print("  ", product)
