init -1 python:
    import os
    import datetime

    def log_debug(message):
        log_path = os.path.join(config.basedir, "debug_log.txt")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{timestamp}] {message}"

        # Запись в файл
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(full_message + "\n")

        # Вывод в консоль Ren'Py (только при разработке)
        if renpy.config.developer:
            print(full_message)