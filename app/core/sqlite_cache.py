import sqlite3
import hashlib
import json
from functools import wraps

# Initialize SQLite database for caching
DB_PATH = "cache.db"

def init_db():
    """Creates the cache table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        conn.commit()

# Run database initialization
init_db()

def db_cache(func):
    """Decorator to cache function results in SQLite."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Generate a unique key based on function name and arguments
        cache_key = hashlib.md5(f"{func.__name__}{args}{kwargs}".encode()).hexdigest()

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Check if result is cached
            cursor.execute("SELECT value FROM cache WHERE key=?", (cache_key,))
            row = cursor.fetchone()
            
            if row:
                return json.loads(row[0])  # Load cached result
            
            # Compute function result
            result = func(*args, **kwargs)
            
            # Store result in cache
            cursor.execute("INSERT INTO cache (key, value) VALUES (?, ?)", 
                           (cache_key, json.dumps(result)))
            conn.commit()
        
        return result

    return wrapper

