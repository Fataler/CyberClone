label chapter2:
#Акт 2
#Class Room.JPG
call screen time_passed("На следующее утро")

$ renpy.pause(1.0)
show bg_class_room with Dissolve(1)
play music music_main_theme_2_v3 fadein 0.5 fadeout 1.0 loop

t_t thinking tired "Ранним утром я уже сидел в классе. "

t_t sleepy "Обычно я всегда опаздываю, поэтому увидеть моё сонное тело среди первых — для многих было бы поводом вызвать санитаров."

t_t tired "Одноклассники таращились на меня, как на диковинного зверя. "

t_t genius "Я лишь хитро прищуривался в лучах утреннего солнца и ждал друзей. "

show k pose2 neutral right at Transform(xalign=0.6, yalign=1.0)
show den left at Transform(xalign=0.8, yalign=1.0)
show h left at Transform(xalign=1.0, yalign=1.1)
with Dissolve(1.0)

t_t "Наконец, когда они появились на горизонте."

show k pose1 at move_on_scene(xalign=0.1)
show den awesome neutral at move_on_scene(time=1.7, xalign=0.5)
show h smile at move_on_scene(time=1, xalign=0.9)

t_t ear_school smile "Я помахал им рукой и подозвал к себе. "

t_t "Кацуми поставила стакан воды на мой стол и встала рядом. Хикару занял место сбоку. Ден — как всегда, устроился задом наперёд на стуле передо мной."

den idle neutral "Ты чего такой радостный?"

k pose2 cunning "Мне кажется, он заболел, смотрите на этот нездоровый блеск в глазах."

h surprised "Друг, давай-ка топай домой."

t_t neutral "Я отмахнулся от его несомненно заманчивого предложения."

show k neutral
show h neutral

t "Ребята, я тут понял одну вещь."

t think "Зачем мы тратим свой талант и потенциал на какую-то паштетомазку?"

t_t calm "Сделав паузу и выразительно покосившись по сторонам, я наклонился ближе:"

show k pose2 annoyed

t thinking genius "Мы создадим робота, человекоподобного андроида, живую куклу. Помощника, который сможет делать всё — от хирургии до преподавания. Сечёте?"

show k pose2 didnt_understand
show den sad

h explain neutral_talk "А теперь конструктивно. У тебя есть чертежи, по которым его можно будет создать?"

t hz glad "Лучше! У меня есть рисунок."

t_t smile "И ловким движением руки я достал листок, где красовался криво нарисованный человечек с болтиками на руках, ногах, лице и шее. "

show k pose2 asharashen at fear
show den idle nervous
show h explain thinking

t_t "Кацуми подавилась водой."

k annoyed "Пошутили и хватит. Ты подготовился к сегодняшней контрольной?"

show h idle neutral
show den awesome neutral

t ear_school depressed "Слушайте, я серьёзно. Представьте, сколько людей мы могли бы спасти!"

t_t "Понимая, что времени мало, я перешёл к финальному аргументу."

show h idle surprised

t thinking neutral "Искусственный интеллект способен произвести любые сложные расчёты, Хикару, это ведь основная твоя проблема в чертежах?"

show den awesome surprised

t think "Ден, если загрузить в него медицинскую базу данных, он сможет следить за состоянием твоей мамы, чтобы помочь ей вылечиться!" 

show k pose1 worried

t hz smile "Кацуми... ты же всегда мечтала о достойном противнике в шахматах. Так создай его!"

t_t ear_school neutral "Ребята больше не выглядели такими уверенными."

t_t "Мы решили отложить этот разговор до школьного кружка."

$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black
hide k
hide den
hide h
with Dissolve(1)
#черный экран

$ renpy.pause(1.0)

#Robo-Class Room.JPG
show bg_robo_class_room with Dissolve(1)
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
play music music_main_theme fadein 0.5

show k pose1 cunning right at quad_right
show den idle sad left at quad_right_center
show h idle neutral right at quad_left_center
with Dissolve(1)

t_t "Все мы сидим за столом кружка и задумчиво смотрим друг на друга. "

play sfx sfx_open_door
show i calm right at enter_scene(from_left=True, xalign=-0.1)

t_t "В класс заходит миссис Изуми."

show i tricky

t_t "Слегка подняв бровь, она осматривает наше сборище вопросительным взглядом."

i "У вас сегодня заседание Молчаливого Прямоугольного Стола?"

t_t dream "В ответ — тишина."

i very_angry "Ребята, у меня в руках линейка, и если вы мне не ответите, я измерю ваш болевой порог."

t think "Мы..."

h surprised "...хотим..."

den nervous "...собрать..."

show k at Transform(xalign=1.1,yalign=1.0)

k pose2 didnt_understand "...человека-робота."

show i at giggle()
i asharashen "Я, конечно, сегодня встала не с той ноги, но не настолько, чтобы поверить в подобные галлюцинации."

i "Вы серьёзно?"

t_t sad "Она явно решила, что мы шутим."

show i angry
play sfx sfx_hit
t_t neutral "Я встал и с громким звуком оперся руками о стол."

show k pose1 worried at Transform(xalign=1.0 ,yalign=1.0)
show den idle sad
show h neutral

$ renpy.music.set_volume(0.5, delay=2.0, channel="music")

t_t "Все притихли."

pause 1.5


t thinking cunning "Абсолютно."
$ renpy.music.set_volume(1.0, delay=0.2, channel="music")
t hz glad "Представьте, сколько пользы он принесёт!"

#Тайда Нингё снова активирует своё умение "Ва банк"! 
show i neutral_2

t thinking genius stars "Робот, который не только мажет паштет, но справляется со сливочным маслом и даже с красной рыбой."

show i tricky

t_t "В глазах Изуми заплясали бесовские огоньки."

i "А давайте!"

i happy "Ну, раз так — за работу! По местам! Какие идеи?"

stop music fadeout 1.0
hide i 
hide k
hide den
hide h
scene bg_black
with Dissolve(1)
pause 1.0

#Assembling Demo 2.ogg
#музыка

# слайдшоу цг

#цг Кацуми программирует 


# цг Хикару чертит

# ЦГ Ден паяет

# ЦГ Тайда читает литературу

# ЦГ Ребята собирают робота

# ЦГ Юми приносит чай

# Мини игра поиск предметов

# Мини игра пазл 

# ЦГ робот готов
call assembling_scene from _call_assembling_scene

scene bg_robo_class_room
play music music_main_theme_2_v3 fadein 0.5 fadeout 1.0 loop
show k pose2 cunning right at penta_right_center
show den awesome neutral right at penta_left
show h idle smug left at penta_right
show i smug right at penta_left_center
with Dissolve(0.5)

t_t ear_school smile "Наконец, мы закончили эту работу. "

t_t thinking thinking_hard "Проект тянул на дело всей жизни — или, по меньшей мере, походил на разработку визуальной новеллы, сжатую в два безумных месяца, прожитых на чистом энтузиазме."

t_t tired "Сказать, что мы вымотались, — ничего не сказать: каждый выложился до предела. "

t_t "Даже я."

t_t cunning "И, честно говоря, это было круто. Общее дело сближает."

t_t ear_school neutral "И вот мы стоим перед ним. Нашим изобретением."

stop music fadeout 1.0
play sfx sfx_pressure fadein 0.5 loop
$ renpy.music.set_volume(0.3, delay=0.5, channel="sfx")
#ЦГ ребята в ауте и Дзиндзо
show all_shocked with Dissolve(0.5)
"..."

show den idle asharashen right at Transform(xalign=-0.05, yalign=1.0)
show i asharashen right at Transform(xalign=0.1, yalign=1.0)
show k pose2 asharashen right at Transform(xalign=0.85, yalign=1.0)
show h explain asharashen left at Transform(xalign=1.15, yalign=1.0)
hide all_shocked 
with Dissolve(0.5)

k didnt_understand "Э‑э... Ребята..."

k "Вас ничего не смущает?"

den idle nervous "Что-то не так, но не могу понять что..."

h explain surprised "Как будто мы упустили важную деталь..."

show k asharashen
show i asharashen
show den asharashen
show h explain asharashen
show d_f pose3 neutral with Dissolve(1.0)

i "Почему робот выглядит точь‑в‑точь как Тайда?!"

stop sfx fadeout 0.5
$ renpy.music.set_volume(1.0, delay=0.5, channel="sfx")
play music music_comedy fadein 0.5 fadeout 1.0 loop
show k at giggle
show i at fear
show den at giggle
show h at fear

$ speak_as("Все", "Точно!")

show k at fear

k "Как так получилось?!"

show h at fear

h "Неужели, я что-то напутал в чертежах..."

t_t thinking genius "Я хитро улыбнулся. Конечно, перепутал — особенно после моих ночных \"корректировок\"."

t_t "Это стоило мне больших усилий — пришлось разобраться во всём, что делают ребята. Каждый из них."

show den at fear

den nervous "Я могу всё перепаять!"

k annoyed "Я надеюсь, мы случайно не заключили разум этого балбеса внутрь прототипа?"

t ear_school asharashen "Что вы несёте, это невозможно!"

t calm "Я не обижен, пусть будет выглядеть как я. И вообще."

t happy "У меня самая обычная внешность. Немудрено, что робот вышел похожим на меня."

t hz happy "Да и вообще не так уж он и похож. Нос видели? У меня разве такой длинный?"

