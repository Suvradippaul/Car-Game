import pygame
import time
import random
import sys
import os

pygame.init()
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# colour values
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
white = (255,255,255)
instruct_colour = (0, 0, 102)
instruct_colour2 = (0, 0, 153)
asset_bg_sound = resource_path('Assets/Audios/Back in Black.mp3')
background_sound = pygame.mixer.music.load(asset_bg_sound)
pygame.mixer.music.play(-1)
height = 600
width = 800
screen = pygame.display.set_mode((width, height))

# load the image
asset_carimg = resource_path('Assets/Images/car7.jpg')
carimg = pygame.image.load(asset_carimg).convert_alpha()
car_width = 56
asset_intro_image = resource_path('Assets/Images/background.jpg')
intro_image = pygame.image.load(asset_intro_image).convert()

# strip = pygame.image.load("yellowstrip.png")


if __name__ == '__main__':




    def intro_loop():


        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = false
                    pygame.quit()
                    sys.quit()

            screen.blit(intro_image, (0, 0))

            asset_font = resource_path('Assets/Fonts/SnesItalic-vmAPZ.ttf')
            font = pygame.font.Font(asset_font, 150)
            title = font.render("CAR GAME", True, (0, 0, 0))
            screen.blit(title, (198, 50))

            mouse = pygame.mouse.get_pos()
            if mouse[0] > 80 and mouse[0] < 230 and mouse[1] > 500 and mouse[1] < 550:
                pygame.draw.rect(screen, (0, 255, 0), (80, 500, 150, 50))
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    countdown()

            else:
                pygame.draw.rect(screen, green, (80, 500, 150, 50))
            if mouse[0] > 550 and mouse[0] < 700 and mouse[1] > 500 and mouse[1] < 550:
                pygame.draw.rect(screen, (255, 0, 0), (550, 500, 150, 50))
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    pygame.quit()
                    quit()

            else:
                pygame.draw.rect(screen, red, (550, 500, 150, 50))
            asset_font1 = resource_path('Assets/Fonts/JustMyType-KePl.ttf')
            font1 = pygame.font.Font(asset_font1, 30)
            title = font1.render("PLAY GAME", True, (255, 255, 255))
            screen.blit(title, (100, 511))
            font2 = pygame.font.Font(asset_font1, 33)
            title = font2.render("QUIT", True, (255, 255, 255))
            screen.blit(title, (599, 508))
            pygame.display.update()


    # load all the images
    asset_backgr = resource_path('Assets/Images/background_new.png')
    backgr = pygame.image.load(asset_backgr)

    asset_strip = resource_path('Assets/Images/yellowstrip.png')
    strip1 = pygame.image.load(asset_strip).convert_alpha()
    strip2 = pygame.image.load(asset_strip).convert_alpha()
    strip3 = pygame.image.load(asset_strip).convert_alpha()
    strip4 = pygame.image.load(asset_strip).convert_alpha()
    strip5 = pygame.image.load(asset_strip).convert_alpha()
    strip1_y = -150
    strip2_y = 0
    strip3_y = 150
    strip4_y = 300
    strip5_y = 450
    strip_x = 400
    strip_y_change = 7
    grass1_y = 0
    grass2_y = 0
    grass1_x = 0
    grass2_x = 650
    grass_y_change = 10

    asset_grass = resource_path('Assets/Images/side_grass150.jpg')
    grass1 = pygame.image.load(asset_grass).convert_alpha()
    grass2 = pygame.image.load(asset_grass).convert_alpha()


    def strip():
        screen.blit(strip1, (strip_x,strip1_y))
        screen.blit(strip2, (strip_x,strip2_y))
        screen.blit(strip3, (strip_x,strip3_y))
        screen.blit(strip4, (strip_x,strip4_y))
        screen.blit(strip5, (strip_x,strip5_y))

    def grass():
        screen.blit(grass1, (grass1_x, grass1_y))
        screen.blit(grass2, (grass2_x, grass2_y))



    # crashed message
    myfont = pygame.font.SysFont("None", 120)
    render_text = myfont.render("CAR CRASHED", 1, (255,0,0))



    # time module
    clock = pygame.time.Clock()

    # setting the caption
    pygame.display.set_caption("CAR RACE")


    # function for adding background image
    def background():
        screen.blit(backgr, (0, 0))


    # image appearing:
    def car(x, y):
        screen.blit(carimg, (x, y))


    # obstacle func
    def obstacle(obs_x, obs_y, obs):

        asset_obs1 = resource_path('Assets/Images/car1-01.jpeg')
        asset_obs2 = resource_path('Assets/Images/car2-01.jpeg')
        asset_obs3 = resource_path('Assets/Images/car4-01.jpeg')
        asset_obs4 = resource_path('Assets/Images/car5-01.jpeg')
        asset_obs5 = resource_path('Assets/Images/car6-01.jpeg')
        asset_obs6 = resource_path('Assets/Images/car7.jpg')
        
        if obs == 0:
            obs_pic = pygame.image.load(asset_obs1).convert_alpha()
        elif obs == 1:
            obs_pic = pygame.image.load(asset_obs2).convert_alpha()
        elif obs == 2:
            obs_pic = pygame.image.load(asset_obs3).convert_alpha()
        elif obs == 3:
            obs_pic = pygame.image.load(asset_obs4).convert_alpha()
        elif obs == 4:
            obs_pic = pygame.image.load(asset_obs5).convert_alpha()
        elif obs == 5:
            obs_pic = pygame.image.load(asset_obs6).convert_alpha()
        screen.blit(obs_pic, (round(obs_x), round(obs_y)))



    def score_card(car_passed, score):
        asset_font = resource_path('Assets/Fonts/JustMyType-KePl.ttf')
        font = pygame.font.Font(asset_font, 35)
        passed = font.render("Passed  " + str(car_passed), True, (255, 255, 255))
        score = font.render("Score  " + str(score), True, (255, 255, 255))
        screen.blit(passed, (0, 50))
        screen.blit(score, (0, 100))

    def countdown():
        countdown = True
        asset_font = resource_path('Assets/Fonts/Squirk-RMvV.ttf')
        while countdown:
            clock.tick(1)
            screen.blit(backgr, (0,0))
            font = pygame.font.Font(asset_font, 100)
            text = font.render("3", True, white)
            text_rect = text.get_rect(center=(int(width / 2), int(height / 2)))
            screen.blit(text, text_rect)
            pygame.display.update()

            clock.tick(1)
            screen.blit(backgr, (0, 0))
            font = pygame.font.Font(asset_font, 150)
            text = font.render("2", True, white)
            text_rect = text.get_rect(center=(int(width / 2), int(height / 2)))
            screen.blit(text, text_rect)
            pygame.display.update()

            clock.tick(1)
            screen.blit(backgr, (0, 0))
            asset_font = resource_path('Assets/Fonts/Squirk-RMvV.ttf')
            font = pygame.font.Font(asset_font, 200)
            text = font.render("1", True, white)
            text_rect = text.get_rect(center=(int(width / 2), int(height / 2)))
            screen.blit(text, text_rect)
            pygame.display.update()

            clock.tick(1)
            screen.blit(backgr, (0, 0))
            font = pygame.font.Font(asset_font, 250)
            text = font.render("GO", True, white)
            text_rect = text.get_rect(center=(int(width / 2), int(height / 2)))
            screen.blit(text, text_rect)



            pygame.display.update()
            clock.tick(1)
            gameloop()





    def gameloop():

        # close button
        bumped = False
        x_change = 0
        x = 400
        y = 470
        # strip_speed = 15
        # strip_y = 0
        obstacle_speed = 13
        obs = 0
        # y_change = 0
        enemy_width = 56
        enemy_height = 125
        obs_x = random.randrange(150, 650 - enemy_width)
        obs_y = -750
        car_passed = 0
        score = 0
        level = 1
        global strip1_y
        global strip2_y
        global strip3_y
        global strip4_y
        global strip5_y
        strip_width = 75
        global grass1_y
        global grass2_y

        while not bumped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    bumped = True
                    sys.exit()

                # moving in x-y cordinates
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -4
                    if event.key == pygame.K_RIGHT:
                        x_change = 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change

            background()
            strip()
            grass()




            obs_y -= (obstacle_speed / 4)
            obstacle(obs_x, obs_y, obs)
            obs_y += obstacle_speed

            # calling the car function
            car(x, y)

            score_card(car_passed, score)  # calling the score function

            if x > 650 - car_width or x < 150:
                screen.blit(render_text, (80, 250))
                pygame.display.update()
                time.sleep(2)
                gameloop()

            if obs_y > height:
                obs_y = 0 - enemy_height
                obs_x = random.randrange(150, 650 - enemy_width)
                obs = random.randint(0, 5)
                car_passed += 1
                score = car_passed * 10
                if int(car_passed) % 11 == 0:
                    level += 1
                    obstacle_speed += 1
                    myfont1 = pygame.font.SysFont(None, 100)
                    leveltext = myfont1.render("Level: " + str(level), 1, (0, 0, 0))
                    screen.blit(leveltext, (280, 200))
                    pygame.display.update()
                    time.sleep(1)

            if y < obs_y + enemy_height:
                if x > obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x + car_width < obs_x + enemy_width:
                    screen.blit(render_text, (80, 250))
                    pygame.display.update()
                    time.sleep(2)
                    gameloop()
            strip1_y += strip_y_change
            strip2_y += strip_y_change
            strip3_y += strip_y_change
            strip4_y += strip_y_change
            strip5_y += strip_y_change

            grass1_y += grass_y_change
            grass2_y += grass_y_change

            if strip1_y + strip_width >800:
                strip1_y = -(800-strip1_y)
            if strip2_y + strip_width >800:
                strip2_y = -(800-strip2_y)
            if strip3_y + strip_width>800:
                strip3_y = -(800-strip3_y)
            if strip4_y + strip_width>800:
                strip4_y = -(800-strip4_y)
            if strip5_y + strip_width>800:
                strip5_y = -(800-strip5_y)

            if grass1_y + 1400 > 800:
                grass1_y = -(800-strip1_y)
            if grass2_y + 1400 > 800:
                grass2_y = -(800-strip2_y)


            pygame.display.update()
            clock.tick(200)


    intro_loop()
    gameloop()
    pygame.quit()
    sys.quit()

