class Hero:
    def __init__(self, position):
        self.level = 1
        self.hp = 20
        self.max_hp = 20
        self.base_attack = 2
        self.base_defense = 2
        self.exp = 0
        self.weapon = None
        self.armor = None
        self.accessories = []
        self.position = position  # Fix: Pass the position as a single argument to the tuple() function
        self.initial_position = self.position
        
    def show(self):
        print(f'LV : {self.level}')
        print(f'HP : {self.hp}/{self.max_hp}')
        print(f'ATT : {self.base_attack}+{self.weapon if self.weapon else 0}')
        print(f'DEF : {self.base_defense}+{self.armor if self.armor else 0}')
        print(f'EXP : {self.exp}/{self.level*5}')
        #print(f'Equipped : {self.accessories}')
        
    def get_exp(self, exp):
        exp = int(exp * (1.2 if 'EX' in self.accessories else 1))
        self.exp += exp
        while self.exp >= self.level*5:
            self.exp = 0
            self.level += 1
            self.max_hp += 5
            self.hp = self.max_hp
            self.base_attack += 2
            self.base_defense += 2
            
    def regeneration(self):
        self.hp = min(self.hp + 3, self.max_hp)
        
    def reincarnation(self):
        self.hp = self.max_hp
        self.position = self.initial_position
        self.accessories.remove('RE')
        
class Monster:
    def __init__(self, name, attack, defense, max_hp, exp, position, is_boss):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = max_hp
        self.max_hp = max_hp
        self.exp = exp
        self.position = tuple(position)
        self.is_boss = is_boss
        
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
        
def simulate_combat(hero, monster):
    first_attack = True
    hunter = False
    courage = True if 'CO' in hero.accessories else False
    dexterity = True if 'DX' in hero.accessories else False
    if 'HU' in hero.accessories and monster.is_boss:
        hero.hp = hero.max_hp
        hunter = True
    while True:
        # Hero attacks first
        damage_modifier = 1
        if first_attack: 
            if courage and dexterity: damage_modifier = 3
            elif courage:  damage_modifier = 2
        damage_to_monster = max(1, (hero.base_attack + (hero.weapon if hero.weapon else 0))*damage_modifier - monster.defense)
        monster.hp -= damage_to_monster
        if monster.hp <= 0:
            return True  # Monster defeated

        # Monster retaliates
        damage_to_hero = max(1, monster.attack - (hero.base_defense + (hero.armor if hero.armor else 0)))
        if first_attack and hunter: damage_to_hero = 0
        hero.hp -= damage_to_hero
        if hero.hp <= 0:
            return False  # Hero defeated
        
        first_attack = False

def process_item_box(hero, item_box):
    if item_box.item_type == 'W':
        hero.weapon = int(item_box.effect)
    elif item_box.item_type == 'A':
        hero.armor = int(item_box.effect)
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
            pass
        else: 
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
                    if 'RE' in hero.accessories:
                        monster.hp = monster.max_hp
                        hero.reincarnation()
                    else:
                        hero_killed_by = monster.name
                        hero.hp = 0
                        return turn_count, f"YOU HAVE BEEN KILLED BY {hero_killed_by}.."
                else:
                    if 'HR' in hero.accessories: hero.regeneration()
                    hero.get_exp(monster.exp)
                    if monster.is_boss:
                        return turn_count, f"YOU WIN!"
                    monsters_dict.pop(hero.position)  # Remove defeated monster
                    grid[hero.position[0]][hero.position[1]] = '.'
        
        # Check for spike trap
        if grid[hero.position[0]][hero.position[1]] == '^':
            if 'DX' in hero.accessories: # Damage from spike trap
                hero.hp -= 1
            else:
                hero.hp -= 5
            if hero.hp <= 0:
                if 'RE' in hero.accessories:
                    hero.reincarnation()
                else:
                    hero_killed_by = "SPIKE TRAP"
                    hero.hp = 0
                    return turn_count, f"YOU HAVE BEEN KILLED BY {hero_killed_by}.."

    return turn_count, "Press any key to continue."
        
N,M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

monsters = []
item_boxes = []
isBoss = tuple([])
for i in range(N):
    for j in range(M):
        if grid[i][j] == '@':
            hero = Hero(tuple([i, j]))
            grid[i][j] = '.'
        if grid[i][j] == 'M':
            isBoss = tuple([i, j])
hero_moves = input()
while 1:
    try:
        x, y, *l = input().split()
        if len(l) == 5:
            monsters.append(Monster(l[0], int(l[1]), int(l[2]), int(l[3]), int(l[4]), tuple([int(x)-1, int(y)-1]), True if tuple([int(x)-1, int(y)-1]) == isBoss else False))
        elif len(l) == 2:
            item_boxes.append(ItemBox(l[0], l[1], tuple([int(x)-1, int(y)-1])))
    except: break
game_map = GameMap(grid, hero, monsters, item_boxes)
turn_count, txt = move_hero(game_map, hero_moves)
for i in range(len(game_map.grid)):
    if i == game_map.hero.position[0] and game_map.hero.hp > 0:
        print(''.join(game_map.grid[i][:game_map.hero.position[1]]+['@']+game_map.grid[i][game_map.hero.position[1]+1:]))
    else:
        print(''.join(game_map.grid[i]))
print(f"Passed Turns : {turn_count}")
hero.show()
print(txt)