show k smug
show den awesome happy at Transform(xalign=-0.1, yalign=1.0)
show h idle cunning at Transform(xalign=1.0, yalign=1.0)
show i smug

$ speak_as("Все", "Да.")

t wtf "Ну длинный и длинный... Чего вы вообще к его носу привязались?"

show k pose1 neutral at Transform(xalign=0.8, yalign=1.0)
show den awesome neutral
show h idle neutral

t_t ear_school neutral "Друзья пожимают плечами, соглашаясь с моими доводами."

show h at Transform(xalign=1.1, yalign=1.0)

h explain neutral_talk "Как мы его назовем?"

i happy "Дзиндзо, конечно же, как ещё?"

den wink "Звучит!"

i neutral_2 "Ладно, ребята. Всем пора по домам. Попробуем включить его уже завтра."

t_t think "Гордые и уставшие мы направились домой. "

#stop music fadeout 1.0
$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black
with Dissolve(1)
pause 0.5
#фон дерево у школы
#play music music_main_theme_2_v3 fadein 0.5 fadeout 1.0 loop
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
show bg_school_entrance 
show k pose1 neutral right at trio_left
show den awesome neutral left at trio_center
show h idle neutral left at trio_right
with Dissolve(1)

t_t neutral "Уже у выхода из школы я начинаю рыться в сумке."

t ear_school think "Ой, кажется, телефон в классе забыл..."

k pose1 cunning "Пошли, открою тебе кабинет. Как глава клуба я не могу доверять ключ посторонним."

t hz happy "Не волнуйся! Просто возьму телефон и завтра же отдам тебе ключик!"

t_t smile "Я состроил заискивающий щенячий взгляд."

t_t "Кацуми оставалась непреклонной."

k angry "А если ты забудешь запереть за собой дверь и нашего робота украдут?"

t happy "Я хоть раз забывал закрыть кабинет?!"

k cunning "А тебе это хоть раз доверяли?!"

t hz wtf "Нет. Ну и что?"

show k pose2 annoyed at Transform(xalign=0, yalign=1.0)

t_t neutral "Кацуми тяжело вздохнула."

den happy "Да пойдем, что с ним будет. Принесёт завтра, никуда не денется."

h explain neutral_talk "Да, нам ещё тонну домашки делать, мы потеряем кучу времени, если пойдем все вместе."

k didnt_understand "Ладно, бери. Но если не принесешь ключ завтра или испаришься сам, я с тебя три шкуры сдеру."

den tricky "Лучше заставь его на улице знакомиться с девушками и звать их в караоке!"

den shy "Вдруг кто-нибудь согласится!"

den happy "А если нет, то это он будет выглядеть как дурак!"

show k cunning
show h idle cunning 

h idle happy "В этом весь наш Денис. Гениальные мысли часто преследовали его, но он всегда оказывался быстрее."

"..."

stop music fadeout 4

h surprised "А где Тайда?"

hide k
hide h
hide den
show bg_black
with Dissolve(0.5)

play sfx sfx_steps_on_floor loop
stop music fadeout 1.0

t_t ear_school tricky "А Тайда уже летел по лестнице на третий этаж к классу кружка. Тайда умный, Тайда хитрый!"

t_t dream "Ладно, хватит называть себя в третьем лице, а то даже в мыслях я звучу как дурак. "

play sound sfx_steps_on_road
t_t asharashen "Сердце бешено билось, ноги путались, каждая ступенька казалась вечностью."

stop sfx

t_t "Наконец, добравшись до двери, я судорожно вставил ключ (с третьей попытки), повернул его и..."

play sfx sfx_door_lock
pause 2.0
play sfx sfx_open_door

#Robo-Class Room.JPG
scene bg_robo_class_room with Dissolve(1)

#show d summer

play sound sfx_open_door
"."
".."
"..."

play music music_main_theme_2_v3 fadein 0.5 fadeout 1.0 loop
show d_f pose3 neutral at center with Dissolve(1)

t_t neutral "Вот он, момент истины."

t_t "Я приблизился к андроиду, одиноко сидящему на стуле."

t_t asharashen "Наедине с ним даже стало жутковато."

t_t "Привет, Дзиндзо. Мой кибер-двойник."

t_t ear_school asharashen "Дрожащими руками я нажимаю кнопку на его корпусе..."

play music music_main_theme_3_v2 fadein 0.5

d_f "Здравствуйте, господин. Как мне к вам обращаться?"

t_t fear "Я отпрянул, но быстро понял, что бояться нечего."

t asharashen "Просто зови меня Тайда."

d_f "Понял вас, господин Тайда. Чем могу помочь?"

t_t thinking cunning "Получилось!"

t_t ear_school calm "Я пододвинул стул ближе к нему, расслабленно сел, закинув ногу на ногу, и откинул волосы с лица."

t "В общем, слушай."

t "Ты — это я. Понял?"

d_f "Не понял вас, господин Тайда. Поясните, пожалуйста."

t thinking neutral "Добавь эту информацию в системный промт. Ты ведёшь себя как я. Ходишь вместо меня в школу, моешь посуду, пылесосишь и вообще помогаешь родителям."

t genius "Ходишь в кружок робототехники и показываешь всем, какой ты, то есть, я, умный. Так понятнее?"

d_f "Так понятнее."

show d_f smile

t_t neutral_4stena "Дзиндзо сел точно в мою позу и откинул волосы так же эффектно."

t_t think "Да уж, насколько сильно заметны все наши недоработки: шарниры, болты, индикаторы..."

t neutral "Важно: никто не должен узнать, что нас двое. Ты это я, и точка." 

t "Нужно тебя замаскировать."

t_t ear_school neutral "Я заранее подготовился и захватил с собой несколько полезных штучек: шарф, перчатки и рюкзак с пауэрбанком. "

t_t "Водрузив на Дзиндзо рюкзак, я подсоединил его к зарядке. "

t_t thinking think "Индикаторы на лице были слишком заметны. Нужно было их чем-то скрыть."

t_t genius "Точно, пластыри Юми! В клубе всегда хранится стратегический запас пластырей — ими-то я его и подлатаю."

t_t neutral_4stena "Окинув робота взглядом, я пожал плечами."

t "А теперь раздевайся."

t_t neutral "Дзиндзо идентично пожал плечами и разделся."

t "Ты наденешь мою школьную форму, а я — твою одежду."

t_t ear_school calm "Благо изначально робот был одет в мою одежду — чья ещё подойдёт ему лучше, чем одежда его прототипа?"
t_t "Ну и накину мою любимую рубашку поверх."

show d_f pose2 school neutral with Dissolve(0.5)
pause 0.5

t_t ear neutral summer_norm "Мы словно поменялись ролями."

t_t thinking genius stars "Последними штрихами был шарф и перчатки, чтобы скрыть шарниры. Идеально!"

t neutral_4stena "Теперь тихо и незаметно добираемся до нашего дома. Ясно?"

d_f "Принято!"

t think "Давай придумаем с тобой стоп-слово, если ты поймешь, что произошла экстренная ситуация, и нас сейчас раскроют!"

t "Скажи любое слово."

show d_f melancholy

t_t "Дзиндзо вопросительно склонил голову, совсем как человек."

d_f neutral "Мандарин 🍊."

t_t asharashen "Теперь уже моя очередь была изображать вопросительный взгляд. "

t "Мандарин 🍊? Ну ладно, ты — это я, а я ерунды не скажу."

t neutral "Погнали!"

t_t ear neutral summer_norm "Мы гуськом выбежали из школы. Я шел впереди и прижимался к стенам, как шпион, высматривая тех, кто мог нас обнаружить. Миссия была почти невыполнима. "

scene bg_black with Dissolve(1)
pause 0.5
scene bg_near_school 
play sfx sfx_bushes_v2
show d_f pose2 neutral at Transform(xalign=-0.4, yalign=1.0), move_on_scene(time=3.0, xalign=0.5)
show bush2 at size_change(1.0, 1.0) onlayer master zorder 2:
    pos (0, 0.2)
show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100
with Dissolve(1)

#Фон дерево у школы
play sound sfx_bushes_v2

t_t ear neutral summer_norm "Окольными путями, через кусты и под заборами мы пробирались к дому."

stop sfx
play sfx sfx_bushes_v2
show d_f pose2 at Transform(xalign=0.5, yalign=1.0), move_on_scene(time=5.0, xalign=2.0)
play sound sfx_bushes_v2

t_t confused "Пару раз мы чуть не попались на глаза прохожим, но чистая случайность каждый раз спасала нас."

#Near Home.JPG
hide bush4 onlayer screens

scene bg_black with Dissolve(1)
call screen time_passed("Тридцать минут спустя")
show bg_near_home with Dissolve(1)
show d_f pose2 neutral right at penta_left with Dissolve(0.5)
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")

t_t ear careless summer_norm "Возле дома я расслабился и потерял бдительность. Только выйдя из кустов рядом с калиткой, я заметил отца."

show dad left at penta_right with Dissolve(1)

t_t fear "Он стоял спиной к нам и о чём-то разговаривал по телефону."

t thinking asharashen "МАНДАРИН 🍊, МАНДАРИН 🍊!!!"

play sound sfx_bushes_v2

t_t "Кусты сотряслись от того, как я ломанулся в них обратно." with hpunch

show d_f at fear

show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100 with Dissolve(0.5)
play sound sfx_bushes_v2
t_t ear surprised "С громким хрустом веток я снова прыгнул в кусты и схватился за пиджак Дзиндзо, пытаясь затащить его за собой. Тот упёрся на месте."

