import pygame
from colour import Color

pygame.display.set_caption('Hanoi Towers Simulator')

class Disk:
    vel = 15
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    MOVING = 10
    QUIET = 11

    HEIGHT = 35
    WIDTH = 80
    ADDITIONAL_WIDTH = 45

    def __init__(self, center, id_disk, color):
        self.rect = pygame.Rect((0, 0), (self.WIDTH + id_disk * self.ADDITIONAL_WIDTH, self.HEIGHT))
        self.rect.center = center
        self.color = color
        self.movements = []
        self.state = self.QUIET

    def is_moving(self):
        return len(self.movements) > 0

    def move_up(self, lmt_top):
        self.rect.y -= self.vel

        if self.rect.centery <= lmt_top:
            self.rect.centery = lmt_top
            self.state = self.QUIET

    def move_down(self, lmt_bot):
        self.rect.y += self.vel

        if self.rect.centery >= lmt_bot:
            self.rect.centery = lmt_bot
            self.state = self.QUIET

    def move_left(self, lmt_left):
        self.rect.x -= 2 * self.vel

        if self.rect.centerx <= lmt_left:
            self.rect.centerx = lmt_left
            self.state = self.QUIET

    def move_right(self, lmt_right):
        self.rect.x += 2 * self.vel

        if self.rect.centerx >= lmt_right:
            self.rect.centerx = lmt_right
            self.state = self.QUIET
    
    def move(self):
        if len(self.movements) == 0: return

        self.state = self.MOVING

        direction, lmt = self.movements[0]
            
        if direction == self.UP: self.move_up(lmt)
        elif direction == self.DOWN: self.move_down(lmt)
        elif direction == self.LEFT: self.move_left(lmt)
        elif direction == self.RIGHT: self.move_right(lmt)

        if self.state == self.QUIET:
            self.movements.pop(0)

    def add_movement(self, direction, lmt):
        self.movements.append((direction, lmt))

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=10)
    
def move_disk(positions, disks, posts, source_post_id, target_post_id):
    id_disk = positions[source_post_id].pop(-1)
    
    source_post = posts[source_post_id]
    target_post = posts[target_post_id]

    disks[id_disk].add_movement(Disk.UP, source_post.top - Disk.HEIGHT // 2)

    if source_post.centerx < target_post.centerx:
        disks[id_disk].add_movement(Disk.RIGHT, target_post.centerx)
    else:
        disks[id_disk].add_movement(Disk.LEFT, target_post.centerx)

    disks[id_disk].add_movement(Disk.DOWN, target_post.bottom - len(positions[target_post_id]) * Disk.HEIGHT - Disk.HEIGHT // 2)

    positions[target_post_id].append(id_disk)

def hanoi(n, source, target, other):
    if n == 1:
        return [(source, target)]
    
    ans = []
    ans += hanoi(n-1, source, other, target)
    ans += [(source, target)]
    ans += hanoi(n-1, other, target, source)

    return ans

def main():
    WIDTH, HEIGHT = 1200, 800
    surf = pygame.display.set_mode((WIDTH, HEIGHT))
    BG_COLOR = (12, 53, 106)

    # ==== POSTS ====

    WIDTH_POST = 25
    HEIGHT_POST = 400
    COLOR_POST = (222, 143, 95)

    posts = []
    
    for i in range(3):
        centerx = 200 + 400 * i
        centery = HEIGHT // 2

        post = pygame.Rect((0, 0), (WIDTH_POST, HEIGHT_POST))
        post.center = (centerx, centery)

        posts.append(post)

    # === DISKS ====

    n_disks = 6

    colors = [(95, 134, 112),
              (255, 152, 0),
              (184, 0, 0),
              (56, 135, 190),
              (195, 172, 208),
              (251, 236, 178)]

    positions = [[], [], []]

    disks = []

    for i in reversed(range(n_disks)):
        disks_inserted = len(disks)
        disks.append(Disk((posts[0].centerx, posts[0].bottom - disks_inserted * Disk.HEIGHT - Disk.HEIGHT // 2), i, colors[i]))
        positions[0].append(i)

    disks.reverse()

    running = True

    clock = pygame.time.Clock()

    some_disk_is_moving = False

    run_hanoi = False
    moves_list = hanoi(n_disks, 0, 2, 1)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    run_hanoi = not run_hanoi

        if run_hanoi:
            if not some_disk_is_moving:
                if len(moves_list) > 0:
                    source, target = moves_list[0]
                    moves_list.pop(0)
                    move_disk(positions, disks, posts, source, target)


        some_disk_is_moving = False
        for disk in disks:
            disk.move()
            if disk.is_moving(): 
                some_disk_is_moving = True

        surf.fill(BG_COLOR)

        for post in posts:
            pygame.draw.rect(surf, COLOR_POST, post)

        for disk in disks:
            disk.draw(surf)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
