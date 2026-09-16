** Customer Support Ticket Intelligence **
* SQL Analysis Queries *
  
-- 1. Total number of support tickets
SELECT COUNT(*) AS total_tickets
FROM tickets;


-- 2. Average resolution time
SELECT
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM tickets;


-- 3. SLA breach rate
SELECT
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END) AS breached_tickets,
    ROUND(
        100.0 * SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate
FROM tickets;


-- 4. Escalation rate
SELECT
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN escalated = TRUE THEN 1 ELSE 0 END) AS escalated_tickets,
    ROUND(
        100.0 * SUM(CASE WHEN escalated = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM tickets;


-- 5. Ticket volume by issue type
SELECT
    issue_type,
    COUNT(*) AS ticket_count
FROM tickets
GROUP BY issue_type
ORDER BY ticket_count DESC;


-- 6. SLA performance by issue type
SELECT
    issue_type,
    COUNT(*) AS total_tickets,
    ROUND(
        100.0 * SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate
FROM tickets
GROUP BY issue_type
ORDER BY sla_breach_rate DESC;


-- 7. Escalation rate by issue type
SELECT
    issue_type,
    COUNT(*) AS total_tickets,
    ROUND(
        100.0 * SUM(CASE WHEN escalated = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM tickets
GROUP BY issue_type
ORDER BY escalation_rate DESC;


-- 8. Performance by customer segment
SELECT
    c.customer_segment,
    COUNT(t.ticket_id) AS ticket_count,
    ROUND(AVG(t.resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(AVG(t.satisfaction_score), 2) AS avg_satisfaction,
    ROUND(
        100.0 * SUM(CASE WHEN t.sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate,
    ROUND(
        100.0 * SUM(CASE WHEN t.escalated = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM tickets t
JOIN customers c
    ON t.customer_id = c.customer_id
GROUP BY c.customer_segment
ORDER BY ticket_count DESC;


-- 9. Performance by support channel
SELECT
    channel,
    COUNT(*) AS ticket_count,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction,
    ROUND(
        100.0 * SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate,
    ROUND(
        100.0 * SUM(CASE WHEN escalated = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM tickets
GROUP BY channel
ORDER BY sla_breach_rate DESC;


-- 10. Resolution time buckets
SELECT
    CASE
        WHEN resolution_time_hours <= 12 THEN '0-12 hours'
        WHEN resolution_time_hours <= 24 THEN '13-24 hours'
        WHEN resolution_time_hours <= 48 THEN '25-48 hours'
        ELSE '49+ hours'
    END AS resolution_bucket,
    COUNT(*) AS ticket_count,
    ROUND(
        100.0 * SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate,
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM tickets
GROUP BY resolution_bucket
ORDER BY
    CASE resolution_bucket
        WHEN '0-12 hours' THEN 1
        WHEN '13-24 hours' THEN 2
        WHEN '25-48 hours' THEN 3
        WHEN '49+ hours' THEN 4
    END;


-- 11. Overall customer satisfaction
SELECT
    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM tickets;


-- 12. Top critical issue areas
SELECT
    issue_type,
    COUNT(*) AS ticket_count,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(
        100.0 * SUM(CASE WHEN sla_breached = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS sla_breach_rate,
    ROUND(
        100.0 * SUM(CASE WHEN escalated = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM tickets
GROUP BY issue_type
ORDER BY escalation_rate DESC, sla_breach_rate DESC;
