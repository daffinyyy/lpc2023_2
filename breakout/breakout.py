import pygame
from status import *
from rectangle import *
from constants import *

pygame.init()

bricks = []

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2023-11-30")

FONT = pygame.font.Font('assets/PressStart2P.ttf', 44)

# player 1
player_1 = Player("assets/player.png", "h", PLAYER_WIDTH, PLAYER_HEIGHT, 300, SCREEN_HEIGHT - 100, 8)
ball = Ball("assets/player.png", BALL_SIZE, BALL_START_X, BALL_START_Y, 8, -30)

# brick
color = COLOR_BLUE
row_y = 70

for i in range(0, 6):
    bricks.append([])
    brick_x = FIRST_BRICK_X
    for j in range(0, 6):
        if i == 2:  # Change color of bricks
            color = COLOR_GREEN
        elif i == 4:
            color = COLOR_ORANGE
        bricks[i].append(Brick("assets/player.png", "h", BRICK_WIDTH, BRICK_HEIGHT, brick_x, row_y, color))
        brick_x += BRICK_WIDTH + BRICK_OFFSET
    row_y += 30
Game_Status.bricks_alive = 36

# victory
victory = False

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_1.move_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_1.move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_1.move_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_1.move_right = False

    # checking the victory condition
    if not Game_Status.bricks_alive == 0 and Game_Status.player_lives > 0:
        # clear screen
        screen.fill(COLOR_BLACK)

        player_1.move(0, SCREEN_WIDTH - PLAYER_WIDTH)
        ball.move(0, SCREEN_WIDTH - BALL_SIZE, 0, SCREEN_HEIGHT - BALL_SIZE)

        lives_text = FONT.render(str(Game_Status.player_lives), True, COLOR_WHITE, COLOR_BLACK)
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.center = (lives_text_rect.width,
                                  lives_text_rect.height)

        score_text = FONT.render(str(Game_Status.player_score), True, COLOR_WHITE, COLOR_BLACK)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (SCREEN_WIDTH - score_text_rect.width,
                                  score_text_rect.height)

        # drawing objects
        screen.blit(score_text, score_text_rect)
        screen.blit(lives_text, lives_text_rect)
        screen.blit(ball.game_object, (ball.x, ball.y))
        screen.blit(player_1.game_object, (player_1.x, player_1.y))  # SCREEN_HEIGHT - 100))

        for x in range(0, 6):
            for y in range(0, 6):
                if (not bricks[x][y].destroyed):
                    screen.blit(bricks[x][y].game_object, (bricks[x][y].x, bricks[x][y].y))
    elif Game_Status.player_lives > 0:
        # clear screen
        screen.fill(COLOR_BLACK)

        victory_text = FONT.render("YOU WIN", True, COLOR_WHITE, COLOR_BLACK)
        victory_text_rect = victory_text.get_rect()
        victory_text_rect.center = (SCREEN_WIDTH / 2,
                                    SCREEN_HEIGHT / 2 - victory_text_rect.height * 4)
        screen.blit(victory_text, victory_text_rect)

        score_text = FONT.render("SCORE:" + str(Game_Status.player_score), True, COLOR_WHITE, COLOR_BLACK)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (score_text_rect.width / 2 + 30,
                                  victory_text_rect.bottom + victory_text_rect.height * 2)
        screen.blit(score_text, score_text_rect)

        extra_score_text = FONT.render("EXTRA LIVES: " + str(Game_Status.player_lives - 1), True, COLOR_WHITE,
                                       COLOR_BLACK)
        extra_score_text_rect = extra_score_text.get_rect()
        extra_score_text_rect.center = (extra_score_text_rect.width / 2 + 30,
                                        score_text_rect.bottom + score_text_rect.height)
        screen.blit(extra_score_text, extra_score_text_rect)

        total_score_text = FONT.render(
            "TOTAL SCORE:" + str(Game_Status.player_score + (Game_Status.player_lives - 1) * 50), True, COLOR_WHITE,
            COLOR_BLACK)
        total_score_text_rect = total_score_text.get_rect()
        total_score_text_rect.center = (total_score_text_rect.width / 2 + 30,
                                        extra_score_text_rect.bottom + extra_score_text_rect.height * 2)
        screen.blit(total_score_text, total_score_text_rect)

    else:
        # clear screen
        screen.fill(COLOR_BLACK)

        defeat_text = FONT.render('YOU LOSE', True, COLOR_WHITE, COLOR_BLACK)
        defeat_text_rect = defeat_text.get_rect()
        defeat_text_rect.center = (SCREEN_WIDTH / 2,
                                   SCREEN_HEIGHT / 2)

        screen.blit(defeat_text, defeat_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
