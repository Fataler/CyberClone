# Мой кибер-двойник опять всё испортил

![Game Icon](icon.ico)

**Визуальная новелла в жанре школьной романтики с элементами фантастики**

[![Ren'Py](https://img.shields.io/badge/Engine-Ren'Py-orange)](https://www.renpy.org/)
[![Version](https://img.shields.io/badge/Version-1.0-green)](https://github.com)
[![Release Date](https://img.shields.io/badge/Release-15.08.2025-blue)](https://github.com)
[![Jam](https://img.shields.io/badge/Game%20Jam-Повидло%20джем%202-purple)](https://t.me/viendesu_official)
[![Jam](https://img.shields.io/badge/Game%20Jam-Джем%20ста%20цветов-red)](https://vk.com/jamof100flowers)

## 📖 Описание

**"Мой кибер-двойник опять всё испортил"** - это визуальная новелла о школьнике Тайде, который мечтает создать робота-клона себя, чтобы тот выполнял все скучные обязанности вместо него. История разворачивается в школьной среде с элементами романтики, дружбы и лёгкой фантастики.

Главный герой - ленивый школьник Тайда, который любит компьютерные игры и проводит много времени в онлайн-играх. Вместе со своими друзьями он посещает школьный кружок робототехники, где пытается воплотить в жизнь свою безумную идею о создании клона.

Игра была разработана в рамках двух игровых джемов:
- [Повидло джем 2](https://t.me/viendesu_official)
- [Джем ста цветов](https://vk.com/jamof100flowers)

## 🛠 Установка и запуск

### Автоматическая установка
1. Скачайте архив игры с [Itch.io](https://fataler.itch.io/cyber-clone)
2. Распакуйте архив в удобную папку
3. Запустите `MyCyberClone.exe`

### Ручная установка из исходников
```bash
# Клонирование репозитория
git clone https://github.com/fataler/cyber-clone.git

# Переход в директорию проекта
cd cyber-clone

# Запуск через Ren'Py SDK
renpy.exe game/
```

## 🏗 Структура проекта

```
game/
├── audio/                 # Аудио файлы
│   ├── bg/               # Фоновая музыка
│   └── sfx/              # Звуковые эффекты
├── chapters/             # Основные главы сюжета
│   ├── chapter1.rpy
│   ├── chapter2.rpy
│   └── chapter3.rpy
├── configs/              # Конфигурационные файлы
│   ├── audio.rpy         # Настройки звука
│   ├── characters.rpy    # Определения персонажей
│   ├── definitions.rpy   # Константы и переменные
│   ├── gui.rpy          # Настройки интерфейса
│   ├── images.rpy       # Определения изображений
│   ├── options.rpy      # Основные настройки
│   └── transforms.rpy   # Анимационные трансформации
├── gui/                  # Графический интерфейс
├── images/              # Графические ресурсы
├── scenes/             # Отдельные сцены
├── screens/            # Экраны интерфейса
│   ├── main_menu.rpy
│   ├── save_load_screen.rpy
│   ├── preferences.rpy
│   └── ...
├── scripts/            # Скрипты и модули
│   ├── achievements.rpy
│   ├── essential/     # Основные скрипты
│   │   ├── auto_flip.rpy
│   │   ├── talking_system.rpy
│   │   └── ...
│   └── mini_games/    # Мини-игры
│       ├── battle_screen.rpy
│       ├── battle.rpy
│       └── clicker_game.rpy
├── tests/             # Тестовые файлы
├── tl/               # Файлы перевода
└── video/            # Видео файлы
    ├── den.webm
    ├── hikaru.webm
    └── ...
```

## 👨‍💻 Команда разработчиков

- **Remi Prochet** ([VK](https://vk.com/remiprochet)) - музыка, звуки
- **Featharine** ([VK](https://vk.com/sweet_sour_figures)) - сценарий, концепт, персонажи, CG, UI
- **Fataler** ([Steam](https://steamcommunity.com/id/fataler)) - код, мини-игры, редактура, анимации
- **Kapushishin** ([Steam](https://steamcommunity.com/id/Kapushishin)) - фоны, сборка новеллы, макеты UI, сбор референсов, режиссура, звуки

## 📚 Использованные ресурсы

### Шрифты
- [Black Ops One (RUS BY aLiNcE)](https://fonts-online.ru/fonts/black-ops-one-rus-alince)
- [Evolventa](https://fonts-online.ru/fonts/evolventa)

### Музыка
- [Meatball Parade by Kevin MacLeod](https://www.chosic.com/download-audio/39319/)
- [Yay by Sakura Girl](https://www.chosic.com/download-audio/59068/)

### Звуковые эффекты
- [Freesound.org](https://freesound.org/) - InspectorJ (Door-Close-SFX)
- [Zvukogram.com](https://zvukogram.com) - дополнительные эффекты

Полный список используемых ресурсов находится в файле `external_resources.txt`.

## 📝 Лицензия

Игра распространяется бесплатно. Использованные сторонние ресурсы имеют соответствующие лицензии (CC BY, CC0 и др.).

## 🌟 Благодарности

- Сообществу Ren'Py за отличный движок
- Участникам джемов "Повидло джем 2" и "Джем ста цветов" за вдохновение
- Всем, кто помогал с тестированием и обратной связью

---

**Разработано с ❤️ на Ren'Py**