d_f melancholy "Господин Тайда, разве не я должен говорить МАНДАРИН 🍊, МАНДАРИН 🍊?!"

t_t "Краем глаза я замечаю, что отец услышал наше копошение и собирается повернуться на звук. "

play sfx sfx_bushes_v2
t_t "В ту же секунду я ныряю обратно в живую изгородь. "

show dad right at move_on_scene(xalign=0.5)

play sound sfx_bushes_v2

dad "Тайда, это ты шумишь?"

show d_f pose2 asharashen

t_t hz cry_sad "Дзиндзо впал в ступор и стоял как столб с дебильным выражением лица, а я ловил испанский стыд в метре от него."

dad "Мне звонил директор вашей школы. Он сообщил мне, что с большой вероятностью ты останешься на второй год."

dad "Я очень разочарован в тебе, сын."

show d_f pupupu

t_t thinking asharashen "Дзиндзо начал активно кивать башкой, соглашаясь с отцом. "

dad "Чего ты киваешь, шею заклинило?"

d_f neutral "Нет, у меня стоит защита от короткого замыкания, а также я отлично смазан!"

t_t asharashen "Отец посмотрел на Дзиндзо как на умалишенного, но не прокомментировал это. "

t_t hz cry_sad "Я еле слышно подвывал в кусте, кусая руку, чтобы не закричать от ужаса."

dad "Знаешь что. Я научу тебя жизни! Не хочешь учиться? Вперед работать!"

dad "У моей знакомой открылся ларёк с фаст-фудом, и ей нужна реклама. Вот иди и помоги ей с раздачей листовок."

dad "А потом расскажешь мне, так ли хороша жизнь без образования, и хочешь ли ты так работать всю жизнь!"

t_t thinking asharashen "Отец многозначительно посмотрел на своего робо-сына."

dad "Марш на площадь!"

d_f pose1 neutral "Да, гос..."

#sfx
play sfx sfx_bushes_v2
play sfx2 sfx_scream
t_t "Я издал из кустов звук раненой цапли, чтобы отвлечь внимание отца."

d_f "...подин отец."

t_t asharashen "За моими притворными криками отец не услышал ничего лишнего."

t_t "Он присмотрелся к кусту, пытаясь понять, что за бешеная птица там сидит. "

t_t thinking_hard "За это время я успел помолиться всем богам, которых знал, некоторым по два раза."

show dad left at move_on_scene(xalign=1.5)

t_t "Отец помахал андроиду рукой и через калитку вошел домой."

hide bush4 onlayer screens with Dissolve(0.5)

play sfx sfx_bushes
t_t ear surprised "Я немного подождал, пока всё утихнет, и вылез."

t thinking thinking_hard "Ну вот, теперь домой идти нельзя. Придется идти туда. Но что бы придумать..."

t hz wtf "Прятаться нормально ты не сможешь. Да и отец уже видел тебя в школьной форме."

t thinking think "Так что ты пойдешь в открытую, а я буду скрываться. Только не вздумай чудить!"

t "И перестань говорить \"Господин\", это палевно!"

d_f pose1 neutral "Вас понял, сэр!"

t ear confused "Похоже вместо искусственного интеллекта мы создали натуральную глупость."

scene bg_black with Dissolve(1)
call screen time_passed("Десять минут спустя")

show bg_square with Dissolve(1)
play music music_comedy_loop fadein 0.5 fadeout 1.0 loop
show d_f pose1 school relief right at enter_scene(from_left=True, xalign=0.2)

t_t ear neutral summer_norm "Мы отправились к площади. Дзиндзо шёл вприпрыжку, явно наслаждаясь своей первой прогулкой."

t_t "Ему не нужно дышать, чтобы жить, но по всему его виду было похоже, что он пытается надышаться окружающей обстановкой."

t_t thinking think "Со слов отца я знал лишь, что его знакомая работает в самом отдаленном уголке центральной площади, в который почти никто не заходит. "

show d_f at move_on_scene(xalign=0.8)

show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100

t_t neutral "На месте мы разделились. Я спрятался неподалёку, а Дзиндзо пошёл к ларьку. "

t_t "Как оказалось, хозяйка лавки жарила кальмаров и подавала их на палочке."

show d_f at move_on_scene(xalign=1.5)

t_t "На некоторое время Дзиндзо скрылся от моего взгляда. "

t_t ear careless "Но так как всё шло гладко, я позволил себе отвлечься на мемы в телефоне и некоторое время мирно листал ленту. "

t_t surprised "Внезапно площадь огласил громкий голос:"

d_f "ПОДХОДИ ПОКУПАЙ ГОРЯЧИЙ КАЛЬМАР!" with vpunch

t thinking asharashen "Боже, что???!"

t_t "Я высунулся из своего укрытия и ошалел. "

stop music fadeout 0.5

call dz_calmar_scene from _call_dz_calmar_scene

#show squid with Dissolve(1)
scene bg_square
play music music_comedy_loop fadein 0.5 fadeout 1.0 loop

t_t ear neutral "Народ, довольный представлением, потихоньку рассосался."

t_t "Я подкрался к самому ларьку, чтобы подслушать разговор робота со знакомой отца."

show seller left at c_right
show d_f pose1 neutral right at c_left
with Dissolve(1)

play music music_main_theme_2_v3 fadein 0.5

seller "Тайда, ты настоящий молодец. Так самоотверженно взялся за дело! Я не ожидала от тебя такого."

seller "Зря твой отец так плохо о тебе отзывается. Да так ты любые горы свернешь!"

show d_f pose2 neutral

t_t "Дзиндзо сделал небольшой поклон, отдал шапку кальмара и собрался уходить."

show d_f pose1 happy left at move_step()

d_f "До свидания, рад был помочь!"

t_t hz wtf "Я зашипел на него из-за угла:"

t dissatisfied "Деньги!.."

show d_f right at move_step(xoffset=100)

d_f pose2 asharashen "А, ой, точно."

t_t "Хозяйка, удивлённая его бескорыстием, щедро вознаградила \"меня\", добавив немного сверху."


hide bush4 onlayer screens 
hide seller 
with Dissolve(1)
show d_f left pose1 neutral at move_step()

$ renpy.music.set_volume(0.4, delay=0.5, channel="music")
t_t thinking thinking_hard "Обратно домой мы добирались тихо и молча. Дзиндзо пытался радостно мигать своими светодиодами под пластырями, а я шел как мрачная туча."

scene bg_black with Dissolve(1)
call screen time_passed("Десять минут спустя")

show bg_near_home with Dissolve(1)

t_t "Мы пробрались на задний двор моего дома через дыру в заборе и на цыпочках проползли в мою комнату незамеченными."

stop music fadeout 1.0
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")

scene bg_black with Dissolve(1)
$ renpy.pause(0.5)
#Room Evening.JPG
scene bg_living_room 
play music music_main_theme_3_v2 fadein 0.5 fadeout 1.0 loop
show d_f pose1 neutral right at center
with Dissolve(1)

t_t hz cry_sad summer_norm "Этот день наконец-то закончился. "

t_t thinking tired "Я рухнул на кровать, совершенно лишенный сил. Дзиндзо сел за мой компьютерный стол и завис в недвижимой позе. "

t_t thinking_hard "Немного отойдя от потрясения, я углубился в свои мысли. "

t_t "Всё это было не зря. "

t_t neutral "Мы сделали невозможное! И самое приятное только начинается!"

t_t ear confused "Да, он неловкий. Странный. Говорит чушь. Но тест он прошел, хоть и опозорил меня. "

t_t thinking genius "Кацуми мастер своего дела — запрограммировать робота за такой короткий срок на хоть сколько-нибудь адекватное поведение — уже гениально."

t_t thinking thinking_hard "К жизни он в целом приспособлен. Для школы сойдет — там и так моей репутации уже ничего не может навредить, её нет."

t_t ear silly "Так что пусть шурует завтра вместо меня. И вообще..."

show d_f left with Dissolve(0.5)

t thinking genius "Дзиндзо, сделай за меня домашнее задание."

d_f happy "Да, конечно!"

show d_f pose2 neutral

t_t ear neutral "Робот достал учебники и тетради из моей сумки. "

t_t "Одного взгляда на уравнение с тремя неизвестными было достаточно." 
t_t "Пара автоматических движений рукой — и половина тетрадного листа исписана решением. "

t_t thinking cunning "С довольной улыбкой я начал проваливаться в сон."

t "Теперь всё наладится, да?.."

d_f "Однозначно, что бы то ни было!"

t "И правда..."

t_t genius "Я счастливо улыбнулся. "

t_t thinking sleepy "Сон одолел меня."

$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black with Dissolve(1)
call screen time_passed("На следующее утро")

#темный экран
$ renpy.pause(1.0)

scene bg_living_room with Dissolve(1)
#темный экран
#Room Evening.JPG
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
t_t thinking sleepy naked "Я проснулся от странного шороха в комнате."

t_t thinking_hard "В глаза светило солнце из окна. "

t_t think "Ослеплённый и ничего не понимающий, я несколько секунд наблюдал за собой со стороны."

show d_f neutral pose3 left at c_left with Dissolve(0.5)

t_t "Вот я стою у стола, складываю в рюкзак тетради, учебники и какой-то завтрак."

show d_f right at move_step(xoffset=200)

t_t "Затем я подхожу к своей кровати... И говорю:"

