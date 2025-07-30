

label test_talking_system:
    "Тестирование системы говорящих персонажей"
    # group emotion:
    #     attribute neutral default:
    #         "images/Izumi/Izumi_neutral.png"
    #     attribute angry:
    #         "images/Izumi/Izumi_angry.png"
    #     attribute asharasen:
    #         "images/Izumi/Izumi_asharasen.png"
    #     attribute calm:
    #         "images/Izumi/Izumi_calm.png"
    #     attribute dreamy:
    #         "images/Izumi/Izumi_dreamy.png"
    #     attribute interested:
    #         "images/Izumi/Izumi_interested.png"
    #     attribute neutral_2:
    #         "images/Izumi/Izumi_neutral_2.png"
    #     attribute neutral_3:
    #         "images/Izumi/Izumi_neutral_3.png"
    #     attribute smug:
    #         "images/Izumi/Izumi_smug.png"
    #     attribute thinking:
    #         "images/Izumi/Izumi_thinking.png"
    #     attribute tricky:
    #         "images/Izumi/Izumi_tricky.png"
    #     attribute very_angry:
    #         "images/Izumi/Izumi_very_angry.png"
    show i neutral
    i "izumi neutral"
    show i angry
    i "izumi angry"
    show i asharasen
    i "izumi asharasen"
    show i calm
    i "izumi calm"
    show i dreamy
    i "izumi dreamy"
    show i interested
    i "izumi interested"
    show i neutral_2
    i "izumi neutral_2"
    show i thinking
    i "izumi thinking"
    show i tricky
    i "izumi tricky"
    show i very_angry
    i "izumi very_angry"


    
    show dad
    dad "Привет!"
    dad "Как дела?"
    show mom
    mom "Привет!"
    mom "Как дела?"



    show taida idle at center:
        yalign 0.5
    taida "Привет!"
    show taida happy
    taida "asdfasdfsadfasdfasdfasdfsadfasdfasdfsadf asdfasdasdasd"
    taida "Я говорю."
    show taida sad
    taida "Сейчас и еще немного говорю."
    taida "А теперь я рассказываю очень длинный длинный текст! Много букв разных!"
    show taida thinking at right:
        yalign 0.5

    taida "Я думаю."
    taida "Я думаю о том, что я думаю."
    taida "Я думаю о том, что я думаю о том, что я думаю."
    taida "Я думаю о том, что я думаю о том, что я думаю о том, что я думаю."
    taida "Я думаю о том, что я думаю о том, что я думаю о том, что я думаю. Я думаю о том, что я думаю о том, что я думаю о том, что я думаю."

    show izumi standing
    izumi "Привет!"
    izumi "Сейчас я в стоячей позе."

    izumi "Я говорю."
    izumi "Сейчас и еще немного говорю."
    izumi "А теперь я рассказываю очень длинный длинный текст! Много букв разных!"

    izumi "Договорила и ушла."
    
    
    # Алиса стоит
    show alice standing
    alice "Привет! Я стою."
    alice "Сейчас я в стоячей позе."
    hide izumi
    
    # Алиса садится
    show alice sitting
    alice "А теперь я села."
    alice "Теперь я сижу."
    
    # Смена поз
    show alice standing
    alice "Встаю."

    "Тестовая фраза рассказчика"
    
    show alice sitting  
    alice "Сажусь."
    
    show alice standing
    alice "И снова встаю."
    
    # Финал
    show alice sitting
    alice "Последний раз сажусь."
    alice "Тест завершён."
    
    hide alice
    
    return

label test_binary_text:
    show bg_white
    $ set_character_dzinzo()
    robot_bin "Привет, мир!"
    robot_bin "Произвожу проверку состояния системы..."
    robot_bin "Состояние аккумулятора: 99 процентов. Циклов заряда: 2"
    robot_bin "Все ключевые системы в норме. Продолжаю выполнение задачи."
    robot_bin "Я шел в направлении школы со скоростью 7,8 километра в час."

    robot_bin "По моим расчётам, прибуду в класс №25 в 8:23."
    robot_bin "Через 50 метров нужно перейти дорогу и повернуть направо."

    robot_bin "Пунктуальность важна, чтобы не подвести господина Тайду."

    robot_bin "По дороге я удивлялся многим вещам. Зачем птицы поют о грядущем конце света?"

    robot_bin "Почему люди идут сонными, ведь можно лечь в 22:00 и проснуться в 6:00 бодрым и отдохнувшим?"

    robot_bin "Почему на улице есть бездомные люди, если можно просто купить дом?"

    robot_bin "Несмотря на то, что в мою память заложено много баз данных, некоторые вещи я не могу объяснить."

    $ set_character_taida()
    robot_bin "Предположение: стоит прекратить транслировать бинарный текст в логи."
    robot_bin "Это усложнит их чтение и анализ, если они будут использоваться в будущем."
    robot_bin "Произвожу правку конфигурации Ввода и вывода."
    robot "Так то лучше."
    robot "До пункта назначения осталось 100 метров."

    return

label test_simple_conditions:
    "Тестирование простых условий доступности"
    
    menu:
        "Вариант 1" if False:
            "Вы выбрали вариант 1"
        "Вариант 2":
            "Вы выбрали вариант 2"
        "Вариант 3" if False:
            "Вы выбрали вариант 3"


return