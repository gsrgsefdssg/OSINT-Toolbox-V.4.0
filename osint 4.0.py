import urllib.parse
import pyperclip
import os
import exifread
from datetime import datetime

def clear_screen():
    """Очищает экран консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Показывает главное меню"""
    print("=" * 50)
    print("           OSINT Toolbox V4.0 by @spokoistvie223")
    print("=" * 50)
    print("1. Поиск по оператору intext:")
    print("2. Поиск по номеру телефона") 
    print("3. Поиск по GitHub")
    print("4. Поиск по Email")
    print("5. Поиск по ФИО")
    print("6. Поиск по номеру машины")
    print("7. Анализ метаданных файла")
    print("8. Выход")
    print("=" * 50)

def intext_search():
    """Поиск по оператору intext:"""
    clear_screen()
    print("[Поиск по intext:]")
    print("=" * 40)
    
    query = input("Введите поисковый запрос: ")
    full_query = f'intext:"{query}"'
    encoded_query = urllib.parse.quote(full_query)
    
    urls = {
        "Google (RU)": f"https://www.google.com/search?q={encoded_query}&hl=ru",
        "Yandex": f"https://yandex.ru/search/?text={encoded_query}",
        "DuckDuckGo (RU)": f"https://duckduckgo.com/?q={encoded_query}&kl=ru-ru",
        "Bing (RU)": f"https://www.bing.com/search?q={encoded_query}&setlang=ru-ru&cc=ru"
    }
    
    print(f"\nСсылки для поиска: intext:\"{query}\"")
    print("=" * 40)
    
    for name, url in urls.items():
        print(f"\n[{name}]")
        print(url)
    
    try:
        pyperclip.copy(urls["Google (RU)"])
        print("\n[+] Ссылка на Google скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def phone_search():
    """Поиск по номеру телефона"""
    clear_screen()
    print("[Поиск по номеру телефона]")
    print("=" * 40)
    
    phone = input("Введите номер телефона: ").strip()
    clean_phone = ''.join(filter(str.isdigit, phone))
    
    queries = {
        "Google": f'"{clean_phone}"',
        "Yandex": clean_phone,
        "VK": clean_phone,
        "Telegram": clean_phone,
        "WhatsApp": clean_phone
    }
    
    sites = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(queries['Google'])}&hl=ru",
        "Yandex": f"https://yandex.ru/search/?text={urllib.parse.quote(queries['Yandex'])}",
        "VK": f"https://vk.com/people/{queries['VK']}",
        "Telegram": f"https://t.me/{queries['Telegram']}",
        "WhatsApp": f"https://wa.me/{queries['WhatsApp']}"
    }
    
    print(f"\nСсылки для поиска номера {clean_phone}:")
    print("=" * 40)
    
    for name, url in sites.items():
        print(f"\n[{name}]")
        print(url)
    
    try:
        pyperclip.copy(sites["Google"])
        print("\n[+] Ссылка на Google скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def github_search():
    """Поиск пользователя и репозиториев на GitHub"""
    clear_screen()
    print("[Поиск по GitHub]")
    print("=" * 40)
    
    username = input("Введите username GitHub: ").strip()
    
    urls = {
        "Профиль пользователя": f"https://github.com/{username}",
        "Репозитории": f"https://github.com/{username}?tab=repositories",
        "Звезды": f"https://github.com/{username}?tab=stars",
        "Подписчики": f"https://github.com/{username}?tab=followers",
        "Подписки": f"https://github.com/{username}?tab=following"
    }
    
    print(f"\nСсылки для поиска пользователя '{username}':")
    print("=" * 40)
    
    for name, url in urls.items():
        print(f"\n[{name}]")
        print(url)
    
    try:
        pyperclip.copy(urls["Профиль пользователя"])
        print("\n[+] Ссылка на профиль скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def email_search():
    """Поиск по email адресу"""
    clear_screen()
    print("[Поиск по Email]")
    print("=" * 40)
    
    email = input("Введите email адрес: ").strip()
    
    queries = {
        "Google": f'"{email}"',
        "Yandex": email,
        "Have I Been Pwned": f"https://haveibeenpwned.com/account/{urllib.parse.quote(email)}",
        "VK": f"https://vk.com/people/{email}",
        "Telegram": f"https://t.me/{email}"
    }
    
    sites = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(queries['Google'])}&hl=ru",
        "Yandex": f"https://yandex.ru/search/?text={urllib.parse.quote(queries['Yandex'])}",
        "Have I Been Pwned": queries["Have I Been Pwned"],
        "VK": queries["VK"],
        "Telegram": queries["Telegram"]
    }
    
    print(f"\nСсылки для поиска email {email}:")
    print("=" * 40)
    
    for name, url in sites.items():
        print(f"\n[{name}]")
        print(url)
    
    print("\n[!] Важно: Have I Been Pwned покажет, был ли email в утечках данных")
    
    try:
        pyperclip.copy(sites["Google"])
        print("\n[+] Ссылка на Google скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def fio_search():
    """Поиск по ФИО"""
    clear_screen()
    print("[Поиск по ФИО]")
    print("=" * 40)
    
    last_name = input("Введите фамилию: ").strip()
    first_name = input("Введите имя: ").strip()
    middle_name = input("Введите отчество (если есть): ").strip()
    
    # Формируем разные варианты ФИО
    full_name = f"{last_name} {first_name} {middle_name}".strip()
    short_name = f"{last_name} {first_name}"
    
    # ИСПРАВЛЕННЫЙ поиск в VK (теперь через обычный поиск)
    queries = {
        "Google": f'"{full_name}"',
        "Yandex": full_name,
        "VK": f"https://vk.com/search?c%5Bq%5D={urllib.parse.quote(full_name)}&c%5Bsection%5D=people",
        "Одноклассники": f"https://ok.ru/search?st.query={urllib.parse.quote(full_name)}",
        "Авито": f"https://www.avito.ru/all?q={urllib.parse.quote(full_name)}"
    }
    
    sites = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(queries['Google'])}&hl=ru",
        "Yandex": f"https://yandex.ru/search/?text={urllib.parse.quote(queries['Yandex'])}",
        "VK": queries["VK"],
        "Одноклассники": queries["Одноклассники"],
        "Авито": queries["Авито"]
    }
    
    print(f"\nСсылки для поиска: {full_name}")
    print("=" * 40)
    
    for name, url in sites.items():
        print(f"\n[{name}]")
        print(url)
    
    print(f"\n[+] Альтернативный вариант: {short_name}")
    
    try:
        pyperclip.copy(sites["Google"])
        print("\n[+] Ссылка на Google скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def car_number_search():
    """Поиск по номеру машины"""
    clear_screen()
    print("[Поиск по номеру машины]")
    print("=" * 40)
    
    car_number = input("Введите номер машины (например, А123БВ777): ").strip().upper()
    
    # Формируем поисковые запросы
    queries = {
        "Google": f'"{car_number}"',
        "Yandex": car_number,
        "Авто.ру": f"https://auto.ru/moskva/cars/all/?license_plate={urllib.parse.quote(car_number)}",
        "Авито Авто": f"https://www.avito.ru/moskva/avtomobili?q={urllib.parse.quote(car_number)}",
        "Drom": f"https://www.drom.ru/order/{urllib.parse.quote(car_number)}/"
    }
    
    sites = {
        "Google": f"https://www.google.com/search?q={urllib.parse.quote(queries['Google'])}&hl=ru",
        "Yandex": f"https://yandex.ru/search/?text={urllib.parse.quote(queries['Yandex'])}",
        "Авто.ру": queries["Авто.ру"],
        "Авито Авто": queries["Авито Авто"],
        "Drom": queries["Drom"]
    }
    
    print(f"\nСсылки для поиска номера {car_number}:")
    print("=" * 40)
    
    for name, url in sites.items():
        print(f"\n[{name}]")
        print(url)
    
    print("\n[!] Поиск по номеру может найти:")
    print("- Объявления о продаже")
    print("- Фотографии машины")
    print("- Обсуждения на форумах")
    print("- Информацию о ДТП (если была публикация)")
    
    try:
        pyperclip.copy(sites["Google"])
        print("\n[+] Ссылка на Google скопирована в буфер!")
    except:
        pass
    
    input("\nНажми Enter чтобы вернуться в меню...")

def metadata_analysis():
    """Анализ метаданных файла"""
    clear_screen()
    print("[Анализ метаданных файла]")
    print("=" * 40)
    
    file_path = input("Укажите полный путь к файлу: ").strip('"')
    
    try:
        if not os.path.exists(file_path):
            print("Ошибка: Файл не найден! Проверьте путь.")
            input("\nНажми Enter чтобы вернуться в меню...")
            return
        
        file_stats = os.stat(file_path)
        file_size = file_stats.st_size
        file_modified = file_stats.st_mtime
        file_created = file_stats.st_ctime
        
        print(f"Размер файла: {file_size} байт")
        print(f"Дата создания: {datetime.fromtimestamp(file_created).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Дата изменения: {datetime.fromtimestamp(file_modified).strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        
        if file_path.lower().endswith(('.jpg', '.jpeg', '.tiff', '.png', '.webp')):
            try:
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f, details=False)
                
                if not tags:
                    print("EXIF-данные не найдены в файле.")
                else:
                    print("\nНайденные EXIF-метаданные:")
                    print("=" * 40)
                    
                    interesting_tags = {
                        'Image DateTime': 'Дата и время съемки',
                        'EXIF DateTimeOriginal': 'Оригинальная дата создания',
                        'GPS GPSLatitude': 'Широта',
                        'GPS GPSLongitude': 'Долгота',
                        'Image Make': 'Производитель камеры',
                        'Image Model': 'Модель камеры'
                    }
                    
                    found_something = False
                    for tag, value in tags.items():
                        if tag in interesting_tags:
                            print(f"{interesting_tags[tag]}: {value}")
                            found_something = True
                    
                    if not found_something:
                        print("Не найдено стандартных EXIF-метаданных.")
            except Exception as ex:
                print(f"Ошибка при чтении EXIF: {ex}")
        else:
            print("Файл не является изображением")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("\nНажми Enter чтобы вернуться в меню...")

def main():
    """Главный цикл программы"""
    while True:
        clear_screen()
        show_menu()
        choice = input("Выберите опцию (1-8): ")
        
        if choice == "1":
            intext_search()
        elif choice == "2":
            phone_search()
        elif choice == "3":
            github_search()
        elif choice == "4":
            email_search()
        elif choice == "5":
            fio_search()
        elif choice == "6":
            car_number_search()
        elif choice == "7":
            metadata_analysis()
        elif choice == "8":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Нажмите Enter...")
            input()

if __name__ == "__main__":
    main()