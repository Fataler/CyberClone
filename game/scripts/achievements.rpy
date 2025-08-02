init -2 python:
    ACHIEVEMENTS_VERSION = 1

    if not hasattr(persistent, '_achievements_version') or persistent._achievements_version != ACHIEVEMENTS_VERSION:
        persistent._achievements_version = ACHIEVEMENTS_VERSION
        persistent._achievement_unlocked = {}

init -1 python:
    if not hasattr(persistent, '_achievement_unlocked'):
        persistent._achievement_unlocked = {}
    elif persistent._achievement_unlocked is None:
        persistent._achievement_unlocked = {}

init python:
    class Achievement(object):
        def __init__(self, id, name, description, hidden=False, icon="images/achievements/achievement.png"):
            self.id = id
            self.name = name
            self.description = description
            self.hidden = hidden
            self.icon = icon
            
            self.gray_icon = Transform(self.icon, matrixcolor=SaturationMatrix(0.1))
            
        @property
        def unlocked(self):
            return self.id in persistent._achievement_unlocked and persistent._achievement_unlocked[self.id]
            
        def unlock(self):
            if not self.unlocked:
                persistent._achievement_unlocked[self.id] = True
                renpy.play(sfx_ui_achieve, channel="ui")
                renpy.show_screen("achievement_popup", achievement=self)
                renpy.restart_interaction()

    ACHIEVEMENT_ICON_SIZE = 96
    ACHIEVEMENT_POPUP_ICON_SIZE = 64

    # ID достижений
    FUTURE_HISTORIAN = "future_historian"
    MAX_DAMAGE = "max_damage"
    STRATEGIST = "strategist"
    PIG_SLAYER = "pig_slayer"
    GENIUS = "genius"
    FIRST_CHAPTER = "first_chapter"
    SECOND_CHAPTER = "second_chapter"
    THIRD_CHAPTER = "third_chapter"
    THANK_YOU = "thank_you"

    # Список достижений
    achievements = {
        FIRST_CHAPTER: Achievement(
            FIRST_CHAPTER,
            "Пройти 1 акт",
            "",
            False,
            "gui/menu/achievements/1.png"
        ),
        SECOND_CHAPTER: Achievement(
            SECOND_CHAPTER,
            "Пройти 2 акт",
            "",
            False,
            "gui/menu/achievements/2.png"
        ),
        THIRD_CHAPTER: Achievement(
            THIRD_CHAPTER,
            "Пройти 3 акт",
            "",
            False,
            "gui/menu/achievements/3.png"
        ),
        THANK_YOU: Achievement(
            THANK_YOU,
            "Спасибо, что прошёл игру. От всего сердца :)",
            "Пройти игру",
            False,
            "gui/menu/achievements/heart.png"
        ),
        FUTURE_HISTORIAN: Achievement(
            FUTURE_HISTORIAN,
            "Историк будущего",
            "Добро пожаловать в эпоху Эдо 2.0 — теперь с киберимплантами и корпоративным сёгунатом",
            True,
            "gui/menu/achievements/samurai.png"
        ),
        MAX_DAMAGE: Achievement(
            MAX_DAMAGE,
            "Почти получилось, ты просто поддавался",
            "Нанести Дзиндзо максимальное количество урона",
            True,
            "gui/menu/achievements/pokeball.png"
        ),
        STRATEGIST: Achievement(
            STRATEGIST,
            "Трус? Нет, стратег",
            "Попытаться сбежать из боя",
            True,
            "gui/menu/achievements/chess.png"
        ),
        PIG_SLAYER: Achievement(
            PIG_SLAYER,
            "Кабанье проклятье",
            "Одержи победу над Ужасным Вепрем",
            True,
            "gui/menu/achievements/pig.png"
        ),
        GENIUS: Achievement(
            GENIUS,
            "Гений поневоле",
            "Ты ответил правильно на всё. Системе не оставили выбора. Тебе — тоже",
            True,
            "gui/menu/achievements/gears.png"
        ),
    }

    def unlock_achievement(id):
        if id in achievements:
            achievements[id].unlock()
            
    def reset_achievements():
        """Сброс всех достижений"""
        persistent._achievement_unlocked.clear()
        renpy.save_persistent()
        renpy.restart_interaction()

    def unlock_all_achievements():
        for ach in achievements.values():
            ach.unlock()