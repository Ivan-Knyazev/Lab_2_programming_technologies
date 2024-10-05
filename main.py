from game_app.objects import Archer, Fort, MobileHouse


def print_tests_data(header: str, objects: list) -> None:
    print("[TEST]", header)
    print("-" * 70)
    print(*objects, sep="\n")
    print("-" * 70, "\n")


def test_objects() -> None:
    archer_1 = Archer(id=1, name="archer_1", X=1, Y=1)
    archer_2 = Archer(id=1, name="archer_2", X=1, Y=1)
    fort = Fort(id=2, name="fort_1", X=12, Y=15, is_build=True)
    mobile_house = MobileHouse(
        id=3, name="mobile_house_1", X=14, Y=20, is_build=True)
    print_tests_data("At the start:", [archer_1, archer_2, fort, mobile_house])

    archer_1.attack(archer_2)
    archer_2.move(30, 40)
    print_tests_data("After move and attack 'archer_2' from archers:",
                     [archer_1, archer_2])

    fort.attack(archer_1)
    print_tests_data("After attack 'archer_1' from fort:",
                     [archer_1, archer_2])

    mobile_house.move(10, 20)
    print_tests_data("After move mobile_house:", [mobile_house])

    tests_of_methods_1 = [
        f"getId() -> int: {archer_1.getId()}",
        f"getName() -> str: {archer_1.getName()}",
        f"getX() -> int: {archer_1.getX()}",
        f"getY() -> int: {archer_1.getY()}",
        f"isAlive() -> bool: {archer_1.isAlive()}",
        f"getHp() -> float: {archer_1.getHp()}"
    ]
    print_tests_data(
        "Methods of the 'archer_1' object:", tests_of_methods_1)

    tests_of_methods_2 = [
        f"getId() -> int: {fort.getId()}",
        f"getName() -> str: {fort.getName()}",
        f"getX() -> int: {fort.getX()}",
        f"getY() -> int: {fort.getY()}",
        f"isBuilt() -> bool: {fort.isBuilt()}"
    ]
    print_tests_data("Methods of the 'fort' object:",
                     tests_of_methods_2)

    for attack in range(10):
        try:
            fort.attack(archer_2)
            print_tests_data(f"After attack 'archer_2' #{
                             attack+1} from fort:", [archer_2])
        except ValueError as err:
            print(f"Exception: type=ValueError, msg='{err}'")
            break


if __name__ == "__main__":
    test_objects()
