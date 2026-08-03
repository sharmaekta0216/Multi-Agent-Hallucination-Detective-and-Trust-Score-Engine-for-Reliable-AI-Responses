# from database import get_connection
import database

print("Database module path:", database.__file__)

from database import get_connection
print("Database service module loaded successfully:",
get_connection.__module__)
print(get_connection)
# -----------------------------
# USER OPERATIONS
# -----------------------------

def create_user(full_name, email, password_hash):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO users
    (full_name, email, password_hash)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (full_name, email, password_hash))

    conn.commit()

    cursor.close()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


# -----------------------------
# QUERY
# -----------------------------

# def save_query(user_id, query_text):
#     conn = get_connection()
#     cursor = conn.cursor()

#     sql = """
#     INSERT INTO queries(user_id, query_text)
#     VALUES (%s, %s)
#     """

#     cursor.execute(sql, (user_id, query_text))
#     conn.commit()

#     query_id = cursor.lastrowid

#     cursor.close()
#     conn.close()

#     return query_id

def save_query(user_id, query_text):
    print("Inside save_query")
    print("1")
    conn = get_connection()
    print("2")

    cursor = conn.cursor()
    print("3")

    sql = """
    INSERT INTO queries(user_id, query_text)
    VALUES (%s, %s)
    """

    print("4")
    cursor.execute(sql, (user_id, query_text))
    print("5")

    conn.commit()
    print("6")

    query_id = cursor.lastrowid
    print("7")

    cursor.close()
    conn.close()
    print("8")

    return query_id
# -----------------------------
# RESPONSE
# -----------------------------

def save_response(query_id, response_text,
                  model_name="gemini-3.6-flash",
                  response_time_ms=None):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO ai_responses
    (query_id, response_text, model_name, response_time_ms)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            query_id,
            response_text,
            model_name,
            response_time_ms
        )
    )

    conn.commit()

    response_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return response_id


# -----------------------------
# TRUST SCORE
# -----------------------------
def save_trust_score(
        response_id,
        fact_score,
        logic_score,
        evidence_score,
        hallucination_score,
        final_trust_score,
        trust_level):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO trust_scores
    (
        response_id,
        fact_score,
        logic_score,
        evidence_score,
        hallucination_score,
        final_trust_score,
        trust_level
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            response_id,
            fact_score,
            logic_score,
            evidence_score,
            hallucination_score,
            final_trust_score,
            trust_level
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    # -----------------------------
# HISTORY
# -----------------------------

def get_user_history(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT
        q.query_id,
        q.query_text,
        q.created_at,
        r.response_text,
        t.final_trust_score,
        t.trust_level
    FROM queries q
    JOIN ai_responses r
        ON q.query_id = r.query_id
    JOIN trust_scores t
        ON r.response_id = t.response_id
    WHERE q.user_id = %s
    ORDER BY q.created_at DESC
    """

    cursor.execute(sql, (user_id,))
    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history
# -----------------------------
# EVIDENCE
# -----------------------------

def save_evidence(
    response_id,
    source_title,
    source_url,
    evidence_text
):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO evidence
    (
        response_id,
        source_title,
        source_url,
        evidence_text
    )
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (
            response_id,
            source_title,
            source_url,
            evidence_text
        )
    )

    conn.commit()

    cursor.close()
    conn.close()
    # -----------------------------
# HALLUCINATION ANALYSIS
# -----------------------------

def save_hallucination_analysis(
    response_id,
    hallucination_score,
    unsupported_claims,
    contradiction_count,
    remarks
):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO hallucination_analysis
    (
        response_id,
        hallucination_score,
        unsupported_claims,
        contradiction_count,
        remarks
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (
            response_id,
            hallucination_score,
            unsupported_claims,
            contradiction_count,
            remarks
        )
    )

    conn.commit()

    cursor.close()
    conn.close()