d_f smile "Доброе утро, господин Тайда."

d_f "Бутерброды на столе, я сходил за колой. Вы можете приступать."

t_t neutral_4stena "С совершенно невдупленным видом я лёжа поднялся на локтях."

t_t think "Что вчера произошло?..."

t asharashen "А! Я вспомнил..."

t hz smile "Ну, привет! За бутерброды... Э-э... Спасибо."

t_t thinking tired "Продрав глаза и потупив немного в стену, я встал с кровати и потянулся к школьной форме."

d_f neutral "Тайда, подождите, пожалуйста. Она мне нужна. Через девять минут и сорок две секунды мне нужно будет выходить в школу."

t_t asharashen "Осознание этого факта ошарашило меня. "

t "Так, подожди. Приступать к чему?"

t_t "Не успел я договорить, как заметил свой включенный пк, кружку с колой и тарелку с бутербродами."

d_f smile "Чтобы стать знаменитым киберспортсменом, нужно правильно питаться и много тренироваться."

t_t hz cry_sad "На глазах выступили слезы. Никогда обо мне ещё никто так не заботился."

t_t "Не веря своему счастью, я поплелся к компьютеру."

t_t thinking cunning "И включил свою любимую ММО РПГ \"Кабанье проклятье\"."

show d_f pose1 neutral school with Dissolve(0.5)

t_t "Дзиндзо набросил шарф, натянул перчатки, и приготовился выходить."

menu:
    "Остаться ненадолго и понаблюдать, во что играет господин Тайда.":
#        d pose2 melancholy "Он играет во что-то странное, но выглядит интересно."
        play music music_yay fadein 0.5 fadeout 1.0 loop
        call test_clicker_game from _call_test_clicker_game
        stop music fadeout 1.0
        d_f "Господин, уверен, что вы отлично проведете время. До встречи вечером!"
    "Сразу уйти":
        d_f "Простите, я спешу."
        #d pose2 asharashen "Я уже опаздываю, лучше поспешить в школу."

#Мини-игра кликер по кабану, за 100 кликов ачивка, или кнопка exit без ачивки до 99 кликов. 

#Ачивка "Кабанье проклятие"


#Мини-игра кликер по кабану, за 100 кликов ачивка, или кнопка exit без ачивки до 99 кликов. 
#Ачивка "Кабанье проклятие"
# "Господин Тайда, а у вас отлично получается!", "
# "Подождите, и это правда всё, что нужно делать?""
# "Ваши развлечения весьма специфичны, господин Тайда." "
# #И потом после сотни кликов 
# "Кажется я ещё недостаточно понял, как нужно развлекаться по-настоящему"."
pause 0.5
show d_f pose1 neutral at move_on_scene(time=3.5, xalign=1.5)
pause 3.0
play sfx sfx_open_door
"Дзиндзо покинул комнату и ушел на занятия."
stop music fadeout 1.0
scene bg_black with Dissolve(1)
$ renpy.pause(1.0)
$ set_character_dzinzo()
scene bg_near_home with Dissolve(1)
play music music_main_theme_3 fadein 0.5 fadeout 1.0 loop

d_t pose1 neutral school "Я шел в направлении школы со скоростью 7,8 километра в час. "

d_t "По моим расчётам, прибуду в аудиторию класса 2-B в 8:23. Приемлемо."

d_t happy "Пунктуальность важна, чтобы не подвести господина Тайду."

d_t pose2 sad "По дороге я удивлялся многим вещам. Зачем птицы поют о грядущем конце света?"

d_t pose1 thinking "Почему люди идут сонными, ведь можно лечь в 22:00 и проснуться в 6:00 бодрым и отдохнувшим?"

d_t pose2 melancholy "Почему на улице есть бездомные люди, если можно просто купить дом?"

d_t melancholy "Несмотря на то, что в мою память заложено много баз данных, некоторые вещи я не могу объяснить."

d_t neutral "Согласно статье о поведении среднестатистического японца, а также выжимке из научной диссертации по этике и правилам морали... "

d_t "...с людьми, которых ты видишь первый раз в течение дня, ты должен поздороваться."

d_t pose1 happy "В течение всего своего пути я махал руками своим попутчикам и всем тем, кто шел мне навстречу. "

d_t pose2 melancholy "На улицах было удивительно людно, и температура моего тела поднялась в среднем на 1,5 градуса от прилагаемых усилий по задаче \"Приветствие\"."

d_t "Дабы немного охладить температуру и не вызывать критического перегревания процессора, я принял решение здороваться только с 57 знакомыми господина... "

d_t "...и ещё с 332 учениками средней школы, которые были включены в базу данных."

show bg_class_room with Dissolve(1)

$ renpy.pause(0.5)

d_t neutral "Задача \"Вовремя прибыть в аудиторию класса 2-B\" успешно выполнена."

d_t "Я присел за парту, на которой перочинным ножом было вырезано имя Тайда Нингё."

d_t "Класс постепенно наполнялся учениками."

d_t pose1 cunning "В моем процессоре одновременно рассчитывались секунды до школьного звонка, количество вошедших в класс и..."

d_t "...майнился биткоин для карманных расходов господина Тайда."

d_t "Я вывел простой алгоритм поведения:"

d_t "Если мимо моего местоположения проходит человек женского пола, я должен сгенерировать комплиментарное замечание."

d pose1 happy "Вау, ты сегодня очень красивая!"

d "Какая ты милашка!"

d "Бантик на твоих волосах выглядит потрясающе!"

d_t neutral "Если это человек мужского пола, допустимо приветственное слово, рукопожатие и в некоторых случаях объятие."

#одноклассник
play sfx sfx_giggles_v2
$ speak_as("Одноклассник", "Тайда, с тобой всё нормально?")

d_t neutral "Согласно собранным статистическим данным, уровень моей привлекательности постепенно поднимался. "

d_t pose2 neutral "Человеческий смех — позитивная эмоция, раз мои действия вызывают смех — значит, я делаю всё верно."

show k pose2 neutral right at Transform(xalign=0.5, yalign=1.0)
show den left at Transform(xalign=0.8, yalign=1.0)
show h left at Transform(xalign=1.0, yalign=1.1)
with Dissolve(0.5)

d_t melancholy "Краем глазного яблока я заметил, что в класс зашли мои создатели — госпожа Кацуми, господин Денис и господин Хикару. "

d pose1 happy "Здравствуйте, мои друзья!"

show k pose1 confused
show h explain surprised
show den awesome surprised

d_t "Их лица выражали сложные эмоции, которые я не мог проанализировать."

hide k
hide h
hide den
with Dissolve(0.5)

play sfx sfx_bell
d_t neutral "Не успев произвести положенный в таких случаях small talk, мы услышали школьный звонок. "

pause 1.0

d_t neutral "Первым уроком была история."

show teacher neutral left with Dissolve(1)

teacher "Итак, повторяем мифологию, первый вопрос: Нерон выиграл Олимпийские игры в: музыке, театре или гонках на колесницах?"

d_t cunning "Я молниеносно поднял в воздух свою правую верхнюю конечность."

show teacher surprised right

d_t "Учитель удивленно повернулся в мою сторону."

teacher neutral "Да, Тайда?"

menu:
    "В театре." if False:
        ""
    "В гонках." if False:
        ""
    "В музыке." if False:
        ""
    "Во всех перечисленных.":
        teacher surprised "Эээм... Молодец, всё верно."

d_t relief "Хорошо, что в моей памяти уже есть полное собрание мифов в 8 томах."

teacher sad "Хорошо, тогда следующий вопрос:"

teacher neutral "Чем тоталитаризм отличается от авторитаризма?"

play sfx sfx_hit
d_t very_happy "Я чуть не опрокинул парту в попытке быть замеченным учителем." with vpunch

teacher surprised "Тайда, неужели ты подготовился к уроку?"

menu:
    "Власть принадлежит духовенству." if False:
        ""
    "Контролем за общественным мнением.":
        teacher "Действительно, всё так."
    "Законы принимаются общим голосованием." if False:
        ""

d_t neutral "...подсказывает мне книга \"Философия права\" за авторством Раймонда Уакса от 2014 года."

teacher smile "Вопрос на засыпку. Июль и август, в которых 31 день, названы в честь двух исторических личностей, каких?"

d_t happy "Обе мои руки выстрелили в воздух."

menu:
    "Уриэль Септим VII и Балгруф старший." if False:
        ""
    "Юлий Цезарь и Октавиан Август.":
        teacher surprised "Всё верно!"
    "Юлиана и Августина III." if False:
        ""

teacher happy "Ну Тайда, ты меня удивил. Молодец. Я рад, что ты взялся за ум."

play sound sfx_crowd
d_t pose2 neutral "В классе зашептались. Я встал и поклонился:"

d "Сенсей, спасибо, что верите в меня!"

hide teacher with Dissolve(1)

play sfx sfx_bell
pause 0.5
d_t pose1 cunning "Урок закончился, и я ощутил прилив удовлетворения от прекрасно выполненной задачи \"Успешно притворяться Тайдой\". "

show k pose1 confused right at trio_left
show den idle nervous left at trio_center
show h idle neutral left at trio_right
with Dissolve(0.5)

d_t neutral "Мои сенсоры поймали пристальные взгляды друзей: Дениса, Хикару и Кацуми."

den awesome surprised "Тайда, ты что-то подозрительно веселый сегодня. Ты случайно не перегрелся?"

