label test_talking_system:
    "Тестирование системы говорящих персонажей"

    call test_izumi_states from _call_test_izumi_states
    
    show dad
    dad "Привет!"
    dad "Как дела?"
    hide dad
    show mom
    mom "Привет!"
    mom "Как дела?"
    hide mom

    call test_umi_states from _call_test_umi_states
    
    call test_dzinzo_states from _call_test_dzinzo_states
    
    call test_taida_states from _call_test_taida_states
    
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

    hide u
    
    show u greeting confused school
    u confused "u greeting confused school"
    
    show u greeting offended school
    u "u greeting offended school"
    
    show u greeting offended_sad school
    u "u greeting offended_sad school"
    
    hide u
    "Тест состояний Umi завершён!"
    
    return

label test_taida_states:
    "Тестирование всех состояний персонажа Taida"
    
    show bg_class_room
    
    "=== ПОЗА EAR (БЕЗ ШКОЛЬНОЙ ФОРМЫ) ==="
    
    show t_f ear neutral
    t ear neutral "ear neutral (default)"
    
    show t_f ear careless
    t ear careless "ear careless (беззаботный)"
    
    show t_f ear cute
    t ear cute "ear cute (милый)"
    
    show t_f ear cute_cry
    t ear cute_cry "ear cute_cry (плачет)"
    
    show t_f ear embarrassed
    t ear embarrassed "ear embarrassed (смущенный)"
    
    show t_f ear laugh
    t ear laugh "ear laugh (непосредственный)"
    
    show t_f ear neutral_camera
    t ear neutral_camera "ear neutral_camera (4 стена)"
    
    show t_f ear silly
    t ear silly "ear silly (глупый)"
    
    show t_f ear oops
    t ear oops "ear oops (упс)"
    
    show t_f ear surprised
    t ear surprised "ear surprised (удивлен)"
    
    "=== ПОЗА EAR_SCHOOL (В ШКОЛЬНОЙ ФОРМЕ) ==="
    
    show t_f ear_school neutral
    t ear_school neutral "ear_school neutral (default)"
    
    show t_f ear_school cry
    t ear_school cry "ear_school cry (плачет)"
    
    show t_f ear_school dream
    t ear_school dream "ear_school dream (мечтательный)"
    
    show t_f ear_school surprised
    t ear_school surprised "ear_school surprised (удивлен)"
    
    show t_f ear_school sad_angry
    t ear_school sad_angry "ear_school sad_angry (грусть+злость)"
    
    show t_f ear_school angry
    t ear_school angry "ear_school angry (злость)"
    
    show t_f ear_school sad
    t ear_school sad "ear_school sad (печальный)"
    
    show t_f ear_school fear
    t ear_school fear "ear_school fear (испуганный)"
    
    show t_f ear_school crazy
    t ear_school crazy "ear_school crazy (безумие)"
    
    show t_f ear_school happy
    t ear_school happy "ear_school happy (счастливый)"
    
    show t_f ear_school tricky
    t ear_school tricky "ear_school tricky (хитрость)"
    
    show t_f ear_school neutral_happy
    t ear_school neutral_happy "ear_school neutral_happy (нейтральный счастливый)"
    
    show t_f ear_school think
    t ear_school think "ear_school thinking (думаю)"
    
    show t_f ear_school asharashen
    t ear_school asharashen "ear_school asharashen (ашарашен)"
    
    show t_f ear_school calm
    t ear_school calm "ear_school calm (спокойный)"
    
    show t_f ear_school depressed
    t ear_school depressed "ear_school depressed (депрессивный)"
    
    "=== ПОЗА THINKING (ПОЗА 2) ==="
    
    show t_f thinking neutral school
    t thinking neutral "thinking neutral (default)"
    
    show t_f thinking cunning school
    t thinking cunning "thinking cunning (хитрый)"
    
    show t_f thinking neutral_4stena school
    t thinking neutral_4stena "thinking neutral_4stena (4 стена)"
    
    show t_f thinking asharashen school
    t thinking asharashen "thinking asharashen (ашарашен)"
    
    show t_f thinking genius school
    t thinking genius "thinking genius (гений)"
    
    show t_f thinking sleepy school
    t thinking sleepy "thinking sleepy (сонный)"
    
    show t_f thinking think school
    t thinking think "thinking thinking (думает)"
    
    show t_f thinking thinking_hard school
    t thinking thinking_hard "thinking thinking_hard (сильно думает)"
    
    show t_f thinking tired school
    t thinking tired "thinking tired (устал)"
    
    "=== ПОЗА HZ (ПОЗА 1) ==="
    
    show t_f hz neutral school
    t hz neutral "hz neutral (default)"
    
    show t_f hz cry_4stena school
    t hz cry_4stena "hz cry_4stena (плачет 4 стена)"
    
    show t_f hz cry_sad school
    t hz cry_sad "hz cry_sad (плачет подавленно)"
    
    show t_f hz cry_why school
    t hz cry_why "hz cry_why (плачет вопросительно)"
    
    show t_f hz happy school
    t hz happy "hz happy (счастлив)"
    
    show t_f hz smile school
    t "hz smile (улыбается)"
    
    show t_f hz dissatisfied school
    t hz dissatisfied "hz dissatisfied (недоволен)"

    hide t_f
    
    show t_f hz neutral_4stena school left
    t hz neutral_4stena "hz neutral_4stena (нейтральный 4 стена)"
    
    show t_f hz glad school right
    t hz glad "hz glad (радуется)"
    
    show t_f hz wtf school
    t hz wtf "hz wtf"
    
    "=== ТЕСТ ЛЕТНЕЙ ФОРМЫ ==="
    
    show t_f ear neutral summer_norm
    t ear neutral summer_norm "ear neutral summer_norm"
    
    show t_f thinking neutral summer_strem
    t thinking neutral summer_strem "thinking neutral summer_strem"
    
    show t_f hz neutral summer_norm
    t hz neutral summer_norm "hz neutral summer_norm"

    show t_f hz neutral summer_strem
    t hz neutral summer_strem "hz neutral summer_strem"
    
    hide t_f
    "Тест состояний Taida завершён!"
    
    return

