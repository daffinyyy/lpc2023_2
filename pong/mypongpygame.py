# Jucimar Jr
# 2022

import pygame
import random
import numpy
import math

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2022-12-12")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300
prev_ball = 0
speed = 5

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5
ball_speed = math.sqrt(ball_dx**2 + ball_dy**2)
acceleration = 1

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball_x < 100:
            if ball_x > 70 and ball_dx < 0:
                ball_speed = math.sqrt(ball_dx ** 2 + ball_dy ** 2)
                acceleration += 0.1
                ball_speed *= acceleration
                if player_1_y - 25 < ball_y < player_1_y + 5:
                    ball_dx = ball_speed * numpy.cos(numpy.pi/3)
                    ball_dy = ball_speed * numpy.sin(numpy.pi/3) * -1
                    bounce_sound_effect.play()
                elif player_1_y + 5 <= ball_y < player_1_y + 35:
                    ball_dx = ball_speed * numpy.cos(numpy.pi / 6)
                    ball_dy = ball_speed * numpy.sin(numpy.pi / 6) * -1
                    bounce_sound_effect.play()
                elif player_1_y + 35 <= ball_y < player_1_y + 65:
                    ball_dx *= -1
                    bounce_sound_effect.play()
                elif player_1_y + 65 <= ball_y < player_1_y + 95:
                    ball_dx = ball_speed * numpy.cos(numpy.pi / 6)
                    ball_dy = ball_speed * numpy.sin(numpy.pi / 6)
                    bounce_sound_effect.play()
                elif player_1_y + 95 <= ball_y < player_1_y + 135:
                    ball_dx = ball_speed * numpy.cos(numpy.pi / 3)
                    ball_dy = ball_speed * numpy.sin(numpy.pi / 3)
                    bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if 1160 < ball_x < 1190 and ball_dx > 0:
            ball_speed = math.sqrt(ball_dx ** 2 + ball_dy ** 2)
            if player_2_y - 25 < ball_y < player_2_y + 5:
                ball_dx = ball_speed * numpy.cos(numpy.pi / 3) * -1
                ball_dy = ball_speed * numpy.sin(numpy.pi / 3) * -1
                bounce_sound_effect.play()
            elif player_2_y + 5 <= ball_y < player_2_y + 35:
                ball_dx = ball_speed * numpy.cos(numpy.pi / 6) * -1
                ball_dy = ball_speed * numpy.sin(numpy.pi / 6) * -1
                bounce_sound_effect.play()
            elif player_2_y + 35 <= ball_y < player_2_y + 65:
                ball_dx *= -1
                bounce_sound_effect.play()
            elif player_2_y + 65 <= ball_y < player_2_y + 95:
                ball_dx = ball_speed * numpy.cos(numpy.pi / 6) * -1
                ball_dy = ball_speed * numpy.sin(numpy.pi / 6)
                bounce_sound_effect.play()
            elif player_2_y + 95 <= ball_y < player_2_y + 135:
                ball_dx = ball_speed * numpy.cos(numpy.pi / 3) * -1
                ball_dy = ball_speed * numpy.sin(numpy.pi / 3)
                bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            acceleration = 1
            ball_dy = 5
            ball_dx = 5
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            acceleration = 1
            ball_dy = -5
            ball_dx = -5
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= speed
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += speed
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence"
        if ball_x <= 700:
            # code of ball guess
            if (abs(player_2_y - prev_ball) < 5) or player_2_y == 0 or player_2_y == 570:
                if player_2_y == 0:
                    prev_ball = player_2_y + random.randint(100, 570)
                elif player_2_y == 570:
                    prev_ball = player_2_y + random.randint(-570, -100)
                else:
                    prev_ball = player_2_y + random.randint(100, 570) * random.choice([-1, 1])
        else:
            prev_ball = ball_y

        player_2_y += numpy.sign(prev_ball - player_2_y) * speed
        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