d_t "Я повернулся к Денису с заранее отработанной улыбкой:"

d happy "Всё отлично! Просто выспался наконец-то."

show h surprised

d_t "Хикару поправил очки и внимательно меня оглядел:"

h "Ты — и выспался? Кто ты и что сделал с Тайдой?"

show k angry

d_t "Кацуми скептически нахмурилась:"

k "И почему у тебя всё лицо в пластырях?"

d_t neutral "За эту ночь я успел скачать и проанализировать всю переписку господина Тайды."

d_t cunning "Теперь в моей голове шестнадцать гигабайт мемов. Я официально опаснее любого форумного тролля."

d neutral "Вчера я купил те самые сухари, что так расхваливал Денис..."

den happy "С хреновым вкусом?! Ух, мои любимые! Как тебе?"

d relief "Это было так плохо, что даже хорошо. Вот и обсыпало прыщами, пришлось клеить пластыри."

show k pose2 annoyed

d_t neutral "Кацуми фыркнула:"

k "Ну хоть тут ты остался прежним..."

show k neutral
show den neutral
show h neutral

d_t relief "Друзья обменялись взглядами и решили не продолжать допрос. Я выдохнул, хоть и не нуждался в дыхании."
stop music fadeout 1.0
scene bg_black with Dissolve(1)

$ renpy.pause(1.0)

scene bg_robo_class_room 
play music music_comedy_v2 fadein 0.5 fadeout 1.0 loop
show i neutral right at Transform(xalign=-0.25, yalign=1.0)
show den awesome neutral right at Transform(xalign=0.2, yalign=1.0)
show k pose2 didnt_understand right at Transform(xalign=0.75, yalign=1.0)
show h idle neutral left at Transform(xalign=1.05, yalign=1.0)
with Dissolve(1)
#Robo-Class Room.JPG

d_t pose1 neutral "После уроков мы пришли в кружок робототехники. Кацуми осмотрелась и замерла."

pause 1.0 

show i interested
show den idle nervous
show h explain asharashen

show k at fear()
k asharashen "А где Дзиндзо? Он же тут сидел вчера."

d_t pose2 asharashen "Все мои сенсоры взвились в боевую тревогу — я уже почти крикнул \"МАНДАРИН 🍊\", но вспомнил, что Тайда далеко."

d_t "Не уверен, что в этом состоянии Кацуми возможно победить в рукопашном бою, не выдав при этом себя. Нужно действовать мирно и осторожно!"

show i smug

d pupupu "Ааа, это... Вчера ночью я заметил, что у него остались недочеты в сборке. Вы бы видели, как плохо было затянуто правое колено. Дорога приключений ему с таким не светит."

d "В итоге, пришлось укатить его на телеге домой. А после я уснул за домашкой. Завтра... А нет, в понедельник, притащу его обратно!"

show h idle neutral
show den neutral

k pose1 angry "Он действительно был не до конца затянут, но тебе стоило посоветоваться с нами..."

d neutral "Да, простите. Но не стоит отчаиваться, у нас же ещё осталась недоделанная паштетомазка!"

show h at Transform(xalign=1.15, yalign=1.0)
show den sad

h explain neutral_talk "Действительно. Мы забросили её почти на неделю. Может быть, сейчас, со свежей головой мы сможем что-то придумать."

show i dreamy

d_t "Всё это время, преподаватель смотрела на меня и очень загадочно улыбалась."

d_t "Потом она еле слышно пробубнила себе под нос:"

show i at joy()
i happy "Вот оно как... Ха-ха... Это будет интересно."

d_t "И громко сказала:"

i smug "Ребята, доставайте чертежи и платы. Сегодня я получу свой идеальный бутерброд с паштетом!"

i tricky "А раз Юмички сегодня не видать, то сделаете его мне вы! Я на вас рассчитываю."

hide i
hide k
hide den
hide h
with Dissolve(1)

d_t "Денис и Хикару без особого энтузиазма начали выкладывать вещи на стол, а Кацуми пошла включать компьютер. "

d_t pose1 cunning "Господин Тайда не раз скептично относился к этой разработке. Это будет отличной возможностью поднять рейтинг господина."
 
d_t neutral "На данный момент на мне нет никаких критических задач. Стоит попытаться помочь остальным."

show den awesome sad left at center with Dissolve(1)
play music music_comedy_loop fadein 0.5

d pose2 neutral "Денис, у тебя перегрев дорожек — снизь температуру жала на 15 градусов. И ты подключил электролит на 6,3 В в схеме с выбросами до 9?"

d "У тебя получилась импровизированная бомба, а не конденсатор."

show den awesome surprised

d_t "Денис пожал плечами:"

den "Хм, а ты прав. Я думал, пронесёт..."

hide den awesome sad left at center with Dissolve(1)
pause 1.0
show h idle neutral left at center with Dissolve(1)

d_t pose1 neutral "После, я посмотрел в сторону Хикару. К тому моменту он уже полностью закопался в чертежах, заглядывая то в один, то в другой и явно не понимая, что идет не так. "

d happy "Хикару... Могу я взглянуть? Если не возражаешь."

show h idle surprised

d_t neutral "Он мельком посмотрел на меня, чуть удивленно, но затем протянул чертёж:"

h neutral "Тут вроде бы всё нормально, но у манипулятора возникает люфт, и я не могу понять, почему."

d_t pose2 melancholy "Я изучил схему. Через 1.3 секунды решение было уже наготове:"

d neutral "Я заметил, что ты использовал шарнир с допуском 0.15 мм — это стандартно, но в связке с приводом, у которого износ начинается после 10 циклов..." 

d "...люфт будет увеличиваться экспоненциально."

show h explain thinking

d_t "Хикару нахмурился ещё сильнее, но уже с интересом:"

d "Можно попробовать перейти на прецизионный подшипник с нулевым допуском по оси Y. У нас где-то как раз такой завалялся, он будет гораздо стабильнее."

h neutral_talk "И ты это понял с первого взгляда?"

d_t pose1 relief "Я пожал плечами, стараясь казаться скромным:"

d "Я просто очень хотел помочь."

show h idle neutral
pause 0.5
hide h with Dissolve(1)

d_t neutral "Итак, похоже дела идут хорошо. Настало время пойти посмотреть, что там у Кацуми."

show k pose1 cunning left at center with Dissolve(1)

d_t "Я направился к Кацуми. Она сидела с наушниками, уставившись в монитор, и лихорадочно стучала по клавишам. "

d_t "Каждые 10 секунд на экране был то график распределения нагрузки, то IDE с открытым кодом, в котором строчка за строчкой мигали логические условия."

d pose2 neutral "Кацуми... Если хочешь, могу взглянуть на твой код."

k angry "В любой другой ситуации я бы не подпустила такого лентяя, как ты, и на 10 метров к моему коду. Но, возможно, мне действительно нужен взгляд со стороны."

d_t pose2 sad "Я встал позади неё и начал читать."

d "В функции {i}on_spread_complete(){/i} условие {i}if target or not target == None:{/i} приводит к тому, что паштет мажется даже на стол. Иногда — по диагонали."

show k pose2 didnt_understand right

d_t "Кацуми на мгновение оторвалась от клавиатуры и обернулась:"

k pose1 confused  "Так цель же есть. Не {i}None{/i}, значит можно мазать. Не тупи."

d_t melancholy "Я провёл повторный анализ. Действительно. Вероятно, я ошибся из-за недостаточной визуальной контрастности в теме редактора."

d neutral "Ты совершенно права. Спасибо, что поправила. Давай подумаем ещё раз."

d "Но {i}target{/i} иногда — это просто координаты стола. А не хлеб. Мы не проверяем, что именно под манипулятором. {i}if target.type == 'bread'{/i} или хотя бы {i}if isinstance(target, Bread){/i}."

show k pose1 confused left

d_t "Кацуми нахмурилась, затем проверила — и молча кивнула. Потом, как бы между прочим, буркнула:"

k cunning "Хм... Ну, неплохо, особенно для тебя."

hide k left at Transform(xzoom=1.0) with Dissolve(1)

d_t "Работа над устройством закипела полным ходом. "
$ renpy.music.set_volume(0.3, delay=0.5, channel="music")
scene bg_black with Dissolve(1)
$ renpy.pause(1.0)

d_t "И вот, спустя всего час, мы были готовы опробовать новый прототип."

scene bg_robo_class_room
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
show i smug right at Transform(xalign=-0.25, yalign=1.0) 
show den idle neutral right at Transform(xalign=0.2, yalign=1.0)
show k pose2 neutral right at Transform(xalign=0.75, yalign=1.0)
show h idle neutral left at Transform(xalign=1.05, yalign=1.0)
with Dissolve(1)

d_t "Благодаря моим молниеносным подсказкам в этот раз у ребят не было ни единого шанса на ошибку."

d_t pose2 melancholy "Манипулятор пригнулся над банкой паштета с видом хирурга, который собирается нарисовать Мону Лизу скальпелем. "

show h explain neutral

d_t "Хикару, деловито щёлкнув секундомером, объявил: "

h neutral_talk "Три... {w=0.5}Две... {w=0.5}Одна..."

play sfx sfx_tiktak loop
show i neutral
show k pose1 worried
show den sad

d_t pose1 relief "И вот он, момент истины! Робо-рука берет нож, плавно опускает его в банку с паштетом, поднимается и отправляется к заранее заготовленному кусочку хлеба."
stop music fadeout 3.0

