# System Architecture — OIC Guardian 🚀

## 1. Overview

OIC Guardian acts as an intelligent middleware layer between Oracle Integration Cloud (OIC) and external systems.

It enhances:
- Observability
- Reliability
- Automation

---

## 2. High-Level Architecture
| OIC Guardian (Django Backend)            |
| ---------------------------------------- |
| - Deduplication Engine                   |
| - Logging Engine                         |
| - Token Manager                          |
| - Replay Engine                          |
| +--------------------------------------+ |
                    |
                    v

            +----------------------+
            | PostgreSQL Database |
            +----------------------+


---

## 3. Component Breakdown

### 3.1 OIC (Oracle Integration Cloud)
- Orchestrates integrations
- Calls OIC Guardian APIs
- Handles external system communication

---

### 3.2 OIC Guardian Backend

#### 🔹 Deduplication Engine
- Prevents duplicate message processing
- Uses unique message IDs

#### 🔹 Logging Engine
- Stores request/response payloads
- Tracks integration status

#### 🔹 Token Manager
- Stores OAuth tokens
- Automatically refreshes expired tokens

#### 🔹 Replay Engine
- Retries failed integrations
- Uses stored payloads

---

### 3.3 Database (PostgreSQL)

Stores:
- Logs
- Tokens
- Deduplication keys
- Audit records

---

## 4. Data Flow

### Step 1: Integration Trigger
- OIC receives event or scheduled trigger

### Step 2: Dedup Check
- OIC calls `/api/dedup-check`
- If duplicate → stop
- Else → continue

### Step 3: Processing
- Integration executes

### Step 4: Logging
- OIC sends logs to `/api/logs`

### Step 5: Failure Handling
- On error → payload stored
- Available for replay

---

## 5. Security Architecture

- HTTPS communication
- API authentication (API Key / JWT)
- Encrypted token storage
- Restricted access to endpoints

---

## 6. Scalability Design

- Stateless Django APIs
- Horizontal scaling possible
- Database indexing for performance
- Future: Redis + Celery for async processing

---

## 7. Future Architecture Enhancements

- Event streaming (Kafka)
- AI engine for failure prediction
- Multi-tenant SaaS architecture
- Microservices separation

---

## 8. Conclusion

OIC Guardian enhances OIC by introducing:
- Intelligence
- Control
- Reliability

Making enterprise integrations more robust and scalable.