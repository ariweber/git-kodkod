from db import get_connection

FIRST_NAMES = [
    "Yossi", "Dana", "Avi", "Noa", "Eitan", "Shira", "Roi", "Maya", "Omer", "Tamar",
    "Gal", "Yael", "Nir", "Liron", "Tom", "Hadar", "Idan", "Mor", "Lior", "Adi",
]
LAST_NAMES = [
    "Cohen", "Levi", "Mizrahi", "Peretz", "Bitton", "Avraham", "Friedman", "Katz",
    "Azoulay", "Dahan", "Shalev", "Barak", "Golan", "Naor", "Regev",
]
RANKS = [
    "Private", "Corporal", "Sergeant", "Staff Sergeant", "Sergeant First Class",
    "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel",
]
UNITS = [
    "Golani", "Givati", "Paratroopers", "Nahal", "Armored Corps", "Artillery",
    "Combat Engineering", "Intelligence", "Air Force", "Navy", "8200", "Cyber",
]


def seed(count: int = 100):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, `rank`, unit, active) VALUES (%s, %s, %s, %s)"
    rows = []
    for i in range(count):
        name = f"{FIRST_NAMES[i % len(FIRST_NAMES)]} {LAST_NAMES[i % len(LAST_NAMES)]}"
        rank = RANKS[i % len(RANKS)]
        unit = UNITS[i % len(UNITS)]
        active = i % 4 != 0  # ~75% active, 25% inactive
        rows.append((name, rank, unit, active))
    cursor.executemany(sql, rows)
    conn.commit()
    print(f"Inserted {cursor.rowcount} soldiers.")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    seed(200)
