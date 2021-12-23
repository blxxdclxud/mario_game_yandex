from classes import *
from CONSTANTS import WIDTH, HEIGHT

player = None
level_x, level_y = None, None
preview = False


def generate_level(level):
    global MAP
    MAP = level

    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == BOX:
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def load_level(filename):
    filename = "data/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Для запуска игры нажмите любую",
                  "клавишу на клавиатуре или кнопку мыши."]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

        global preview

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                preview = True
                return
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    player, level_x, level_y = generate_level(load_level('map_1.txt'))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pos_x, pos_y = player.pos_x, player.pos_y
                signal = pygame.key.get_pressed()

                if signal[pygame.K_RIGHT] and pos_x + 1 < level_x and \
                        MAP[pos_y][pos_x + 1] != BOX:
                    player.kill()
                    player = Player(pos_x + 1, pos_y)
                elif signal[pygame.K_LEFT] and pos_x - 1 >= 0 and \
                        MAP[pos_y][pos_x - 1] != BOX:
                    player.kill()
                    player = Player(pos_x - 1, pos_y)
                elif signal[pygame.K_UP] and pos_y - 1 >= 0 and \
                        MAP[pos_y - 1][pos_x] != BOX:
                    player.kill()
                    player = Player(pos_x, pos_y - 1)
                elif signal[pygame.K_DOWN] and pos_y + 1 < level_y and \
                        MAP[pos_y + 1][pos_x] != BOX:
                    player.kill()
                    player = Player(pos_x, pos_y + 1)

        if not preview:
            start_screen()

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