label test_dzinzo_states:
    "Тестирование всех состояний персонажа Dzinzo"
    
    show bg_near_school
    "=== ПОЗА POSE1 (ШКОЛЬНАЯ ФОРМА) ==="
    
    show d pose1 neutral school
    d "d pose1 neutral school"
    
    show d pose1 happy school
    hide d
    d "d pose1 happy school"
    t "d a"
    d_t "мысли Дзиндзо"
    show t_f happy
    t_f "мысли тайда"
    
    show d pose1 very_happy school
    d "d pose1 very_happy school"
    
    show d pose1 surprised school
    d "d pose1 surprised school"
    
    show d pose1 thinking school
    d "d pose1 thinking school"
    
    show d pose1 cunning school
    d "d pose1 cunning school"
    
    show d pose1 relief school
    d "d pose1 relief school"
    
    "=== ПОЗА POSE1 (ЛЕТНЯЯ ФОРМА) ==="
    
    show d pose1 neutral summer
    d "d pose1 neutral summer"
    
    show d pose1 happy summer
    d "d pose1 happy summer"
    
    "=== ПОЗА POSE2 (ШКОЛЬНАЯ ФОРМА) ==="
    
    show d pose2 neutral school
    d "d pose2 neutral school"
    
    show d pose2 sad school
    d "d pose2 sad school"
    
    show d pose2 melancholy school
    d "d pose2 melancholy school"
    
    show d pose2 osharashen school
    d "d pose2 osharashen school"
    
    show d pose2 pupupu school
    d "d pose2 pupupu school"
    
    "=== ПОЗА POSE2 (ЛЕТНЯЯ ФОРМА) ==="
    
    show d pose2 neutral summer
    d "d pose2 neutral summer"
    
    show d pose2 sad summer
    d "d pose2 sad summer"
    
    hide d
    "Тест состояний Dzinzo завершён!"
    
    return
