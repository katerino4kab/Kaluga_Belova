import sqlite3


def fetch_trolls(min_gold, min_jewelry, min_total_wealth):
    connection = sqlite3.connect('gullibility.db')
    cursor = connection.cursor()

    query = """
        SELECT DISTINCT name, place
        FROM Wealth
        WHERE (gold >= ? AND jewelry >= ?) OR (gold + silver + jewelry >= ?)
    """

    cursor.execute(query, (min_gold, min_jewelry, min_total_wealth))
    results = cursor.fetchall()

    connection.close()

    return results


def main():
    input_data = input("Введите минимальное количество золота, драгоценных камней и общего богатства: ")
    min_gold, min_jewelry, min_total_wealth = map(int, input_data.split())

    trolls = fetch_trolls(min_gold, min_jewelry, min_total_wealth)

    if trolls:
        names = sorted(set(troll[0] for troll in trolls))
        places = sorted(set(troll[1] for troll in trolls))

        print(", ".join(names))
        print(", ".join(places))
    else:
        print("Нет подходящих троллей.")


if __name__ == "__main__":
    main()
