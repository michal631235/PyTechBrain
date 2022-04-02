import PyTechBrain as Ptb
import random
import time

if __name__ == '__main__':
    board = Ptb.PyTechBrain()
    r = 0
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    b = 25

    while True:
        temp = board.temperatura_C()
        time.sleep(0.33)
        if temp < 20.5:
            board.sygnalizator_czerwony("on")
            board.sygnalizator_zolty("off")
            board.sygnalizator_zielony("off")
        elif temp > 20.5 and temp < 22:
            board.sygnalizator_zolty("on")
            board.sygnalizator_czerwony("off")
            board.sygnalizator_zielony("off")
        else:
            board.sygnalizator_zielony("on")
            board.sygnalizator_zolty("off")
            board.sygnalizator_czerwony("off")
        print(f"{temp}")

        # btn_lewy = board.przycisk_lewy()
        # btn_srodek = board.przycisk_srodkowy()
        # btn_prawy = board.przycisk_prawy()
        #
        # if btn_prawy == True:
        #     time.sleep(0.1)
        #     board.buzzer_sygnal("beep")
        # if btn_lewy == True:
        #     time.sleep(0.02)
        #     board.buzzer_sygnal("beep")
        # if btn_srodek == True:
        #     time.sleep(0.05)
        #     board.buzzer_sygnal("beep")
        #
        # vol = board.glosnosc_raw()
        # print(vol)


        # if vol < 200:
        #     time.sleep(0.25)
        #     board.buzzer_sygnal("beep")
        #     board.sygnalizator_czerwony("on")
        #     board.sygnalizator_zolty("off")
        #     board.sygnalizator_zielony("off")
        # elif vol > 200 and vol < 377:
        #     time.sleep(0.15)
        #     board.buzzer_sygnal("beep")
        #     board.sygnalizator_czerwony("off")
        #     board.sygnalizator_zolty("on")
        #     board.sygnalizator_zielony("off")
        # else:
        #     time.sleep(0.05)
        #     board.buzzer_sygnal("beep")
        #     board.sygnalizator_czerwony("off")
        #     board.sygnalizator_zolty("off")
        #     board.sygnalizator_zielony("on")





