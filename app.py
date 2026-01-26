from flask import Flask, render_template, request, abort
import sqlite3
import hashlib
import hmac
import secrets

app = Flask(__name__)

SERVER_SECRET = "cloud_secret_key"

# ---- MANUAL DATABASE INIT ----
def init_db():
    conn = sqlite3.connect("security.db")
    cur = conn.cursor()

    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            anon_id TEXT PRIMARY KEY,
            secret_key TEXT
        )
    """)

    # Nonces table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS used_nonces (
            anon_id TEXT,
            nonce TEXT,
            PRIMARY KEY (anon_id, nonce)
        )
    """)

    conn.commit()
    conn.close()

# Call database init manually
init_db()
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        nonce = request.form.get("nonce")
        if not nonce:
            abort(400, "Missing authentication parameters")

        # Generate anonymous user ID
        anon_id = hashlib.sha256(username.encode()).hexdigest()

        # Connect to DB
        conn = sqlite3.connect("security.db")
        cur = conn.cursor()

        # Generate / fetch secret
        cur.execute("SELECT secret_key FROM users WHERE anon_id=?", (anon_id,))
        row = cur.fetchone()
        if row:
            secret = row[0]
        else:
            secret = secrets.token_hex(16)
            cur.execute("INSERT INTO users (anon_id, secret_key) VALUES (?, ?)", (anon_id, secret))
            conn.commit()

        # Check for replay
        cur.execute("SELECT 1 FROM used_nonces WHERE anon_id=? AND nonce=?", (anon_id, nonce))
        if cur.fetchone():
            conn.close()
            abort(403, "Replay detected")

        # Store nonce
        cur.execute("INSERT INTO used_nonces (anon_id, nonce) VALUES (?, ?)", (anon_id, nonce))
        conn.commit()
        conn.close()

        # Generate session key
        session_key = hmac.new(
            key=secret.encode(),
            msg=nonce.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        return render_template(
            "dashboard.html",
            anon_id=anon_id[:12],
            session_key=session_key[:12]
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