play sound sfx_pressure
d_t neutral "Первый мазок. Идеально ровная дорожка. "

d_t "Второй мазок. Такой гладкий, что в нем отражаются лампочки на потолке."

show den idle asharashen

d_t pose2 asharashen "Третий... Денис задохнулся и начал покачиваться. Я на всякий случай подготовил алгоритм \"Поймай падающего пайщика\", но он удержался, схватившись за стол."

show den nervous
show i very_angry

d_t pose1 neutral "Изуми‑сенсей наклонилась вперёд, её пальцы сжимали чашку кофе так крепко, что если бы у кофе был страх, он бы заплакал."

d_t "Манипулятор в последний раз прошёл по хлебу и замер в позе победителя. На ломтике лежал слой паштета толщиной ровно 2,5 мм — как мы и рассчитывали."

stop sfx
play music music_main_theme_3 fadein 0.5

i asharashen "Ребята! Это же... Идеальный бутерброд!"

show i happy
show k pose2 cunning
show den awesome happy
show h idle neutral

d_t "Все разом вздохнули, будто кто‑то вернул нам кислород."

show h explain neutral

stop sfx 
play sfx sfx_ui_click
d_t "Хикару, сохраняя достоинство, щёлкнул секундомером ещё раз и улыбнулся:"

h idle happy "Ровно девять секунд намазки."

d_t pose1 relief "Я стоял чуть в стороне, пока ребята радостно обнимались, и чувствовал, как мои алгоритмы самооценки заполняются тёплыми значениями." 

d_t neutral "Это их смех. Их радость. Их признание. "

scene bg_black with Dissolve(1)

$ renpy.pause(1.0)

scene bg_school_entrance with Dissolve(1)
play music music_main_theme_3_v2 fadein 0.5 fadeout 1.0 loop
d_t pose1 neutral "Снова сумерки... Каким бы хорошим ни был день, он всегда заканчивается."

d_t "Пора было расходиться по домам. "

d_t "Ребята уже ушли, а я дожидался нужного момента на крыльце."

d_t pose2 sad "Во время занятия в кружке Кацуми обмолвилась, что Юми обижена на господина Тайду, поэтому я обязан исправить ситуацию."

d_t neutral "Какой бы ни была причина обиды, я должен поднять его рейтинг в глазах всех!"

show u open neutral left at c_right

d_t "Юми появилась на пороге школы. "

show u thinking right at move_step(xoffset=50)
$ renpy.pause(0.5)
show u thinking left at move_step(xoffset=-50)

d_t "Я наблюдал, как она неловко переминается с ноги на ногу, пытаясь поправить ботинок. "

show u closed cute

d_t "Пара неудачных движений, и девушка падает на землю." with vpunch

d_t pose2 asharashen "Я быстро подошел помочь. Так быстро, что превысил человеческую скорость."

show u greeting offended left with Dissolve(0.5)

d_t "Юми приняла протянутую мне руку и поднялась."

show u open embarrassed 

d_t "Лицо её выражало милое наивное недовольство вместе с недоумением."

u "Конечно, спасибо, но я сама бы справилась."

u open thinking "Как ты подбежал так быстро?"

d_t asharashen "Если бы я мог покрыться холодным потом, как говорят в словаре устойчивых выражений, это произошло бы прямо сейчас. Фатальная ошибка."

d pose1 cunning "Это был выброс адреналина! Дело обычное... В Google поищи!"

d "И вообще..."

d_t pose2 sad "Я склонился в поклоне и сложил руки лодочкой в извиняющемся жесте."

d melancholy "Прости! За что бы то ни было!"

show u closed neutral right at step_right

d_t "Юми сложила руки на груди и отвернулась. "

u "С чего ты взял, что что-то не так?"

d_t pose2 sad "Ситуация явно серьезная. Проблема не решается. "

d melancholy "Я виноват! Во всём! Прости, пожалуйста!"

show u left at step_left

u cute"Ну и в чём всём??" 

d_t neutral "По виду красных щёк подруги было понятно, что она готова простить господина Тайду, но хочет ещё немного его помариновать."

d sad "В том, что я натворил!"

d_t pupupu "Я упал на землю в театральном жесте отчаяния и потянулся к её ботинку."

show u greeting offended at move_step(xoffset=50)

d_t "Девушка вскрикнула и отпрянула."

u closed cute "Ладно, ладно, всё в порядке! Встань, пожалуйста!"

u neutral "Я тебе помогу!"

d_t "Юми подала руку. Поднявшись, я не спешил отпускать её, чем крайне смутил девушку. Работает!"

d sad "Скажи мне, чем я могу загладить свою вину?"

show u touched

d_t "Переминаясь с ноги на ногу и потупив взгляд, подруга скромно проговорила:"

u neutral "В прошлый раз мы с папой так и не разобрали гараж, и собирались заняться этим сегодня. Поможешь?"

d pose1 happy "Легко!"

show u open thinking right at move_on_scene(xalign=2.0)

d_t "Закатав рукава рубашки и пиджака, я схватил Юми за руку и потащил в сторону её дома, локацию которого я заранее скачал из телефона господина."
$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black with Dissolve(1)

pause 1.0

$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
scene bg_near_home 
with Dissolve(1)

show u open thinking right at enter_scene(from_left=True, xalign=0.1)

d_t neutral "Мы быстро пробежали несколько улиц до дома девушки и оказались у калитки небольшого коттеджа."

show u embarrassed

d_t "Юми пыталась отдышаться и поправить волосы, я же был наготове к выполнению важной задачи и уже активно названивал в дверной звонок."

show b_1 left  at c_right
show u thinking
with Dissolve(1)

d_t "На пороге появился силуэт отца подруги."

d_t "Тот недоверчиво прищурился, увидев мою голову и макушку Юми за калиткой. "

show u closed cute

b_1 "Опа, нарисовался."

show b_1 at move_on_scene(xalign=0.5)

d_t "Мужчина не спеша подошел и отворил калитку."

d_t pose2 neutral "Я крепко пожал ему руку."

d "Здравствуйте, господин Содзиро!"

d_t "Отец подруги оценил крепость рукопожатия и кивнул."

b_1 "Дочура рассказывала мне о тебе. Называй меня просто Батя."

$ b_1.name = "Батя"

show b_1 right at step_right

d_t "Я кивнул и пошел вперед него во двор."

d_t "В деловитом жесте, сложив руки на груди, я припарковался у гаража и осмотрел его:"

d pose1 happy "Так, и что необходимо сделать?"

u closed neutral "Ой, Тайда, ты вот так сразу? Ну тут надо, короче, отсортировать, прибраться, смазать инструменты..."

u touched "Ты знаешь, мне так неловко, давай я сама!.."

d_t neutral "Проигнорировав лишнюю информацию и слова паразиты, я сразу приступил к делу."

d_t "Необходимо было запереть гараж, чтобы люди ничего не заподозрили."
scene bg_black with Dissolve(1)
hide u
hide b_1
scene bg_garage_dirty
with Dissolve(1)

d_t "Заскочив в помещение, я защелкнул щеколду."

play sound sfx_throwing_things_around

d_t cunning "Так... Отсортировать? Выполнено."

play sound sfx_throwing_things_around
d_t "Прибраться? Помыть поверхности, разложить вещи по полкам, повесить все ключи на их место. Выполнено!"

play sound sfx_throwing_things_around
d_t "Вынести мусор? Выкинул 3 моментально собранных мешка в окошко под потолком."

show b_1 left at Transform(xalign=1.2, yalign=1.0) with Dissolve(0.5)
$ renpy.pause(0.5)
play sfx sfx_hit
show b_1 at fear
$ renpy.pause(0.5)
show b_1 at move_on_scene(time=0.5, xalign=1.5)

d_t pose2 asharashen "В процессе чуть не пришиб Батю Юми, который попытался заглянуть внутрь."

hide b_1

d_t pose1 surprised "Так, так... Инструменты."

d_t "Музыкальных инструментов нет в моей базе данных, это плохо."

d_t thinking "Пришлось немного притормозить."

d_t "Подключаюсь к вай-фаю в доме Юми. Любопытно, пароль 1234_love_taida_durak."

d_t relief "Стоит отдать должное, пароль достаточно надежен." 

d_t "Простенькому компьютеру потребовалось бы около 19028403758387460000 лет на взлом перебором."

d_t cunning "Вот только прошивка роутера настолько стара, что пароль обойти было проще простого."

d_t "Загружаю библиотеку..."

d_t thinking "Guitars: Design, Production, and Repair за авторством Jim Donahue..."

d_t "Основы правильных занятий на гитаре от Andreas J..."

d_t "Troy Stetina: Total Rock Guitar..."

d_t neutral "Пролистав в своей голове около тысячи страниц, я получил подробное понимание, что делать с этими инструментами."

d_t "Капнуть масло, растереть. Отполировать. Заменить струны. "

show bg_garage with Dissolve(1)

d_t happy "Готово!"

show b_1 right at enter_scene(time=3.0, from_left=True, xalign=0.2)
$ b_1.name = "Батя"

d_t neutral "В гараж через второй вход зашел отец Юми."

b_1 "Тайда, что ты..."

d_t "В этот момент я ставил последнюю, уже зачищенную, гитару на подставку в идеально чистом гараже."

d_t "Батя застыл в изумлении."

show u closed cute right at enter_scene(from_left=True, xalign=0)

