import datetime

# Получите текущую дату
current_date = datetime.date.today()

# Создайте словарь с данными для заполнения шаблона
data = {
    "ArtistName": "Имя художника",
    "ArtistDescription": "Описание художника",
    "ArtistLink": "https://www.example.com/artist",
    "CurrentDate": current_date,
}

# Шаблон HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>{ArtistName}</title>
</head>
<body>
<header>
    <h1>{ArtistName}</h1>
</header>
<main>
    <img src="The_Persistence_of_Memory.jpg" alt="Картина художника 1">
    <p>{ArtistDescription}</p>
    <p>Посетите веб-сайт художника: <a href="{ArtistLink}">ссылка</a></p>
    <p>Текущая дата: {CurrentDate}</p>
</main>
<nav>
    <ul>
        <li><a href="index.html">На главную</a></li>
        <!-- Добавьте ссылки на других художников здесь -->
    </ul>
</nav>
</body>
</html>
"""

# Замените плейсхолдеры данными из словаря
filled_html = html_template.format(**data)

# Сохраните заполненный шаблон в файл
with open("output.html", "w", encoding="utf-8") as output_file:
    output_file.write(filled_html)

print("Шаблон успешно заполнен и сохранен в output.html")
