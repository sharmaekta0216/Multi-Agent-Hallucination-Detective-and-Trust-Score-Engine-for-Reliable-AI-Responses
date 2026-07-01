CREATE DATABASE IF NOT EXISTS trust_score_db;
USE trust_score_db;

-- USERS
CREATE TABLE users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('USER','ADMIN') DEFAULT 'USER',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- QUERIES
CREATE TABLE queries (
    query_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    query_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- AI RESPONSES
CREATE TABLE ai_responses (
    response_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    query_id BIGINT NOT NULL,
    response_text LONGTEXT NOT NULL,
    model_name VARCHAR(100),
    response_time_ms INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (query_id) REFERENCES queries(query_id) ON DELETE CASCADE
);

-- EVIDENCE
CREATE TABLE evidence (
    evidence_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT NOT NULL,
    source_title VARCHAR(255),
    source_url TEXT,
    evidence_text LONGTEXT,
    reliability_score DECIMAL(5,2),
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id) ON DELETE CASCADE
);

-- HALLUCINATION ANALYSIS
CREATE TABLE hallucination_analysis (
    analysis_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT NOT NULL,
    hallucination_score DECIMAL(5,2),
    unsupported_claims INT DEFAULT 0,
    contradiction_count INT DEFAULT 0,
    remarks TEXT,
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id) ON DELETE CASCADE
);

-- TRUST SCORES
CREATE TABLE trust_scores (
    trust_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    response_id BIGINT NOT NULL,
    fact_score DECIMAL(5,2),
    evidence_score DECIMAL(5,2),
    hallucination_score DECIMAL(5,2),
    final_trust_score DECIMAL(5,2),
    trust_level ENUM('LOW','MEDIUM','HIGH'),
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (response_id) REFERENCES ai_responses(response_id) ON DELETE CASCADE
);