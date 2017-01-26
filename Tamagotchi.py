from pygame import * #Без этого не работает звук
import pygame,time,datetime,random,sys# Подключение библиотек
pygame.init()# Инициализация фреймворка
pygame.mixer.init()# Инициализация звука
red = [240, 74, 74]#Создание переменных цвета
orange = [240, 157, 74]
yellow = [240, 240, 74]
green = [116, 240, 74]
blue = [74, 240, 198]
indigo = [74, 116, 240]
violet = [157, 74, 240]
white = [255,255,255]
black = [0,0,0]
gray = [33, 39, 33]
goldgray = [144, 140, 116]
whitegray = [237, 237, 237]
xviev = 800
yviev = 500
size = [xviev, yviev]# Задание размеров окна
screen = pygame.display.set_mode(size)# Создание окна заданного размера
pygame.display.set_caption("Tamagotchi")# Заголовок окна
done = False# Переменная закрытия окна
clock = pygame.time.Clock()# Функция закрытие окна
pilt = pygame.image.load("bask.png")
screen.blit(pilt, (0, 0))
LiveTime = time.time()#Live
HangTime = time.time()#Hanger
MoodTime = time.time()#Mood
t4 = time.time()#Years
t5 = time.time()#Animation
dep = False
ill = False
dep1 = dep
ill1 = ill
startanimation = False
botom = 0
kastyl2 = True
kastyl3 = False
kastylLive = True
LiveMassage1 = False
LiveMassage2 = False
HangMassage1 = False
HangMassage2 = False
MoodMassage1 = False
MoodMassage2 = False
stool = False
puk = False
#------------------------Загрузка всех спрайтов---------------------------------
egg = pygame.image.load("egg.png")#яйцо
egg1 = pygame.image.load("egg1.png")
egg2 = pygame.image.load("egg2.png")
egg3 = pygame.image.load("egg3.png")
egg4 = pygame.image.load("egg4.png")
egg5 = pygame.image.load("egg5.png")
egg6 = pygame.image.load("egg6.png")
egg7 = pygame.image.load("egg7.png")
egg8 = pygame.image.load("egg8.png")
apple = pygame.image.load("apple.png")#яблоко
med = pygame.image.load("med.png")#аптечка
play = pygame.image.load("play.png")#джостик
chickL = pygame.image.load("chickL.png")#Цыплёнок лево
chickR = pygame.image.load("chickR.png")#Цыплёнок право
sprite = pygame.image.load('gray.png').convert_alpha()#Рамка
baskgr = pygame.image.load("bask.png")#Задний фон
gameover = pygame.image.load("go.png")#Конец игры

#------------------------Звуки музыка-----------------------------------------
musicGameOver = False
musicGame = True
castil = False
#-------------------------------------------------------------------------------
def EnterName():#Функция ввода имени
    pygame.draw.rect(screen, gray,[0,0,800,500],0)
    font = pygame.font.Font(None,25)
    text0 = font.render('Enter Name Your animal:',True,white)
    screen.blit(text0,[300,120])
    pygame.display.flip()
    Name = input('Введите имя питомца: ')
    while len(Name)>13:
        Name = input('Введите имя питомца: ')
    return Name
#*******************************************************************************
def LiveTimeFanc(LiveTime,clik):#Live
    if clik == 3 or clik == 4:
        t = int(time.time())
        timer = int(time.time() - t)
    else:
        t = LiveTime
        timer = int(time.time() - t)
    return timer,t
#*******************************************************************************
def HangTimeFanc(HangTime,clik):#Hanger
    if clik == 1 or clik == 4:
        t = int(time.time())
        timer = int(time.time() - t)
    else:
        t = HangTime
        timer = int(time.time() - t)
    return timer,t
#*******************************************************************************
def MoodTimeFanc(MoodTime,clik):#Mood
    if clik == 2 or clik == 4:
        t = int(time.time())
        timer = int(time.time() - t)
    else:
        t = MoodTime
        timer = int(time.time() - t)
    return timer,t
