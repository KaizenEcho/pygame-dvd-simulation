# ====================== imports =======================

import pygame
import random

# ======================================================
# ==================== pygame setup ====================

# main settings
fps_limit = 60 # FPS limit
colides = 0 # current colides
info_text_size = 30 # the info text size
speed = 1 # starting speed

# DVD coliding checker
collide_x = True
collide_y = True

# DVD starting colors
r_color = 255
g_color = 255
b_color = 255

# screen settings
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# text fonts
DVD_font = pygame.font.Font(None, 128)
info_font = pygame.font.Font(None, info_text_size)

# DVD center spawn
DVD_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# ======================================================
# ======================= game =========================

while running:

    # ======================================================
    # ======================= setup ========================

    # startable setup + button click check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # exit button
            running = False # stop the game
        elif event.type == pygame.MOUSEBUTTONDOWN: # if button speed button clicked
            if more_speed_rect.collidepoint(event.pos): # speed adding button
                speed += 1 # speed adding
            elif less_speed_rect.collidepoint(event.pos) and speed != 0: # speed decrease button
                speed -= 1 #speed decrease

    # screen color
    screen.fill("black")

    # ======================================================
    # ==================== main script =====================
    # ===================== HUD setup ======================

    # DVD setup + appear
    text = DVD_font.render("DVD", True, (r_color, g_color, b_color))
    screen.blit(text, DVD_pos)

    # current DVD colors setup + appear
    info = info_font.render(f"red: {r_color} green: {g_color} blue: {b_color}", True, (255, 255, 255))
    screen.blit(info, (10, (info_text_size//5)*1))

    # current game FPS setup + appear
    clock.tick(fps_limit)
    fps = int(clock.get_fps())
    current_fps = info_font.render(f"current fps: {fps}", True, (255, 255, 255))
    screen.blit(current_fps, (10, (info_text_size//5)*9))

    # colide counter setup + appear
    current_colides = info_font.render(f"colided: {colides}", True, (255, 255, 255))
    screen.blit(current_colides, (10, (info_text_size//5)*13))

    # buttons setup + current speed text
    more_speed = info_font.render("+", True, (100, 255, 100)) # rise speed button
    less_speed = info_font.render("-", True, (255, 100, 100)) # decrease speed button
    speed_stat = info_font.render(f"speed {speed}", True, (255, 255, 255)) # current speed text

    # backstage rectangular pressable button creation
    more_speed_rect = more_speed.get_rect(topleft=((info_text_size//5)*1, (info_text_size//5)*5))
    less_speed_rect = less_speed.get_rect(topleft=((info_text_size//5)*5, (info_text_size//5)*5))

    # button appear
    screen.blit(more_speed, more_speed_rect)
    screen.blit(less_speed, less_speed_rect)
    screen.blit(speed_stat, ((info_text_size//5)*8, (info_text_size//5)*5))

    # ======================================================
    # ================= DVD current move ===================

    if collide_x:
        DVD_pos.x += speed # moving right
    else:
        DVD_pos.x -= speed # moving left

    if collide_y:
        DVD_pos.y += speed # moving down
    else:
        DVD_pos.y -= speed  # moving up

    # ======================================================
    # ==================== DVD script ======================

    # colides by screen width
    if DVD_pos.x <= 0: # outbound from left limit of screen
        DVD_pos.x = 0 # back to the screen when outbound
        colides += 1 # colide count
        r_color, g_color, b_color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255) # randomise colors when colide
        collide_x = True # after colide going to right
    elif DVD_pos.x >= screen.get_width() - text.get_width(): # outbound from right limit of screen
        DVD_pos.x = screen.get_width() - text.get_width() # back to the screen when outbound
        colides += 1 # colide count
        r_color, g_color, b_color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255) # randomise colors when colide
        collide_x = False # after colide going to left

    # colides by screen height
    if DVD_pos.y <= 0: # outbound from upper limit of screen
        DVD_pos.y = 0 # back to the screen when outbound
        colides += 1 # colide count
        r_color, g_color, b_color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255) # randomise colors when colide
        collide_y = True # after colide going to down
    elif DVD_pos.y >= screen.get_height() - text.get_height(): # outbound from down limit of screen
        DVD_pos.y = screen.get_height() - text.get_height() # back to the screen when outbound
        colides += 1 # colide count
        r_color, g_color, b_color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255) # randomise colors when colide
        collide_y = False # after colide going to up

    # ======================================================
    # ================== screen appear =====================

    pygame.display.flip()

    # ======================================================

pygame.quit()

# ======================================================