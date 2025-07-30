label test_talking_system:
    "Тестирование системы говорящих персонажей"

    call test_izumi_states
    
    show dad
    dad "Привет!"
    dad "Как дела?"
    hide dad
    show mom
    mom "Привет!"
    mom "Как дела?"
    hide mom

    call test_umi_states
    
    # show t idle at center:
    #     yalign 0.5
    t "Привет!"
    show t happy
    t "asdfasdfsadfasdfasdfasdfsadfasdfasdfsadf asdfasdasdasd"
    t "Я говорю."
    show t sad
    t "Сейчас и еще немного говорю."
    t "А теперь я рассказываю очень длинный длинный текст! Много букв разных!"
    show t thinking at right:
        yalign 0.5

    t "Я думаю."
    t "Я думаю о том, что я думаю."
    t "Я думаю о том, что я думаю о том, что я думаю."
    t "Я думаю о том, что я думаю о том, что я думаю о том, что я думаю."
    t "Я думаю о том, что я думаю о том, что я думаю о том, что я думаю. Я думаю о том, что я думаю о том, что я думаю о том, что я думаю."
    
    "Конец"
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

label test_izumi_states:
    
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

    hide i

    return

label test_umi_states:
    "Тестирование всех состояний персонажа Umi"
    
    show bg_amusement_park
    "=== ПОЗА OPEN (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u open neutral school
    u "u open neutral school"
    
    show u open angry school
    u "u open angry school"
    
    show u open cute school
    u "u open cute school"
    
    show u open embarrassed school  
    u "u open embarrassed school"
    
    show u open laugh school
    u "u open laugh school"
    
    show u open laugh_wall school
    u "u open laugh_wall school"
    
    show u open surprised school
    u "u open surprised school"
    
    show u open thinking school
    u "u open thinking school"
    
    "=== ПОЗА OPEN (ЛЕТНЯЯ ФОРМА) ==="
    
    show u open neutral summer
    u "u open neutral summer"
    
    show u open cute summer
    u "u open cute summer"
    
    "=== ПОЗА CLOSED (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u closed alluring school
    u "u closed alluring school"
    
    show u closed confused school
    u "u closed confused school"
    
    show u closed cry school
    u "u closed cry school"
    
    show u closed cry_embarrassed school
    u "u closed cry_embarrassed school"
    
    show u closed sad_cry school
    u "u closed sad_cry school"
    
    show u closed touched school
    u "u closed touched school"
    
    show u closed tricky school
    u "u closed tricky school"
    
    "=== ПОЗА CLOSED (ЛЕТНЯЯ ФОРМА) ==="
    
    show u closed alluring summer
    u "u closed alluring summer"
    
    show u closed tricky summer
    u "u closed tricky summer"
    
    "=== ПОЗА GREETING (ШКОЛЬНАЯ ФОРМА) ==="
    
    show u greeting smile school
    u "u greeting smile school"
    
    show u greeting confused school
    u "u greeting confused school"
    
    show u greeting offended school
    u "u greeting offended school"
    
    show u greeting offended_sad school
    u "u greeting offended_sad school"
    
    hide u
    "Тест состояний Umi завершён!"
    
    return