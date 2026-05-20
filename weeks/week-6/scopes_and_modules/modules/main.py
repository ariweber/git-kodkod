import math
import mathutils
from mathutils import square, cube
from tools import add
from datetime import datetime as td

    
def public_names(m):
    return sorted([name for name in dir(m) if not name.startswith('_')])

def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag








def main():
    print(square(5))
    print(cube(3))
    print(mathutils.square(4))
    print(mathutils.cube(2))


if __name__ == "__main__":
    main()

main()
print(public_names(math)) 