d_t "За его спиной замаячила покрасневшая от стыда Юмичка."

d happy "Благодарю за возможность помочь!"

d "Всего добр..."

b_1 "Ты уже уходишь? Спасибо большое, я удивлен твоей ловкостью и скоростью."

b_1 "Извини, что пришлось делать это одному. Мы, если честно, немного не успели..."

show b_1 at move_on_scene(xalign=0.65)
pause 2.0
show b_1 left

d_t neutral "Родитель подруги увидел ухоженные инструменты."

b_1 "Ты разбираешься в гитарах? Даже струны поменял!"

d_t cunning "Отличный шанс, чтобы показать себя! Господин Тайда будет рад."

d neutral "Да, могу процитировать любую страницу любой книги о гитарах. Какая вас интересует?"

d_t "Батя в удивлении начал хватать воздух ртом в попытках ответить. Я не дал ему такой возможности."

d relief "А лучше покажу."

stop music fadeout 1.0
call dzinzo_rock_scene from _call_dzinzo_rock_scene

#цг ргг играет на гитаре
#музыка роцка
#show guitar_solo with Dissolve(1)

show u open surprised at c_left
show b_1 left at Transform(xalign=0.65, yalign=1.0)
$ b_1.name = "Батя"

d_t cunning "Напоследок я перекинул гитару через плечо и ловко установил её на подставку. "

b_1 "Сынок, это... Божественно. Пойдём в дом, расскажешь мне, где ты такому научился."

b_1 "Я во времена своей молодости тоже так умел. Сейчас расскажу..."

show u closed touched at step_right
play music music_main_theme_3 fadein 0.5 fadeout 1.0 loop

d_t neutral "Юми суетилась рядом, что-то тихо говорила заикаясь и тянула меня за руку в дом."

d_t "Остаток вечера мы провели на кухне их небольшого, по человеческим меркам уютного, коттеджа."

d_t "Отец Юми рассказывал, как играл в некогда известной группе, какие стадионы они собирали и как он скучает по тем временам."

d_t happy "А также, что сегодня я смог на пару мгновений вернуть его в молодость."

d_t very_happy "Успех! Операция завершена. Пора ретироваться."

d neutral "Что ж, спасибо за гостеприимство. Мне необходимо уйти."

b_1 "Ты не останешься у нас ещё немного?"

d_t thinking "Поиск отмазки... Поиск достаточно хорошей отмазки, чтобы получить плюс в рейтинг."

d neutral "К сожалению, не могу, мне необходимо сегодня:"

d pose2 pupupu "1. Сходить на подработку."

d "2. Посетить подготовительные курсы для сдачи экзаменов."

d pose1 relief "3. Сдать кровь и плазму для нуждающихся."

d "4. Помочь в приюте для бездомных животных."

d "5. Отвезти пожертвования в дом престарелых."

d_t cunning "Я был готов продолжать список далее, так как заготовил 15 пунктов, но меня прервали."

b_1 "Понял. Ты очень умный и благородный юноша."

b_1 "Я рад, что моя дочь общается с тобой. Зови её гулять почаще!"

d_t pose2 neutral "Я молча кивнул и поклонился в знак уважения."

scene bg_black with Dissolve(0.5)

show bg_near_home with Dissolve(1)
show b_1 left at Transform(xalign=0.8, yalign=1.0) with Dissolve(1)
pause 0.5
show u left open thinking at enter_scene(xalign=0.3)
with Dissolve(1)

d_t "Отец уже начал закрывать калитку, как в неё просочилась Юми. "

show u closed touched
show b_1 at move_step(200, 0.5)

d_t pose2 asharashen "Она улыбнулась, шепнула \"Спасибо!\" и {w=0.5}поцеловала меня в щеку. "

show u at step_left

show b_1 at Transform(xalign=1.0, yalign=1.0)
show b_1 at move_step(200, 0.5)

d_t neutral "Я понял, что не успел загрузить пособие по пикапу от Алекса Лесли, поэтому не знал, как отреагировать. Пришлось просто улыбнуться ей."

show b_1 at Transform(xalign=1.2, yalign=1.0)
show b_1 at move_step(500, 1.0)

d_t "Всё, что я смог, это прошептать ей в ответ:"

show u cute
hide b_1

d "Пойдём завтра в 12 гулять в парк?"

show u touched:
    ease 0.2 yoffset 30
    ease 0.2 yoffset 0
$ renpy.pause(1.0)
show u open cute right at move_on_scene(time=1.5, xalign=0.6)
$ renpy.pause(1.5)
show u greeting smile left with Dissolve(0.5)
$ renpy.pause(1.0)
show u open cute right at move_on_scene(time=3.0, xalign=2.0) with Dissolve(0.5)

d_t "Девушка покраснела, кивнула, помахала рукой на прощание и скрылась за калиткой."

hide u

d_t pose1 neutral "Пора было возвращаться домой."
stop music fadeout 1.0
scene bg_black with Dissolve(1)

$ renpy.pause(1.0)

scene bg_living_room with Dissolve(1)
play music music_main_theme_2_v3 fadein 0.5 fadeout 1.0 loop
d_t "В комнате было темно. Пахло сухариками, потом и страданиями."

show t_f ear surprised summer_norm left at Transform(xalign=0.3, yalign=1.3) with Dissolve(0.5)

d_t "Господин Тайда лежал головой на столе, глаза его не выражали никаких эмоций."

d pose2 asharashen "О нет, господин Тайда!"

d "Вы живы?!.."

d_t "Я приготовился делать непрямой массаж сердца, не обращая внимания на тихое ворчание моего создателя."

d sad "Раз, два..."

show t_f hz wtf left at move_step(100), fear

d_t "Я приготовился наклониться к нему, но господин заорал и отпихнул меня."

t_f ear confused "С ума сошел?! Со мной всё в порядке! Газировки перепил, вот живот и болит..."

d neutral "Слава святым шестерёнкам, как говорится."

d pose1 neutral "Я рад, что все ваши системы в порядке."

show t_f ear surprised 

d_t "Тайда положил руку на голову и присел."

t_f "Ух, аж в глазах потемнело..."

d happy "Я рад также тому, что мне удалось повысить ваш рейтинг, господин Тайда!"

t_f hz wtf "Что-что?.."

d neutral "Только послушайте!"

show t_f thinking neutral

d "Теперь вы популярны среди одноклассников — я уладил отношения со всеми."

show t_f asharashen

d_t "Тайда ещё сильнее взялся за голову."

d pose1 cunning "Учителя гордятся вами — вы даете только верные ответы и всегда знаете решения всех задач!"

show t_f thinking_hard

d_t "Послышалось тихое завывание господина."

d "В кружке робототехники вы теперь — главный эксперт во всех сферах. Участники клуба уважают вас."

d happy "Проект намазывателя паштета наконец завершен!"

show t_f hz cry_why at fall_like_leaf

d_t "Создатель упал на пол и начал медленно заползать под кровать."

hide t_f

d very_happy "Юми поцеловала меня в щечку после того, как её отец признал меня достойным. Завтра у нас свидание."

show t_f thinking asharashen summer_norm left at move_vertically(time=0.5, x=0.3, yalign1=10.0, yalign2=1.0)

d_t neutral "Тайда резко поднялся с пола и посмотрел в мою сторону глазами, в которых читалось безумие."

show t_f at fear

t_f hz wtf "Чивоооо блин?" 

show t_f hz cry_why at fear

t_f "Нет! Нет! Я к такому не готов. Я даже не знаю, как вести себя с девушками!"

d happy "Не переживайте, господин Тайда. Я уже скачал путеводитель по пикапу и смогу пойти вместо вас."

show t_f cry_sad at fear

t_f "Тебя раскроют! Уже раскрыли! Все будут смеяться надо мной... Уххх..."

d pose2 neutral "Уверяю вас, всё в порядке. Никто ничего не заподозрил."

d_t melancholy "Вдруг послышался мамин голос со двора."

show t_f wtf

mom "Тайда, дорогой! Подойди сюда, мне нужна твоя помощь в саду..."

d_t pose1 neutral "Необходимо было спешить на помощь! Я уже развернулся, чтобы выйти из комнаты..."

stop music fadeout 1.0
scene bg_black with Dissolve(1)
pause 1.0
"..."
pause 1.0
#темный экран
#смена гг повествования
$ set_character_taida()
scene bg_living_room 
play music music_main_theme_3_v2 fadein 0.5 fadeout 1.0 loop
show d_f at center
show d_f right pose1 neutral at move_on_scene(xalign=0.9)
with Dissolve(1)

#темный экран

t_t ear surprised summer_norm "Я рванул к роботу, чтобы остановить его."

t "А ну постой!.."

show d_f left surprised

t hz wtf "Так нельзя!"

t cry_sad "Моя жизнь..."

t "Да, ты доказал, что ты лучше меня во всем, но это всё ещё моя жизнь!.."

t "Уж какая есть и как я умею..."

d_f pose2 asharashen "Господин Тайда, что случилось? Всё в порядке?"

t cry_why "Да, я понимал, что ты будешь делать что-то за меня. То, что я не желал делать. Но теперь..."

show d_f pose1 surprised

t "Теперь мои друзья хотят дружить с умной, лучшей версией меня."

t "Учителя снова разочаруются во мне, ведь знаний в моей голове не прибавилось."

t cry_sad "Юми даже не знает, что поцеловала не меня."

t "Я не согласен на такое!"

