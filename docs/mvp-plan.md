# MVP Plan — OIC Guardian 🚀

## 1. Objective

Build a **Minimum Viable Product (MVP)** that demonstrates core value:

- Prevent duplicate processing
- Capture and store integration logs
- Enable replay of failed integrations
- Manage token lifecycle

---

## 2. MVP Scope

### Included Features:

1. **Deduplication Engine**
   - Prevent duplicate message processing
   - Unique message ID tracking

2. **Logging System**
   - Store request/response payloads
   - Capture integration status (success/failure)

3. **Replay Mechanism**
   - Retry failed integrations using stored payloads

4. **Token Management**
   - Store and refresh OAuth tokens

---

### Excluded (Future Phases):

- AI-based failure prediction
- Advanced dashboard UI
- Multi-tenant SaaS architecture
- Event streaming (Kafka)

---

## 3. Architecture (MVP)
Oracle HCM → OIC → OIC Guardian (Django API) → PostgreSQL


---

## 4. Tech Stack

### Backend:
- Django
- Django REST Framework

### Database:
- PostgreSQL

### Integration:
- OIC REST APIs

### Tools:
- Postman (testing)
- GitHub (version control)

---

## 5. Database Design

### Core Tables:
- Connection
- Token
- Log
- DedupKey
- Audit

---

## 6. API Endpoints (MVP)

| Endpoint | Method | Purpose |
|---------|--------|--------|
| /api/dedup-check | POST | Prevent duplicate processing |
| /api/logs | POST | Store logs |
| /api/logs | GET | Fetch logs |
| /api/tokens/refresh | POST | Refresh tokens |
| /api/replay/{id} | POST | Replay failed integration |

---

## 7. Development Timeline

### Week 1:
- Project setup
- Database schema
- Basic APIs

### Week 2:
- Deduplication logic
- Logging system

### Week 3:
- Replay feature
- Token management

### Week 4:
- Integration with OIC
- Testing and debugging

---

## 8. Success Criteria

MVP is successful if:

- Deduplication prevents duplicate entries
- Logs are captured correctly
- Failed integrations can be replayed
- Token refresh works without manual intervention

---

## 9. Risks & Mitigation

| Risk | Mitigation |
|-----|-----------|
| OIC API limitations | Use wrapper logic |
| Token refresh failure | Retry mechanism |
| Data inconsistency | Dedup validation |
| Performance issues | Optimize DB queries |

---

## 10. Deployment Plan

- Local development → Testing
- Deploy backend to cloud (AWS / OCI)
- Connect with OIC instance
- Run test integrations

---

## 11. Future Enhancements

- Real-time alerts (Slack/Email)
- Dashboard UI (React)
- AI failure detection
- Multi-client support

---

## 12. Conclusion

The MVP focuses on delivering **immediate value** by solving critical OIC limitations while laying the foundation for a scalable SaaS product.