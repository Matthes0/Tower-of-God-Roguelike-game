import fractions
import math
def scan(row):
    import main
    rows = [row]
    while rows:
        row = rows.pop()
        prev_tile_y = None
        prev_tile_x = None
        for tile_y, tile_x in row.tiles():
            if main.terrain_map[tile_y][tile_x].passable is False: # or is_symmetric(row, tile):

            if main.terrain_map[prev_tile_y][prev_tile_x].passable is False and main.terrain_map[tile_y][tile_x].passable is True:
                row.start_slope = slope(tile)
            if main.terrain_map[prev_tile_y][prev_tile_x].passable is True and main.terrain_map[tile_y][tile_x].passable is False:
                next_row = row.next()
                next_row.end_slope = slope(tile)
                rows.append(next_row)
            prev_tile_y = tile_y
            prev_tile_x = tile_x
        if main.terrain_map[prev_tile_y][prev_tile_x].passable is True:
            rows.append(row.next())

def shadowcast(actor):
    import main
    main.terrain_map[actor.y][actor.x].visible = True
    for i in range(4):
        direction = Quadrant(i, actor.y, actor.x)
        start_row = Row(1, fractions.Fraction(-1),fractions.Fraction(1))


class Quadrant:
    north = 0
    east = 1
    south = 2
    west = 3

    def __init__(self, direction, start_y, start_x):
        self.direction = direction
        self.start_y = start_y
        self.start_x = start_x


class Row:
    def __init__(self, depth, start, end):
        self.depth = depth
        self.start = start
        self.end = end

    def tiles(self):
        min_col = math.floor(self.depth * self.start)
        max_col = math.ceil(self.depth * self.end)
        for col in range(min_col, max_col + 1):
            yield self.depth, col