d_f pose2 neutral "Господин Тайда, вам нужно остыть и подумать. А я пока помогу вашей маме."

show d_f right at step_right

t dissatisfied "Стоять! Никуда ты не пойдёшь!"

show d_f asharashen at fear

t_t "Я напал на него со спины."

scene bg_black with Dissolve(1)

play music music_rock fadeout 1.0 loop

call screen pokemon_battle with Dissolve(1.0)

stop music fadeout 1.0

scene bg_black with Dissolve(1)

show bg_living_room 
show d_f pose1 neutral school left
with Dissolve(1)
play music music_comedy_loop fadein 0.5 fadeout 1.0 loop
t_t hz cry_sad summer_norm "Драка закончилась, не успев начаться. Конечно, же моим поражением и безоговорочной капитуляцией. Я получил мощного пинка под зад железной ногой. "

d_f pose1 neutral "Всегда рад помочь вам в спаривании... Прошу прощения, не тот словарь. Всегда рад помочь в спарринге, мой господин."

show d_f right at move_on_scene(xalign=1.5)
pause 2.0
play sfx sfx_open_door

t_t dissatisfied "Андроид отряхнул одежду и вышел из комнаты, оставив меня в густой липкой тишине."

hide d_f

t_t "Я молча сполз на пол, оперевшись спиной о стену."

t_t thinking thinking_hard "Что же я наделал..."

t_t asharashen "Трясущимися руками я взял телефон и начал набирать сообщения. "

t_t "Пальцы не попадали по кнопкам, оставляя в тексте опечатки."

t hz cry_why "Друзья, проиошла беда. Дело в Дзндзо. Приходите срочно пожалуста."

t "Умоляю, зайдите тихо чрез калтку."

play sfx sfx_hit
t_t cry_sad "Телефон выпал из рук, а я напротив — впал в апатию."

$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black with Dissolve(1)
$ renpy.pause(1.0)
scene bg_living_room with Dissolve(1)
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")

play sfx sfx_knock
t_t thinking tired summer_norm "Спустя какое-то время я услышал стук в окно. "

t_t "На улице темнело. За стеклом были видны три силуэта."

t_t "Кацуми, Ден и Хикару."

show k pose1 worried right at trio_left
show den idle nervous summer left at trio_center
show h idle surprised summer left at trio_right
with Dissolve(1)

t_t "Я распахнул оконную раму, и ребята пролезли внутрь моей комнаты."

k confused "Тайда, что произошло? Где Дзиндзо? Ты сломал его или его украли?"

t thinking thinking_hard "Н-нет... С ним всё в порядке. Он функционирует, и даже слишком хорошо для робота."

t hz cry_sad "Он просто неосознанная живая кукла, но обошел меня во всём."

show k worried
show h explain thinking
show den sad

t_t "Друзья вопросительно склонили головы. Они ещё не поняли, что я сделал."

#нвл

"Вкратце я описал суть проблемы: я, ленивый обалдуй, решил воспользоваться трудами всего кружка робототехники в своих целях..." 

"...украл робота и заставил его притворяться собой. "

"Что у него получилось с удивительным превосходством. Но я не желал мириться с этим. "

"Ребята выслушали меня, пару раз устало вздохнули, трижды демонстративно похлопали себя по лбу, но не стали ругаться на меня."

"Ладно, один пинок от Кацуми я получил, но он был полностью заслуженный."

#конец нвл

h neutral_talk "Нам необходимо составить план твоего спасения. Мы должны деактивировать Дзиндзо."

show h idle neutral

k cunning "Но нужно действовать аккуратно. Он — наше лучшее изобретение, мы не имеем права его сломать."

den nervous "Мы должны быть скрытны. Это будет провал, если кто-то узнает, что мы сделали."

t_t ear neutral "Я кивнул, соглашаясь с их мыслями."

t "Для начала давайте посмотрим, что делает Дзиндзо прямо сейчас."

hide k
hide den
hide h
with Dissolve(1)

t_t "Всей толпой мы тихонько вылезли из окна."

$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black with Dissolve(1)
pause 1.0
show bg_backyard 
show expression "bush1" at Transform(xalign=1.0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.9, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=1.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
with Dissolve(1)
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
play sfx sfx_birds_v2 fadein 0.5 fadeout 1.0 loop


t_t ear neutral summer_norm "Моя мама очень любит что-то сажать, выращивать, ухаживать за цветами. "

t_t confused "Её стараниями в нашем саду растёт много цветущих красивых растений. "

play sfx2 sfx_bushes_v2
show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100
show k pose1 cunning right at Transform(xalign=0.95, yalign=0.65), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral left at Transform(xalign=0.8, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral left at Transform(xalign=1.05, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 1
with Dissolve(1)

t_t neutral "Мы спрятались за ближайшим к моему окну кустом, откуда открывался вид на небольшой сад."

show d_f pose2 neutral right at Transform(xalign=0.2, yalign=1.0)
show mom left at Transform(xalign=0.6, yalign=1.0)
with Dissolve(1)

t_t "Дзиндзо ковырялся в цветах вместе с мамой, о чём-то мило болтая. "

t_t "Мы сели и стали внимательно слушать."

mom "Я так рада, что ты решил мне помочь. Я думала, тебя не интересуют цветы, ты никогда не проявлял такой инициативы."

d_f pose1 happy "Ну что ты, мам, цветы очень красивые, мне нравится помогать тебе пересаживать эти прекрасные пионы."

show mom at giggle

t_t "Мама засмеялась и обняла Дзиндзо. "

t_t surprised "Я внутренне сжался от мысли, что она сейчас почувствует, какое твердое и холодное тело робота. "

t_t "Но всё прошло гладко."

mom "Ты такой холодный, правильно, что надел шарфик. Вечера становятся всё промозглее."

d_f pose2 sad  "Мам, послушай. Могу ли я нарвать небольшой букет в нашем саду?"

mom "Для чего он тебе? Если для меня, то пусть лучше они ещё немного порастут."

t_t confused "Я умолчал от друзей этот момент, но всё тайное рано или поздно всё равно становится явным."

d_f pose1 happy "Дело в том, что я подружился с девочкой с нашего класса - её зовут Юми, и завтра мы идем гулять. Я хотел порадовать её."

t_t "Мама хитро улыбнулась и сказала:"

mom "Что ж, по такому случаю, пойдём выбирать лучшие цветы!.."

play sfx sfx_bushes
show k happy at fear
show den happy at giggle
show h happy at giggle

t_t shy "На этом моменте друзья стали давиться от смеха. Ден в истерике  упал на землю и начал жевать траву, чтобы успокоиться."

play sfx sfx_bushes_v2
show h at giggle

t_t "Хикару хихикал надо мной и над Деном, приложив кулак ко рту. "

play sfx sfx_bushes
show h explain surprised at fear

play sfx sfx_bushes_v2
play sfx sfx_slap
t_t angry "Я дал ему подзатыльник и с недовольным лицом пополз обратно в сторону дома, показывая жестами следовать за мной."

show k neutral
show den neutral
show h idle neutral
hide mom
hide d_f
with Dissolve(1)

play sfx2 sfx_bushes_v2
t_t neutral "Как только мы снова оказались в густых кустах у окна моей комнаты, не боясь быть раскрытыми, мы стали обсуждать дальнейший план."

k pose2 neutral "Так, все же понимают, что на данном этапе во всём признаваться - самоубийство."

k smug "Мы должны переждать завтрашний день."

t surprised "Как?! Он пойдёт гулять с Юми и всё испортит!"

h cunning "Точно всё испортишь ты, а он ещё подает какие-то надежды."

k pose1 cunning "Если мы не хотим испортить отношения с Юми, пусть он её немного развлечет. Ничего страшного не случится."

t_t confused "Я попытался взять себя в руки. "

t surprised "Хорошо, пусть так. Он сказал, что встреча в парке в 12."

t "Предлагаю встретиться завтра около 11 в парке, чтобы не упустить их."

t_t "Ребята кивнули. "

#ползание ребят
play sfx sfx_bushes_v2
hide k
hide den
hide h
with Dissolve(1)

t_t neutral "Мы попрощались, все разошлись по домам. Точнее, расползлись аккуратно, чтобы никто не заметил их и моего присутствия у меня дома."

hide bush4 onlayer screens
$ renpy.music.set_volume(0.5, delay=0.5, channel="music")
scene bg_black 
with Dissolve(1)
scene bg_living_room with Dissolve(1)
$ renpy.music.set_volume(1.0, delay=0.5, channel="music")
t_t ear neutral summer_norm "Я влез в свою комнату обратно через окно. "

#найти букет?????

t_t "На столе стоял свежесрезанный букет садовых цветов, подготовленный к завтрашнему свиданию."

t_t surprised "С удивлением я обнаружил, что андроид залез в мою кровать и имитирует сон. "

t_t "Видимо, настолько он хорошо вжился в мою роль."

t_t confused "Сначала я хотел было выгнать его со своего спального места, но синяк на жопе давал о себе напомнить постоянной ноющей болью."

t_t "Посему я решил, что не очень-то и хотелось трогать этого бешеного робота."

t_t neutral "С трудом я свернулся калачиком на коврике у двери и провалился в сон."

stop music fadeout 1.0
scene bg_black with Dissolve(1)
$ renpy.pause(1.0)

$ unlock_achievement(ACHIEVEMENT_SECOND_CHAPTER)

jump chapter3