-- ==============================
-- DATABASE SETUP
-- ==============================

CREATE DATABASE IF NOT EXISTS trust_score_db;
USE trust_score_db;

-- ==============================
-- USERS TABLE
-- ==============================

CREATE TABLE users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('USER','ADMIN') DEFAULT 'USER',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================
-- QUERIES TABLE
-- ==============================

CREATE TABLE queries (
    query_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT,
    query_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
);

-- ==============================
-- AI RESPONSES TABLE
-- ==============================

CREATE TABLE ai_responses (
    response_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    query_id BIGINT,
    response_text TEXT NOT NULL,
    model_name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (query_id) REFERENCES queries(query_id)
        ON DELETE CASCADE
);

-- ==============================
-- EVIDENCE TABLE
-- ==============================

CREATE TABLE evidence (
    evidence_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT,
    source_url TEXT,
    relevance_score FLOAT,
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id)
        ON DELETE CASCADE
);

-- ==============================
-- HALLUCINATION ANALYSIS TABLE
-- ==============================

CREATE TABLE hallucination_analysis (
    analysis_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT,
    hallucination_score FLOAT,
    issues_found TEXT,
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id)
        ON DELETE CASCADE
);

-- ==============================
-- TRUST SCORES TABLE
-- ==============================

CREATE TABLE trust_scores (
    trust_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT,
    trust_score FLOAT,
    explanation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id)
        ON DELETE CASCADE
);