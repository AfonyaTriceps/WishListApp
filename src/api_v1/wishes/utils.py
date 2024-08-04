import csv
from io import StringIO

from src.api_v1.wishes.models import WishCard


async def generate_csv(wishes: list[WishCard]) -> str:
    """Генерация csv из списка желаний."""
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['№', 'Название', 'Ссылка', 'Описание', 'Цена'])

    for i, wish in enumerate(wishes):
        writer.writerow([i + 1, wish.name, wish.url, wish.description, wish.price])

    return output.getvalue()
