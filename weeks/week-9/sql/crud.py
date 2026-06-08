from db import get_connection

def create(name: str, rank: str, unit: str, active: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, `rank`, unit, active) VALUES (%s, %s, %s, %s)"
    values = (name, rank, unit, active)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM soldiers")
    a =  cursor.fetchall()
    for  s in a:
        print(s)
    # MySQL gives us the id it assigned
    cursor.close()
    conn.close()
    return new_id

def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
# Build the SET clause dynamically from the dict
    set_parts = [f"{key} = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    print(set_clause)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]
    print(values)
    cursor.execute(sql, values)
    conn.commit()
    cursor.execute("SELECT * FROM soldiers")
    a =  cursor.fetchall()
    for  s in a:
        print(s)
    changed = cursor.rowcount > 0 # False if id did not exist
    cursor.close()
    conn.close()
    return changed



def delete(soldier_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s", (soldier_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return deleted


def gat_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM soldiers")
    a =  cursor.fetchall()
    for  s in a:
        print(s)

gat_all()        


