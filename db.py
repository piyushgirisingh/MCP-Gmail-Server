import sqlite3

def init_db():
    conn = sqlite3.connect("applications.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY,
        company TEXT,
        role TEXT,
        applied_date TEXT,
        source TEXT,
        email_id TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()

def save_application(company, role, date, source, email_id):
    conn = sqlite3.connect("applications.db")
    c = conn.cursor()

    c.execute("""
    INSERT OR IGNORE INTO applications
    (company, role, applied_date, source, email_id)
    VALUES (?, ?, ?, ?, ?)
    """, (company, role, date, source, email_id))

    conn.commit()
    conn.close()
