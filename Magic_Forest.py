sdalsya = "Я сдаюсь"
pomosch = "Помоги"
pravila = "Напомни правила"
ugadat_slovo = "Я попробую угадать целое слово"
itogovoe_slovo = ""
schetchik_dva = 0
ispolsovannie_bukvi = set()
print("Привет, человек! Сыграй в мою игру *Диковинный лес*. Сам придумал.")     
print("Что? Просто так не хочешь играть? Ну, тогда сыграем на жвачку.")
print("Я загадаю слово, а ты должен будешь его угадывать по букве.") 
print("Или же,для тех кто любит рисковать, ты можешь попробовать угадать целое слово.")
print("НО! Если ты не угадаешь, то ты ПРОИГРАЕШЬ!!!")
zhivotnoe_mnozhestvo = set()            ###МНОЖЕСТВА С ЗАГАДАННЫМИ СЛОВАМИ
zhivotnoe_mnozhestvo = {"собака", "корова", "медведь", "попугай", "крокодил"}
techno_mnozhestvo = set()
techno_mnozhestvo = {"двигатель", "телескоп", "фотоаппарат", "интернет", "информация"}
rastenia_mnozhestbo = set()
rastenia_mnozhestbo = {"тайга", "тюльпан", "лиственница", "осина", "кустарник"}
print("Я позволю тебе решить, на какую из тем мне загадть слово.")
print("Животные. Тема для тех, кто несилён в отгадывании слов.")
print("Растения. Тема для тех, кто считает, что сумеет угадать среденее по сложности слово.")
print("Технологии. Загадаю сложное слово на эту тему. Для тех, кто уверен, что угадает абсолютно любое слово.")
print("Напиши *Животные*, *Растения* или *Технологии*. Звездочки я написал вместо кавычек. Итак: ")
tema = input()
print(tema)
if tema == "Растения":
    zagadannoe_slovo = rastenia_mnozhestbo.pop()
elif tema == "Технологии":
    zagadannoe_slovo = techno_mnozhestvo.pop()
elif tema == "Животные":
    zagadannoe_slovo = zhivotnoe_mnozhestvo.pop()
else:
    print("Такой темы я не предлагал. Я же русским языком тебе объяснял... Выберу сам, понял?!")
    zagadannoe_slovo = rastenia_mnozhestbo.pop()
print("В чем-то не разобрался? Напиши *", pomosch,"*, и я тебе подсоблю!", sep="")
print("За сколько попыток ты сможешь выиграть? Решать тебе: ")
kolvo_popitok = int(input())
print(kolvo_popitok)
potracheno_popitok = 0
print("Если ты проиграешь... Ладно, сечас не об этом. Да начнется игра!!!")
schetchik = 0
slovo = ""
slovo_atalon = "*" * len(zagadannoe_slovo)
print(slovo_atalon)                            ###ЗАШИФРОВАННОЕ СЛОВО               
print("Попробуй угадать букву: ")
bukva = input()
bukvi_zagadannogo_slova = set()
###СОЗДАНИЕ МНОЖЕСТВА С БУКВАМИ НИЖНЕГО И ВЕРХНЕГО РЕГИСТРА ЗАГАДАННОГО СЛОВА
for i in zagadannoe_slovo:                           
        bukvi_zagadannogo_slova.add(i)
        bukvi_zagadannogo_slova.add(chr(ord(i) - 32))
