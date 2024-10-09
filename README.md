# Lab №2 for Programming Technologies

Is a test task for creating some classes of game objects to wark with `OOP` and use `interfaces`, `inheritance` and `polymorphism`.

## For start:

Run this command in your shell in root directory of this project:

```bash
python3 main.py
```

The result of this script:

```
[TEST] At the start:
----------------------------------------------------------------------
Archer(id=1, name=archer_1, X=1, Y=1, is_alive=True, hp=100)
Archer(id=2, name=archer_2, X=1, Y=1, is_alive=True, hp=100)
Fort(id=3, name=fort_1, X=12, Y=15, is_build=True)
MobileHouse(id=4, name=mobile_house_1, X=14, Y=20, is_build=True)
---------------------------------------------------------------------- 

[TEST] After move and attack 'archer_2' from archers:
----------------------------------------------------------------------
Archer(id=1, name=archer_1, X=1, Y=1, is_alive=True, hp=100)
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=True, hp=76.0)
---------------------------------------------------------------------- 

[TEST] After attack 'archer_1' from fort:
----------------------------------------------------------------------
Archer(id=1, name=archer_1, X=1, Y=1, is_alive=True, hp=81.0)
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=True, hp=76.0)
---------------------------------------------------------------------- 

[TEST] After move mobile_house:
----------------------------------------------------------------------
MobileHouse(id=4, name=mobile_house_1, X=24, Y=40, is_build=True)
---------------------------------------------------------------------- 

[TEST] Methods of the 'archer_1' object:
----------------------------------------------------------------------
getId() -> int: 1
getName() -> str: archer_1
getX() -> int: 1
getY() -> int: 1
isAlive() -> bool: True
getHp() -> float: 81.0
---------------------------------------------------------------------- 

[TEST] Methods of the 'fort' object:
----------------------------------------------------------------------
getId() -> int: 3
getName() -> str: fort_1
getX() -> int: 12
getY() -> int: 15
isBuilt() -> bool: True
---------------------------------------------------------------------- 

[TEST] After attack 'archer_2' #1 from fort:
----------------------------------------------------------------------
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=True, hp=57.0)
---------------------------------------------------------------------- 

[TEST] After attack 'archer_2' #2 from fort:
----------------------------------------------------------------------
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=True, hp=38.0)
---------------------------------------------------------------------- 

[TEST] After attack 'archer_2' #3 from fort:
----------------------------------------------------------------------
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=True, hp=19.0)
---------------------------------------------------------------------- 

[TEST] After attack 'archer_2' #4 from fort:
----------------------------------------------------------------------
Archer(id=2, name=archer_2, X=31, Y=41, is_alive=False, hp=0.0)
---------------------------------------------------------------------- 

Exception: type=ValueError, msg='Damage of more hp!'
```

- **Вопрос:** почему при реализации задания на `Python`, после изменения сигнатуры метода интерефейса (например, `Movable`) в классе всё работает, хотя не должно (сигнатура самого интерфейса не соблюдена)?
  Проблема возникает при реализации через `abc` standart library, нужно проверить

<hr>

It was created on 05/10/24.