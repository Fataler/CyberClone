label chapter3:
#АКТ 3
#темный экран
call screen time_passed("На следующее утро")
play music music_main_theme_3 fadein 0.5 fadeout 1.0 loop
scene bg_living_room with Dissolve(1)

#темный экран

t_t thinking tired naked "Яркий луч солнца светил в глаза. Я попытался их открыть, но они словно слиплись."
t_t thinking_hard "Пара усилий, и я поднялся на локтях и проморгался. "
t_t think "Всё тело болело. Почему?.."
t_t hz wtf "Ах да. Я всю ночь проспал на полу. Не очень удобно, надо сказать. "
t_t neutral "Медленно поднявшись, чтобы не потемнело в глазах, я осмотрелся. "
t_t "Проснулся раньше обычного? Или?.."
t_t thinking think "Бросившись к столу, я увидел время. 11:34."
t_t asharashen "Меня охватила паника. "
t_t hz cry_sad "Я опоздал."
t_t "Дзиндзо уже не было в комнате. "
t_t cry_why "Он выключил будильник и просто переступил через меня, спавшего на пороге. "
t_t dissatisfied "Это привело меня в ярость. И в осознание, что с этим точно необходимо что-то делать!"
pause 0.5
play sfx sfx_knock
t_t thinking asharashen "За окном послышался тихий, но настойчивый стук по стеклу."
t_t "Я наспех начал одеваться."
t_t "Погода жаркая, выходной день..."
t_t think "Где мои единственные шорты..."
play sfx sfx_knock

t_t asharashen "Стук повторился. К нему прибавились тихие ругательства." with vpunch
t_t "Половина вещей из шкафа была выкинута мной на пол, но желаемое найти не удалось. "
t_t thinking_hard "Чертыхаясь и обливаясь потом, я схватил первое попавшееся."
t_t hz wtf "Это были шорты, которые я носил ещё в средней школе, в максимально дурацкой расцветке."
show t_f ear asharashen summer_strem with Dissolve(1)

t_t ear asharashen "Еле-еле натянув их на себя, я взглянул в зеркало и ужаснулся."

window hide
pause 2.0
window show

t_t cry_sad "Раскрыв шторы, я увидел очень злые лица друзей."

hide t_f with Dissolve(1)
show den awesome sad left summer at trio_left
show k pose1 angry right at trio_center
show h idle angry left summer at trio_right
with Dissolve(1)

k "Бестолочь, ты опять проспал! Ну и видок у тебя. Позорище."
t hz wtf summer_strem "У тебя не лучше! Ты зачем в выходной день вырядилась в школьную форму?"
t_t "Она самоуверенно задрала нос:"
k "Школьная форма... Она идет мне больше всего! И вообще..."
k pose2 annoyed "Мы ждали тебя полчаса!"
den idle nervous "Даже я не позволяю себе так опаздывать! Поспать — это святое, но проспать свою жизнь!.."
h "Да, с тобой в разведку не сходишь. Или на рыбалку..."
k pose1 neutral "Побежали скорее, мы на великах!"

show bg_near_home with Dissolve(1)

t_t summer_strem thinking neutral "Ребята гуськом двинулись вдоль забора к выходу со двора, вскочили на велики и двинулись в сторону парка."
t_t hz cry_sad "Я тихо подвывал от обиды и от того, как старые шорты сдавливали мне мои самые лучшие достоинства."
t_t "Велосипед нес меня вдаль, а я лишь шептал:"
t cry_why "Он украл не только мою жизнь, но и мои единственные шорты..."

stop music fadeout 1.0
scene bg_black with Dissolve(1)
$ renpy.pause(1.0)
#темный экран
#Amusement Park.JPG
scene bg_amusement_park with Dissolve(1)
play music fluffing_a_duck loop
t_t ear surprised summer_strem "Мы прибыли к входу в парк развлечений. "

show k pose1 confused right at enter_scene(time=1.5, xalign=0.5)
show den idle nervous summer left at enter_scene(xalign=0.8)
show h idle surprised summer left at enter_scene(time=1.0, xalign=0.2)

t_t "Запыхавшиеся, потные и недовольные, мы вбежали внутрь территории."
t_t "Вокруг царила атмосфера непринужденного веселья, летняя и лёгкая. "
t_t thinking thinking_hard "А также присутствовала определенная толика романтики..."
t_t "...ведь что может быть лучше для пары школьников, чем совместное посещение аттракционов и мороженое в летнюю знойную жару?.."
t_t neutral "Отогнав лишние мысли, я бросился искать их. "
pause 0.5
t_t thinking thinking_hard "И нашел. "