###ОСНОВНОЙ ЦИКЛ
a = "Бесконечный цикл"
while a == "Бесконечный цикл":
    ###ПОМОЩЬ
    if bukva == pomosch:
        print(bukva)
        print("Если тебе нужна помощь, напиши *", pomosch,"*.", sep="")
        print("Если хочешь, чтобы я напомнил тебе правила, напиши *", pravila, "*.", sep="")
        print("Если хочешь сдаться, напиши *", sdalsya,"*.", sep="")
        print("Если хочешь угадать целое слово, напиши *", ugadat_slovo,"*.", sep="")
        print("Надеюсь, еще раз повторять не придётся.")
        print("Твой выбор: ")
        bukva = input()
    ###ПРАВИЛА
    elif bukva == pravila:
        print(bukva)
        print("Диковинный лес - это игра, в которой программа загадывает слово, а пользователь пытается его угадать.") 
        print("В программе загадано слово. Пользователь вводит число попыток, за которое угадает его.") 
        print("На экран выводиться загаданное слово, но вместо букв специальные символы (звездочки). Пользователь вводит по одной букве.")
        print("Если он ввел букву, которое есть в слове, то его уведомляют и показывают место буквы в загаданном слове.") 
        print("Если же он не угадал, то ему сообщают об этом, а число попыток уменьшается на одну.") 
        print("При угадывании слова пользователя поздравляют и указывает, сколько попыток у него осталось.")
        print("Примечание:")
        print("1. Ввод не чувствителен к регистру.")
        print("2. Если пользователь вводит больше одной буквы или не букву, выводится сообщение об ошибке.")
        print("3. Если пользователь вводит букву, которую ранее использовал, выводится соответствующее сообщение.")
        print("4. Игра продолжается до тех пор, пока не будет угадано слово.")
        print("5. Если введенная буква встречается более одного раза в слове, то открываются все.")
        print("Фух, как я устал это объяснять. Буква: ")
        bukva = input()
    ###СДАТЬСЯ
    elif bukva == "Я сдаюсь":
        print(bukva)
        print("Ха - ха! Еще ни у кого не получилось угадать это слово!")
        print("Ты сдался на", potracheno_popitok, "попытке. Жалкое зрелище...")
        print("Ступай! То же мне, игрок! Ха - ха - ха!")
        break
    ###УГАДАТЬ ЦЕЛОЕ СЛОВО        
    elif bukva == ugadat_slovo:
        print(bukva)
        print("Ну, рискни:")
        celoe_slovo = input()
        for w in celoe_slovo:                           
            if w == zagadannoe_slovo[schetchik_dva]:
                itogovoe_slovo += w
                schetchik_dva += 1      
            elif chr(ord(w) + 32) == zagadannoe_slovo[schetchik_dva]:
                itogovoe_slovo += chr(ord(w) + 32)
                schetchik_dva += 1
        if itogovoe_slovo == zagadannoe_slovo:
            print(itogovoe_slovo)
            print("Попался! Это не... Стоп...")
            print("Ты угадал ЦЕЛОЕ СЛОВО?! И ВСЕГО ЛИШЬ ЗА ", potracheno_popitok, " ПОПЫТОК?", sep="")
            print("КТО ТЫ?! КАКОЙ-ТО КОЛДУН?!")
            print("Я не хочу иметь дело с колдуном! Забирай жвачку и проваливай!.. Пожалуйста. ")
        else:
            print("Это... НЕВЕРНЫЙ ОТВЕТ! Ха - ха -ха!")
            print("Ты должен мне упаковку жвачек!")
            print("Как говорится: больший риск, большой штраф! Ха - ха!")
            print("Этого нет в правилах? Послушай, это моя игра, а значит отныне это правило.")
            print("Что? Чайник не выключил дома?! Тогда потом отдашь, хорошо? Я буду ждать.")
        break
    ###ПРОВЕРКА НА РУССКУЮ БУКВУ
    elif 1039 < ord(bukva) < 1104:
        ###ВВОД БУКВЫ, КОТОРУЮ УЖЕ ПЕЧАТАЛ
        if bukva in ispolsovannie_bukvi:              
            print(bukva)
            print("Ты уже использовал эту букву. Скажи, в чем смысл ВВОДИТЬ ОДНУ И ТУ ЖЕ БУКВУ?!")
            print(slovo_atalon)
            print("Постарайся вспомнить еще какую-нибудь букву из алфавита:")
            bukva = input()
        ###ПРОВЕРКА ВВОДА 1 БУКВЫ
        elif len(bukva) > 1:                                          
            print(bukva)
            print("Ты ввел больше, чем одну букву. НАРУШЕНИЕ ПРАВИЛ!!!")
            print(slovo_atalon)
            print("Попытайся ввести ОДНУ букву. Это что, так сложно?")
            bukva = input()        
        ###УГАДАЛ
        elif bukva in bukvi_zagadannogo_slova:                      
            print(bukva)
            print("Так... Похоже, что ты угадал.")
            if 1039 < ord(bukva) < 1072:
                ###ДОБАВЛЕНИЕ К ИСПОЛЬЗОВАННЫМ БУКВАМ
                ispolsovannie_bukvi.add(bukva)
                ispolsovannie_bukvi.add(chr(ord(bukva) + 32))
                ###УДАЛЕНИЕ ИЗ МНОЖЕСТВА С БУКВАМИ ЗАГАДАННОГО СЛОВА
                bukvi_zagadannogo_slova.remove(bukva)                  
                bukvi_zagadannogo_slova.remove(chr(ord(bukva) + 32))
                for j in zagadannoe_slovo:                      
                    if chr(ord(bukva) + 32) == j:
                        slovo += chr(ord(bukva) + 32)
                        schetchik += 1
                    elif 1039 < ord(slovo_atalon[schetchik]) < 1104:
                        slovo += (slovo_atalon[schetchik])
                        schetchik += 1
                    else:
                        slovo += "*" 
                        schetchik += 1
                slovo_atalon = slovo
                slovo = ""
            else:
                ispolsovannie_bukvi.add(bukva)
                ispolsovannie_bukvi.add((chr(ord(bukva) - 32)))
                bukvi_zagadannogo_slova.remove(chr(ord(bukva) - 32))
                bukvi_zagadannogo_slova.remove(bukva)
                for g in zagadannoe_slovo:                      
                    if bukva == g:
                        slovo += bukva
                        schetchik += 1
                    elif 1039 < ord(slovo_atalon[schetchik]) < 1104:
                        slovo += (slovo_atalon[schetchik])
                        schetchik += 1
                    else:
                        slovo += "*" 
                        schetchik += 1    
                slovo_atalon = slovo
                slovo = ""
            schetchik = 0
            print(slovo_atalon)
            if slovo_atalon == zagadannoe_slovo:
                break
            print("Твоя следующая догадка: ")
            bukva = input()
        ###ТЫ НЕ УГАДАЛ
        else:
            print(bukva)                                         
            if 1039 < ord(bukva) < 1072:
                ispolsovannie_bukvi.add(bukva)
                ispolsovannie_bukvi.add(chr(ord(bukva) + 32))
            else:
                ispolsovannie_bukvi.add(bukva)
                ispolsovannie_bukvi.add((chr(ord(bukva) - 32)))
            potracheno_popitok += 1
            if kolvo_popitok == potracheno_popitok:
                break
            print("Ага, не угадал! На один шаг ближе к победе!")
            print("Ты потратил ", potracheno_popitok, " попыток из ", kolvo_popitok, ".", sep="")
            print(slovo_atalon)
            print("Предположи букву: ")
            bukva = input()                                  
    ###ЕСЛИ БУКВА НЕ РУССКАЯ
    else:
            print(bukva)
            print("Я же говорил ввести букву... А это что-то на непонятном мне языке.")
            print("Дам тебе шанс исправить свою ошибку: ")
            bukva = input()