#*******************************************************************************
def timer4(t4,clik):#Years
    if clik == 4:
        t = int(time.time())
        timer = (int(time.time() - t))
    else:
        t = t4
        timer = (int(time.time() - t))
    return timer,t
#*******************************************************************************
def timer5(t5,startanimation):#Animation
    if startanimation == True:
        t = t5
        timer = time.time() - t
    else:
        t = time.time()
        timer = time.time() - t
    return timer,t
#*******************************************************************************
def DravMessege(LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,kastyl3):
    if LiveMassage1 == True:
        Mne_Ploho = pygame.image.load("Mne_Ploho.png")
        screen.blit(Mne_Ploho, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    elif LiveMassage2 == True: 
        Ya_Bolen = pygame.image.load("Ya_Bolen.png")
        screen.blit(Ya_Bolen, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    elif HangMassage1 == True:  
        Mne_Grustno = pygame.image.load("Mne_Grustno.png")
        screen.blit(Mne_Grustno, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    elif HangMassage2 == True:
        U_Menya_Dypressiya = pygame.image.load("U_Menya_Dypressiya.png")
        screen.blit(U_Menya_Dypressiya, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    elif MoodMassage1 == True:
        Hosu_Yest = pygame.image.load("Hosu_Yest.png")
        screen.blit(Hosu_Yest, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    elif MoodMassage2 == True:
        Ya_Goloden = pygame.image.load("Ya_Goloden.png")
        screen.blit(Ya_Goloden, (0, 0))
        if kastyl3 == False:
            sound = pygame.mixer.Sound('Zvuk.ogg')
            sound_channel = sound.play(loops = 0)
            kastyl3 = True
    else:
        kastyl3 = False
    return LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,kastyl3
#*******************************************************************************
def LiveDraw(LiveTime,mood,hunder,clik,ill,LiveMassage1,LiveMassage2):# Отрисовываем жизни
    clock,t = LiveTimeFanc(LiveTime,clik)
    font = pygame.font.Font(None,25)
    text0 = font.render('Live: ',True,white)
    screen.blit(text0,[650,140])
    if mood == True and hunder == True and ill == False:
        t = time.time()
        x = 15
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if mood == False and hunder == True and ill == False:
        z = clock // 20
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 6:
            LiveMassage1 = True
        if x1 != 6:
            LiveMassage1 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if hunder == True and mood == False and ill == False:
        z = (clock/1.5) // 10
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 4:
            LiveMassage1 = True
        if x1 != 4:
            LiveMassage1 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if mood == False and hunder == False and ill == False:
        z = (clock/2) // 5
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 2:
            LiveMassage1 = True
        if x1 != 2:
            LiveMassage1 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
#///////////////////////////////////////////////////////////////////
    if mood == True and hunder == True and ill == True:
        z = clock // 20
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 14:
            LiveMassage2 = True
        if x1 != 14:
            LiveMassage2 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if mood == False and hunder == True and ill == True:
        z = (clock/1.9) // 10
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 12:
            LiveMassage2 = True
        if x1 != 12:
            LiveMassage2 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if hunder == True and mood == False and ill == True:
        z = (clock/2) // 5
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 10:
            LiveMassage2 = True
        if x1 != 10:
            LiveMassage2 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
    if mood == False and hunder == False and ill == True:
        z = (clock/3) // 3
        x = 15 - z
        y = 0
        x1 = x
        while x > 0:
            pygame.draw.rect(screen, red,[570+y,160, 10,10],0)
            y += 15
            x -= 1
        if x1 == 8:
            LiveMassage2 = True
        if x1 != 8:
            LiveMassage2 = False
        if x1 > 0:
            return True,t,LiveMassage1,LiveMassage2
        else:
            return False,t,LiveMassage1,LiveMassage2
#*******************************************************************************
def MoodDraw(MoodTime,clik,dep,MoodMassage1,MoodMassage2):# Отрисовка настроение
    dat,t = MoodTimeFanc(MoodTime,clik)
    font = pygame.font.Font(None,25)
    text0 = font.render('Mood: ',True,white)
    screen.blit(text0,[650,180])
    if dat <= 60:
        x = 15
        y = 0
        while x > 0:
            pygame.draw.rect(screen, blue,[570+y,200, 10,10],0)
            y += 15
            x -= 1
        return True,t,MoodMassage1,MoodMassage1
    if dat > 60 and dep == False:
        dat = dat - 60
        z = dat // 10
        x = 15 - z
        x1 = x
        y = 0
        while x > 0:
            pygame.draw.rect(screen, blue,[570+y,200, 10,10],0)
            y += 15
            x -= 1
        if x1 == 7:
            MoodMassage1 = True
        if x1 != 17:
            MoodMassage1 = False
        if x1 > 0:
            return True,t,MoodMassage1,MoodMassage1
        else:
            return False,t,MoodMassage1,MoodMassage1
#/////////////////////////////////////////////////////
    if dat > 60 and dep == True:
        dat = dat - 60
        z = (dat) // 5
        x = 15 - z
        x1 = x
        y = 0
        while x > 0:
            pygame.draw.rect(screen, blue,[570+y,200, 10,10],0)
            y += 15
            x -= 1
        if x1 == 11:
            MoodMassage2 = True
        if x1 != 11:
            MoodMassage2 = False
        if x1 > 0:
            return True,t,MoodMassage1,MoodMassage1
        else:
            return False,t,MoodMassage1,MoodMassage1
#*******************************************************************************
def HungerDraw(HangTime,clik,HangMassage1,HangMassage2):# Отрисовка Голода
    dat,t = HangTimeFanc(HangTime,clik)
    font = pygame.font.Font(None,25)
    text0 = font.render('Hunger: ',True,white)
    screen.blit(text0,[650,220])
    if dat <= 60:
        x = 15
        y = 0
        while x > 0:
            pygame.draw.rect(screen, green,[570+y,240, 10,10],0)
            y += 15
            x -= 1
        return True,t,HangMassage1,HangMassage2
    else:
        dat = dat - 60
        z = dat // 15
        x = 15 - z
        x1 = x
        y = 0
        while x > 0:
            pygame.draw.rect(screen, green,[570+y,240, 10,10],0)
            y += 15
            x -= 1
        if x1 == 9:
            HangMassage1 = True
        if x1 != 9:
            HangMassage1 = False
        if x1 == 5:
            HangMassage2 = True
        if x1 != 5:
            HangMassage2 = False
        if x1 > 0:
            return True,t,HangMassage1,HangMassage2
        else:
            return False,t,HangMassage1,HangMassage2
#*******************************************************************************
def Disease(t4,dep,ill,clik,stool):# Отрисовка болезней
    dat,t = timer4(t4,clik)
    dat = dat - 60
    pygame.draw.rect(screen, white,[570,270, 220,90],1)
    font = pygame.font.Font(None,25)
    text1 = font.render('Disease: ',True,white)
    screen.blit(text1,[650,280])
    font2 = pygame.font.Font(None,35)
    if dat > 0:
        if stool == True:
            x = random.randint(1,1000)
            y = random.randint(1,1000)
            if x == 330 and ill == False:
                sound = pygame.mixer.Sound('ill.ogg')
                sound_channel = sound.play(loops = 0)
                ill = True
            if ill == True:
                pilt = pygame.image.load("ill.png")
                screen.blit(pilt, (595, 300))
            if y == 660 and dep == False:
                sound = pygame.mixer.Sound('ill.ogg')
                sound_channel = sound.play(loops = 0)
                dep = True
            if dep == True:
                pilt1 = pygame.image.load("depr.png")
                screen.blit(pilt1, (715, 300))
        else:
            x = random.randint(1,10000)
            y = random.randint(1,10000)
            if x == 3300 and ill == False:
                sound = pygame.mixer.Sound('ill.ogg')
                sound_channel = sound.play(loops = 0)
                ill = True
            if ill == True:
                pilt = pygame.image.load("ill.png")
                screen.blit(pilt, (595, 300))
            if y == 6600 and dep == False:
                sound = pygame.mixer.Sound('ill.ogg')
                sound_channel = sound.play(loops = 0)
                dep = True
            if dep == True:
                pilt1 = pygame.image.load("depr.png")
                screen.blit(pilt1, (715, 300))
    return dep,ill,t
#*******************************************************************************
def Control():#Функция вывода Группы имени и учеб.зав.
    pygame.draw.rect(screen, white,[30,370, 760,120],1)
    font = pygame.font.Font(None,35)
    text1 = font.render('Feed',True,green)
    pygame.draw.rect(screen, whitegray,[52,382, 111,36],0)
    screen.blit(text1,[80,390])
    font1 = pygame.font.Font(None,35)
    text2 = font1.render('Play',True,blue)
    pygame.draw.rect(screen, whitegray,[177,382, 111,36],0)
    screen.blit(text2,[200,390])
    font2 = pygame.font.Font(None,35)
    text3 = font2.render('Treat',True,red)
    pygame.draw.rect(screen, whitegray,[302,382, 111,36],0)
    screen.blit(text3,[320,390])
    font3 = pygame.font.Font(None,35)
    text4 = font3.render('Reset',True,indigo)
    pygame.draw.rect(screen, whitegray,[427,382, 111,36],0)
    screen.blit(text4,[450,390])
    pygame.draw.rect(screen, white,[50,380, 115,40],1)
    pygame.draw.rect(screen, white,[175,380, 115,40],1)
    pygame.draw.rect(screen, white,[300,380, 115,40],1)
    pygame.draw.rect(screen, white,[425,380, 115,40],1)
    pygame.draw.line(screen, white,[570,370],[570,488],1)
    pilt = pygame.image.load("ico.png")
    screen.blit(pilt, (80, 430))
    font4 = pygame.font.Font(None,25)
    text5 = font4.render('Ida-Virumaa',True,white)
    screen.blit(text5,[580,380])
    text6 = font4.render('Kutsehariduskeskus',True,white)
    screen.blit(text6,[580,400])
    text7 = font4.render('KTVR - 16',True,white)
    screen.blit(text7,[580,420])
    text8 = font4.render('Lomovskoy Kirill',True,white)
    screen.blit(text8,[580,440])
#*******************************************************************************
def MenuDrawing(LiveTime,HangTime,MoodTime,t4,Name,clik,dep,ill,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,stool):#Функция вывода меню
    font = pygame.font.Font(None,25)
    text0 = font.render('Name Your animal:',True,white)
    screen.blit(text0,[580,33])
    text1 = font.render(Name,True,white)
    screen.blit(text1,[580,55])
    pygame.draw.rect(screen, white,[570,27, 220,50],1)
    pygame.draw.rect(screen, white,[570,85, 220,50],1)
    text2 = font.render('Age of pet:',True,white)
    screen.blit(text2,[580,90])
    dat,t44 = timer4(t4,clik)
    datmin = dat//60
    if datmin < 100:
        dat1 = str(datmin)+' year'
        text3 = font.render(dat1,True,white)
    else:
        dat0 = datmin // 100
        dat1 = str(dat0)+' year died'
        text3 = font.render(dat1,True,white)
    screen.blit(text3,[650,110])
    mood,MoodTime,MoodMassage1,MoodMassage2 = MoodDraw(MoodTime,clik,dep,MoodMassage1,MoodMassage1)# Отрисовка настроение
    hunder,HangTime,HangMassage1,HangMassage2 = HungerDraw(HangTime,clik,HangMassage1,HangMassage2)# Отрисовка Голода
    live,LiveTime,LiveMassage1,LiveMassage2 = LiveDraw(LiveTime,mood,hunder,clik,ill,LiveMassage1,LiveMassage2)# Отрисовываем жизни
    dep1,ill1,t4 = Disease(t4,dep,ill,clik,stool)# Отрисовка болезней
    Control()#Функция вывода Группы имени и учеб.зав.
    return LiveTime,HangTime,MoodTime,t4,dat,live,dep1,ill1,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2
#*******************************************************************************
def ChickDrawing(LiveTime,HangTime,MoodTime,t4,chickL,chickR,sprite,baskgr,done,Name,clik,dep,ill,musicGameOver,castil,kastyl2,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,stool):#Функция рисования цыплёна
        pilt = pygame.image.load("bask.png")
        screen.blit(pilt, (0, 0))
        screen.blit(baskgr,(0,0))
        screen.blit(sprite,(0,0))
        LiveTime,HangTime,MoodTime,t44,dat,live,dep1,ill1,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2 = MenuDrawing(LiveTime,HangTime,MoodTime,t4,Name,clik,dep,ill,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage1,stool)
        if dat < 60:
            if dat < 53:
                screen.blit(egg,(10,20))
            if dat == 53:
                screen.blit(egg1,(10,20))
                if kastyl2 == True:
                    sound = pygame.mixer.Sound('EggCrack1.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = False
            if dat == 54:
                screen.blit(egg2,(10,20))
                if kastyl2 == False:
                    sound = pygame.mixer.Sound('EggCrack2.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = True
            if dat == 55:
                screen.blit(egg3,(10,20))
                if kastyl2 == True:
                    sound = pygame.mixer.Sound('EggCrack2.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = False
            if dat == 56:
                screen.blit(egg4,(10,20))
                if kastyl2 == False:
                    sound = pygame.mixer.Sound('EggCrack2.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = True
            if dat == 57:
                screen.blit(egg5,(10,20))
                if kastyl2 == True:
                    sound = pygame.mixer.Sound('EggCrack2.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = False
            if dat == 58:
                screen.blit(egg6,(10,20))
                if kastyl2 == False:
                    sound = pygame.mixer.Sound('EggCrack2.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = True
            if dat == 59:
                screen.blit(egg7,(10,20))
                if kastyl2 == True:
                    sound = pygame.mixer.Sound('EggCrack3.ogg')
                    sound_channel = sound.play(loops = 0)
                    kastyl2 = False
            if dat == 60:
                screen.blit(egg8,(10,20))
                kastyl2 = True
        elif dat//60 > 99 or live == False:
            screen.blit(gameover,(10,20))
            if castil == False:
                musicGameOver = True
                castil = True
        else:
            if(int(time.clock()) // 5) % 2 == 0:
                screen.blit(chickL,(0,20))
            else:
                screen.blit(chickR,(0,20))
        return LiveTime,HangTime,MoodTime,t44,done,dep1,ill1,dat,musicGameOver,castil,kastyl2,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,live
#*******************************************************************************
def ControlClik(dep,ill, musicGame):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            xy = event.pos
    else:
        xy = (0,0)
    x = xy[0]
    y = xy[1]
    if x > 50 and y > 380 and x < 165 and y < 420:
        chec = 1
        sound = pygame.mixer.Sound('clisk.ogg')
        sound_channel = sound.play(loops = 0)
    elif x > 175 and y > 380 and x < 290 and y < 420:
        chec = 2
        dep = False
        sound = pygame.mixer.Sound('clisk.ogg')
        sound_channel = sound.play(loops = 0)
    elif x > 300 and y > 380 and x < 415 and y < 420:
        chec = 3
        ill = False
        sound = pygame.mixer.Sound('clisk.ogg')
        sound_channel = sound.play(loops = 0)
    elif x > 425 and y > 380 and x < 540 and y < 420:
        chec = 4
        musicGame = True
        castil = True
        sound = pygame.mixer.Sound('clisk.ogg')
        sound_channel = sound.play(loops = 0)
    else:
        chec = 0
    return chec,dep,ill,musicGame
#*******************************************************************************
def music(musicGame,musicGameOver,castil):
    if musicGame == True:
        pygame.mixer.quit()
        pygame.mixer.init()
        music = pygame.mixer.Sound('background_music.ogg')
        music_channel = music.play(loops = -1)
        music_channel.set_volume(0.2)
        musicGame = False
        musicGameOver = False
    if musicGameOver == True and castil == True:
        pygame.mixer.quit()
        pygame.mixer.init()
        music = pygame.mixer.Sound('Game_Over.ogg')
        music_channel = music.play(loops = -1)
        music_channel.set_volume(0.3)
        musicGame = False
        musicGameOver = False
    return musicGame,musicGameOver,castil
#*******************************************************************************
def Animation(clik, startanimation, t5, botom, dat):
    if dat > 60:
        if startanimation == False:
            timer,t5 = timer5(t5,startanimation)
            if clik == 1:
                startanimation = True
                botom = 1
            if clik == 2:
                startanimation = True
                botom = 2
            if clik == 3:
                startanimation = True
                botom = 3
        if startanimation == True:
            if botom == 1:
                timer,t5 = timer5(t5,startanimation)
                screen.blit(apple,(200,int(timer*40)))
                if int(timer) == 3:
                    sound = pygame.mixer.Sound('priz.ogg')
                    sound_channel = sound.play(loops = 0)
            if botom == 2:
                timer,t5 = timer5(t5,startanimation)
                screen.blit(play,(200,int(timer*40)))
                if int(timer) == 3:
                    sound = pygame.mixer.Sound('priz.ogg')
                    sound_channel = sound.play(loops = 0)
            if botom == 3:
                timer,t5 = timer5(t5,startanimation)
                screen.blit(med,(200,int(timer*40)))
                if int(timer) == 3:
                    sound = pygame.mixer.Sound('priz.ogg')
                    sound_channel = sound.play(loops = 0)
            if timer >= 3:
                startanimation = False
    return startanimation,t5,botom
#*******************************************************************************!!!!!!!
def Stool(stool,t4,clik,puk,live):
    t,time = timer4(t4,clik)
    t = t // 60
    if t >= 1 and t <= 99 and live == True:
        rand = random.randint(1,5000)
        if rand == 3000 and stool == False:
            stool = True
        if stool == True:
            image = pygame.image.load("stool.png")
            screen.blit(image,(450,250))
            if puk == False:
                sound = pygame.mixer.Sound('puk.ogg')
                sound_channel = sound.play(loops = 0)
                puk = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                xy = event.pos
        else:
            xy = (0,0)
        x = xy[0]
        y = xy[1]
        if x > 452 and y > 252 and x < 560 and y < 360:
            stool = False
            sound = pygame.mixer.Sound('metla.ogg')
            sound_channel = sound.play(loops = 0)
            puk = False
    return stool,puk
#-------------------------------------------------------------------------------
Name = EnterName()
while done == False:# Основной цикл тела программы, пока кно не закрыто
    clock.tick(60)# FPS
    for event in pygame.event.get():# Проход по событиям
        if event.type == pygame.QUIT:# Если есть команда закрытия окна
            done = True# Команда закрытия окна
    clik,dep,ill, musicGame = ControlClik(dep, ill, musicGame)
    LiveTime,HangTime,MoodTime,t4,done,dep,ill,dat,musicGameOver,castil,kastyl2,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,live = ChickDrawing(LiveTime,HangTime,MoodTime,t4,chickL,chickR,sprite,baskgr,done,Name,clik,dep,ill,musicGameOver,castil,kastyl2,LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,stool)
    startanimation,t5,botom = Animation(clik, startanimation, t5, botom,dat)
    musicGame,musicGameOver,castil = music(musicGame,musicGameOver,castil)
    LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,kastyl3 = DravMessege(LiveMassage1,LiveMassage2,HangMassage1,HangMassage2,MoodMassage1,MoodMassage2,kastyl3)
    stool,puk = Stool(stool,t4,clik,puk,live)
    pygame.display.flip()# Обновить экран
pygame.quit()# Закрыть программу
#===============================================================================

