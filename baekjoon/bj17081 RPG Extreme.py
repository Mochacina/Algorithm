class Hero:
    def __init__(self):
        self.level = 1
        self.hp = 20
        self.max_hp = 20
        self.base_attack = 2
        self.base_defense = 2
        self.exp = 0
        self.weapon = None
        self.armor = None
        self.accessories = []
        self.position = [0, 0]
        
    def show(self):
        print(f'LV : {self.level}')
        print(f'HP : {self.hp}/{self.max_hp}')
        print(f'ATT : {self.base_attack}+{self.weapon.attack if self.weapon else 0}')
        print(f'DEF : {self.base_defense}+{self.armor.defense if self.armor else 0}')
        print(f'EXP : {self.exp}/{self.level*5}')
        
class Monster:
    def __init__(self, name, attack, defense, max_hp, exp, position):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = max_hp
        self.max_hp = max_hp
        self.exp = exp
        self.position = position
        self.is_boss = False
        
class ItemBox:
    def __init__(self, item_type, effect, position):
        self.item_type = item_type
        self.effect = effect
        self.position = position

class GameMap:
    def __init__(self, grid, hero, monsters, item_boxes):
        self.grid = grid
        self.hero = hero
        self.monsters = monsters
        self.item_boxes = item_boxes
        
N,M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
hero = Hero()
monsters = []
item_boxes = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == '@':
            hero.position = [i, j]
hero_moves = input()
while 1:
    try:
        x, y, *l = input().split()
        if len(l) == 5:
            monsters.append(Monster(l[0], int(l[1]), int(l[2]), int(l[3]), int(l[4]), [int(x), int(y)]))
        elif len(l) == 2:
            item_boxes.append(ItemBox(l[0], l[1], [int(x), int(y)]))
    except: break
hero.show()
print(monsters)
print(item_boxes)
game_map = GameMap(grid, hero, monsters, item_boxes)
def simulate_combat(hero, monster):
    while True:
        # Hero attacks first
        damage_to_monster = max(1, hero.base_attack + (hero.weapon if hero.weapon else 0) - monster.defense)
        monster.hp -= damage_to_monster
        if monster.hp <= 0:
            return True  # Monster defeated

        # Monster retaliates
        damage_to_hero = max(1, monster.attack - (hero.base_defense + (hero.armor if hero.armor else 0)))
        hero.hp -= damage_to_hero
        if hero.hp <= 0:
            return False  # Hero defeated

def process_item_box(hero, item_box):
    if item_box.item_type == 'W':
        hero.weapon = item_box.effect
    elif item_box.item_type == 'A':
        hero.armor = item_box.effect
    elif item_box.item_type == 'O':
        if len(hero.accessories) < 4 and item_box.effect not in hero.accessories:
            hero.accessories.append(item_box.effect)

def move_hero(game_map, moves):
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    hero = game_map.hero
    grid = game_map.grid
    monsters_dict = {monster.position: monster for monster in game_map.monsters}
    item_boxes = {(box.position[0], box.position[1]): box for box in game_map.item_boxes}
    turn_count = 0
    hero_killed_by = None

    def in_bounds(pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    for move in moves:
        turn_count += 1
        dx, dy = directions[move]
        new_position = (hero.position[0] + dx, hero.position[1] + dy)
        
        if not in_bounds(new_position) or grid[new_position[0]][new_position[1]] == '#':
            continue  # Skip move if out of bounds or hits a wall
        
        hero.position = new_position
        
        # Check for item box at the new position
        if hero.position in item_boxes:
            item_box = item_boxes.pop(hero.position)
            process_item_box(hero, item_box)
            grid[hero.position[0]][hero.position[1]] = '.'
        
        # Check for monster at the new position
        if hero.position in monsters_dict:
            monster = monsters_dict[hero.position]
            combat_result = simulate_combat(hero, monster)
            if not combat_result:  # Hero defeated
                hero_killed_by = monster.name
                return turn_count, f"YOU HAVE BEEN KILLED BY {hero_killed_by}"
            else:
                monsters_dict.pop(hero.position)  # Remove defeated monster
                grid[hero.position[0]][hero.position[1]] = '.'
        
        # Check for spike trap
        if grid[hero.position[0]][hero.position[1]] == '^':
            hero.hp -= 5  # Damage from spike trap
            if hero.hp <= 0:
                hero_killed_by = "SPIKE TRAP"
                return turn_count, f"YOU HAVE BEEN KILLED BY {hero_killed_by}"

        grid[hero.position[0]][hero.position[1]] = '@'  # Move hero to new position

    return turn_count, "Press any key to continue."

move_hero(game_map, hero_moves)