###ЧТОБЫ НИЧЕГО НЕ ПЕЧАТОЛОСЬ ПРИ КОМАНДЕ *СДАТЬСЯ*
if bukva == sdalsya:
    print("")
###ЧТОБЫ НИЧЕГО НЕ ПЕЧАТОЛОСЬ ПРИ КОМАНДЕ *Я попробую угадать целое слово*
elif bukva == "Я попробую угадать целое слово":
    print("")
###ПОБЕДА
elif potracheno_popitok < kolvo_popitok:                                                 
    print("Что?! Ты угадал слово?! НЕ МОЖЕТ ТАКОГО БЫТЬ!!!")
    print("И ТЫ ПОТРАТИЛ ", potracheno_popitok, " ПОПЫТОК ИЗ ", kolvo_popitok, "? Ты точно жульничал!", sep="")
    print("Что? Жвачка? Какая жвачка? Ничего не знаю!")
    print("Уходи с глаз долой!")
###ПРОИГРЫШ
else:
    print("Ха - ха - ха! Я так и знал! НИКТО не сможет угадать это слово!")    
    print("Теперь ты должен мне жвачку.")
    print("Как это такого не было в правилах? Надо было слушать внимательно!!!")
    print("Эй, ты куда?!")
    print("Эх, еще один убежал...")