play sfx sfx_bushes_v2
show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100
show expression "bush1" at Transform(xalign=1.0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.9, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=1.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
show k pose1 cunning right at Transform(xalign=0.95, yalign=0.65), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral left at Transform(xalign=0.8, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral left at Transform(xalign=1.05, yalign=0.95), size_change(0.6, 0.6) onlayer master zorder 1
with Dissolve(1)

t_t ear neutral "Мы мгновенно приняли скрытную стойку возле ближайшей палатки с тиром."

show d_f pose1 neutral summer left at Transform(xalign=0.4, yalign=1.0)
show u closed cry summer right at Transform(xalign=0, yalign=1.0)
with Dissolve(1)

t_t surprised "Они сидели у фонтана. Юми, вероятно, натерла ногу в своих красивых босоножках на каблуках, и была расстроена."
t_t "В момент, когда мы их заметили, Дзиндзо не терял времени даром. "

show d_f pose2 neutral

t_t thinking thinking_hard "Он вытащил из рюкзака запас пластырей, которыми я не так давно заклеивал ему палевные болты, и приклеил их ей на ногу."

show u touched

t_t "Юми засмущалась, но поблагодарила Дзиндзо, и они весело болтали, сидя на бортике фонтана и брызгая друг друга теплой водичкой."
t ear asharashen "Вот бы его короткое замыкание пробрало!.."
t angry "Я ему щас!!!.."

play sfx sfx_hit
play sfx2 sfx_bushes

t_t "Чуть было не сдвинувшись с места в попытке помешать им, я был прижат к стене. " with vpunch
stop sfx
play sfx2 sfx_bushes_v2
show den idle nervous at fear
show h explain surprised at giggle

t_t surprised "Внезапно друзья схватили меня и обездвижили. "

show k pose2 didnt_understand at fear

play sfx sfx_bushes
t_t "Кацуми шикнула, чтобы я замолчал."
t_t angry "Ден и Хикару крепко прижимали моё барахтающееся в ярости тело, пока я не обессилил и не обвис в их объятиях."
t_t thinking thinking_hard "Что ж..."
t_t hz cry_sad "Остаток дня нам оставалось лишь наблюдать, как робот гуляет с девушкой, которая мне нравится."

hide bush4 onlayer screens
scene bg_black with Dissolve(1)
#слайдшоу цг 
call park_scene from _call_park_scene

t_t ear cry summer_strem "Я потерял всякую мотивацию как-либо влиять на ситуацию."
t_t hz cry_sad "Что я мог?.."
window hide

#темный экран
hide bush4 onlayer screens
scene bg_black with Dissolve(1)
pause 1.0
play music music_main_theme_3 fadein 0.5 fadeout 1.0 loop
scene bg_amusement_park with Dissolve(1)
#Amusement Park.JPG
#play sfx sfx_bushes
show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer screens zorder 100
show expression "bush1" at Transform(xalign=1.0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.9, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=1.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
show k pose1 cunning right at Transform(xalign=0.95, yalign=0.65), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral summer left at Transform(xalign=0.8, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral left summer at Transform(xalign=1.05, yalign=0.95), size_change(0.6, 0.6) onlayer master zorder 1
show d_f pose1 relief summer left at Transform(xalign=0.4, yalign=1.0) onlayer master zorder 3
show u open cute summer right at Transform(xalign=0, yalign=1.0) onlayer master zorder 3
with Dissolve(1)

t_t ear cry summer_strem "День подходил к концу. "


show d_f pose2 neutral summer right at move_on_scene(xalign=0.6)
show u closed touched summer right at move_on_scene(time=3.0, xalign=1.0)
pause 2.0
show u left
play sfx sfx_bushes
show expression "bush1" at Transform(xalign=0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.1, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=-0.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
show k pose1 cunning left at Transform(xalign=-0.05, yalign=0.8), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral right at Transform(xalign=0.05, yalign=0.7), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral right at Transform(xalign=0.2, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
with Dissolve(1)

t_t "Мы таскались за этой сладкой парочкой около 6 часов. "


show d_f pose1 neutral summer left at move_on_scene(xalign=0.4)
show u open happy summer left at move_on_scene(time=3.0, xalign=0)
pause 2.0
show u right
play sfx sfx_bushes
show expression "bush1" at Transform(xalign=1.0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.9, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=1.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
show k pose1 cunning right at Transform(xalign=0.95, yalign=0.65), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral left at Transform(xalign=0.8, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral left at Transform(xalign=1.05, yalign=0.95), size_change(0.6, 0.6) onlayer master zorder 1
with Dissolve(1)

t_t "Попутно отбиваясь от фанаток Хикару, которые то и дело преграждали нам путь, пытаясь увести его под ручку или накормить мороженым."


show d_f pose2 neutral summer right at move_on_scene(xalign=0.6)
show u closed touched summer right at move_on_scene(time=3.0, xalign=1.0)
pause 2.0
show u left
play sfx sfx_bushes
show expression "bush1" at Transform(xalign=0, yalign=1.0), size_change(0.6, 0.6) onlayer master zorder 2
show expression "bush3" at Transform(xalign=0.1, yalign=0.7), size_change(0.35, 0.35) as bushh1 onlayer master zorder 2
show expression "bush3" at Transform(xalign=-0.2, yalign=1.0), size_change(0.5, 0.5) as bushh2 onlayer master zorder 2
show k pose1 cunning left at Transform(xalign=-0.05, yalign=0.8), size_change(0.5, 0.5) onlayer master zorder 1
show den awesome neutral right at Transform(xalign=0.05, yalign=0.7), size_change(0.5, 0.5) onlayer master zorder 1
show h idle neutral right at Transform(xalign=0.2, yalign=0.6), size_change(0.5, 0.5) onlayer master zorder 1
with Dissolve(1)

t_t hz cry_why "Что сказать, свидание удалось."

t_t cry_sad "Мне уже было наплевать. Голову посещали мрачные мысли."

show k pose1 worried
show den awesome sad
show h idle surprised

t_t "Друзья сочувствующе смотрели на меня и молчали. "

t_t "Мы сидели на корточках у забора. Из живого здесь была только изгородь, я же ощущал себя совершенно истощенным."

t_t ear cry "Дзиндзо и Юми стояли по ту сторону изгороди и не видели нас."

t_t "Расстояние, что нас разделяло, было совсем небольшим, так что мы могли подслушать их разговор."

u cute "Тайда, спасибо за сегодняшний вечер. Было классно! Мне очень понравилось."

t_t "Юми покрылась густым румянцем."

u closed touched "Ты очень милый и хороший."

u "Я рада, что ты позвал меня сегодня."

show u cute

t_t "Девушка потупила взгляд и стыдливо пинала песок носком босоножки."

u "Вчера, когда ты был у нас в гостях, ты поразил меня."

show d_f pose1 neutral

t_t "Дзиндзо лишь стоял и ласково улыбался девушке."

u "Я знаю тебя давно, но не думала, что ты такой быстрый и ловкий."

show k pose1 angry at fear

play sfx sfx_bushes
t_t "Кацуми шикнула на меня:"

k worried "Тайда, нельзя больше прятаться, это твой шанс!"

den idle nervous "Иначе случится непоправимое - они же сейчас поцелуются!"

h explain sad "Первый поцелуй не повторишь дважды..."

t ear surprised "Я понял..."

hide bush4 onlayer screens
show bush4 at Transform(xalign=-0.3, yalign=1.5), size_change(0.8, 0.8) onlayer master zorder 2
play sfx sfx_bushes_v2
t_t asharashen "Я выскочил из куста прямо перед ними." with hpunch

show u open thinking at fear
show d_f pose2 asharashen

t_t "Юми вскрикнула."

t_t "Я был уверен, что в роботическом искусственном взгляде на секунду мелькнул совсем человеческий страх. "

show d_f sad left at step_left

t_t asharashen "Дзиндзо двинулся в мою сторону и толкнул меня в попытке спрятать в кустах." with hpunch

stop music fadeout 1.0

t_t thinking genius "Но после речи Юми я снова стал полон решимости. Я верну то, что принадлежит мне!"

play music music_melancholy fadein 1.0 fadeout 1.0 loop

t ear surprised "Юми, он — не я! Он не настоящий!.."

t "Всего лишь живая кукла..."

show d_f asharashen at step_left

t_t angry "Дзиндзо сделал ещё одну попытку припрятать меня, но я оказал активное сопротивление." with hpunch

t "Я больше не намерен скрываться!"

show d_f sad

t "Я создал его, чтобы он стал лучшей версией меня."

t thinking thinking_hard "Я не идеален. Более того — много в чём я был плох."

t ear cry "Я ленивый. Безответственный."

t "Я раскаиваюсь в том, что сделал, правда."

t hz cry_why "Моя жизнь... Я люблю её и не хочу потерять."

t "Я должен был прилагать больше усилий. Теперь я понял, что я представляю из себя, и кем я на самом деле должен быть."

t thinking thinking_hard "Мои друзья, родные, моё будущее, даже школа... Всё это — то, ради чего я существую."

t_t ear surprised "Я повернулся к Юми, медленно выдохнул и сжал кулаки."

t shy "Я люблю тебя и не хочу потерять из-за своей же глупости!"

show d_f asharashen
show k pose1 confused
show den awesome surprised
show h idle surprised
show u closed cute

t_t "Все удивленно охнули. Казалось, даже Дзиндзо шире раскрыл глаза от удивления."

t_t surprised "Я чувствовал легкую дрожь в теле и облегчение, что сказал это."

t_t "Лучше сделать и пожалеть, чем всю жизнь жалеть о том, чего не сделал!"

show u touched

t_t "Юми покрылась густым румянцем."

u neutral "Т-тайда..."

t_t "Мне пришлось перебить её."

t "Я обещаю тебе, ты больше не увидишь старого меня."

t_t hz dissatisfied "Я показал рукой на Дзиндзо."

t "Ты не заметишь разницы."

t ear shy "Я буду таким же заботливым и внимательным. И больше никогда не откажу тебе, когда ты нуждаешься в помощи!" 

t "Обещаю, я стану таким же умным, и добьюсь высот в жизни!"

show u touched

t_t "Юми улыбнулась и отвела взгляд."

u "Тайда, спасибо..."

u "Дзиндзо и правда очень милый и хороший... Но ты мне нравишься таким, какой ты есть."

u neutral "В-всё хорошо..."

t_t embarrassed "От её слов дыхание в моей груди перехватило, я не мог шевельнуться."

u open thinking "Друзья, простите, мне нужно бежать!.."

show u left at move_on_scene(time=1.5, xalign=0.4)
pause 1.5
show u right closed touched at move_on_scene(time=1.0, xalign=0.8)
pause 1.0
show u left open thinking at move_on_scene(xalign=-0.7)

t_t "От неловкости ситуации Юми попыталась скрыться, но вспомнила про тележку с игрушками, развернулась, схватила её и сбежала прочь."

t_t ear confused "Я выдохнул и прикрыл глаза от облегчения."

t_t "Кажется, я успел всё исправить. Или не всё..."

t ear surprised "Дзиндзо..."

d_f pose2 neutral "Да, мой господин?"

play sfx sfx_bushes_v2
show k pose1 cunning at giggle
show den awesome happy at fear
show h idle happy at giggle

t_t "Ребята, стоящие рядом, хихикнули."

t shy "Дзиндзо, пожалуйста, называй меня по имени. Я не господин для тебя."

d_f pose1 neutral "Хорошо, Тайда."

t_t surprised "Я снова собрал всю волю в кулак и посмотрел ему в глаза, моему... Нашему творению."

t confused "Прости меня."

show d_f pose2 asharashen

t_t surprised "Дзиндзо снова вопросительно наклонил голову, что совсем не свойственно для бездушного андроида. И где насмотрелся?"

t confused "Я был малодушен по отношению к тебе. Это несправедливо."

show d_f pose2 melancholy

t "Я создал и использовал тебя для низких целей." 

t thinking thinking_hard "Да, прошло всего ничего времени, но я осознал, что поступил неправильно по отношению к тебе."

t "Я должен был сам бороться с проблемами в своей жизни, а не взваливать их на твои плечи."

show d_f pose1 neutral

t_t ear surprised "Дзиндзо легко улыбнулся и жестом остановил мою речь."

d_f "Всё в порядке. Я не обижен. Ведь я не умею обижаться."

d_f "Примерно представляю, что значит эта эмоция, но испытывать её не могу."

d_f relief "Но могу сказать, что был рад помогать тебе с делами, Тайда."

d_f neutral "Мне лишь нужна цель или задание, ты предоставил мне это, спасибо."

t_t asharashen "Я нервно сглотнул и кивнул."

stop music fadeout 2.0

d_f pose2 sad "Что теперь будет со мной, друзья? Я выполнил свою задачу и больше не нужен?"

play sfx sfx_bushes_v2
show k pose1 happy at giggle
show den at fear
show h at giggle

play music music_main_theme_3_v2 fadein 1.0 fadeout 1.0 loop

t_t "Ребята засмеялись. "

show d_f pose1 neutral

k neutral "Конечно же, нужен, как ты можешь так говорить? Теперь ты наш друг!"

den wink "Ты очень крутой, чел!"

h smile "Теперь ты в нашей компании!"

t_t confused "Инстинктивно поморщившись, я достойно принял эту ситуацию."

t_t hz smile "Он — не я, я не — он. "

k neutral_4stena "Что ж! Раз все вопросы мы решили, предлагаю всем вместе пойти и покушать тайяки!"

play sfx sfx_bushes_v2
show k happy at giggle
show den at fear
show h at giggle

$ speak_as("Все", "Дааа!!!~")


stop music fadeout 2.0
scene bg_black
with Dissolve(2.0)
pause 2.0

$ unlock_achievement(ACHIEVEMENT_THIRD_CHAPTER)

call epilogue_scene from _call_epilogue_scene

call label_credits from _call_label_credits