from db import get_connection

def create(name: str, rank: str, unit: str, ac) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, `rank`, unit) VALUES (%s, %s, %s, %s)"
    values = (name, rank, unit)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id



def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    set_parts = [f"`{key}` = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]
    cursor.execute(sql, values)
    conn.commit()
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


def reset_table():
    conn = get_connection()
    cursor = conn.cursor()
    # TRUNCATE deletes all rows AND resets AUTO_INCREMENT back to 1
    cursor.execute("TRUNCATE TABLE soldiers")
    conn.commit()
    cursor.close()
    conn.close()





def get_all() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # returns dicts instead of
  
    cursor.execute("SELECT * FROM soldiers")
    rows = cursor.fetchall()
    print(type(rows))
    cursor.close()

    conn.close()
    return rows
 





def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
    row = cursor.fetchone() # returns one dict or None
    cursor.close()
    conn.close()
    return row


def get_names_and_ranks() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=False)
    cursor.execute("SELECT id, name, `rank` FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_rank(rank: str) -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute( "SELECT * FROM soldiers WHERE `rank` = %s", (rank,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows 

def search_by_name(term: str) -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s",(f"%{term}%",))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_active_sorted(order: str = "asc") -> list:
    if order.lower() not in ("asc", "desc"):
        order = "asc"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute(f"SELECT * FROM soldiers WHERE active = TRUE ORDER BY name {order.upper()}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_distinct_units() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT unit FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # fetchall returns tuples: [('8200',), ('9900',)]
    return [row[0] for row in rows]



def get_with_missing_rank() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE rank` IS NULL")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def count_by_unit() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT
    unit,
    COUNT(*) AS total
    FROM soldiers
    GROUP BY unit
    ORDER BY total DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_summary() -> dict:
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)
  cursor.execute("SELECT COUNT(*) AS total FROM soldiers")
  total = cursor.fetchone()["total"]
  cursor.execute("""SELECT COUNT(*) AS active FROM soldiers WHERE active =
TRUE""")
  active = cursor.fetchone()["active"]
  cursor.close()
  conn.close()
  return {"total": total, "active": active, "inactive": total - active}

