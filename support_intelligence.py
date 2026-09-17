
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

#Customer IDs

customer_ids = []

for i in range(1, 10001):
    customer_id = f"CUST{i:05d}"
    customer_ids.append(customer_id)

#Customer Segment

segments = np.random.choice(['Standard','Premium','Enterprise'], size=10000, p=[0.65, 0.30, 0.05])

#Country

countries = np.random.choice(['United States', 'India', 'Canada', 'United Kingdom', 'Australia'], size=10000, p=[0.55, 0.20, 0.10, 0.10, 0.05])

#Preferred Support Channels

preferred_channels = np.random.choice(['Chat', 'Email', 'Phone', 'Web'], size=10000, p=[0.35, 0.30, 0.20, 0.15])

#Customer signup dates

end_date = datetime.today()
start_date= end_date - timedelta(days=3*365)

#generate 10,000 random signup dates
signup_dates = pd.to_datetime(
    np.random.randint(start_date.timestamp(),end_date.timestamp(),size = 10000),unit='s')

#Inspect Customer Data
print(customer_ids[:5])
print(len(customer_ids))
print(pd.Series(segments).value_counts())
print(pd.Series(countries).value_counts())
print(pd.Series(preferred_channels).value_counts())
print(pd.Series(signup_dates).value_counts())

#Create Dataframe
customers = pd.DataFrame({
    "customer_id": customer_ids,
    "customer_segment": segments,
    "country": countries,
    "preferred_support_channel": preferred_channels,
    "signup_date": signup_dates
})

#Inspect data
print("\nCustomer DataFrame:")
print(customers.head())

print("\nDataset shape:")
print(customers.shape)

print("\nDataset info:")
print(customers.info())

print("\nDataset null values:")
print(customers.isnull().sum())

print("\nDataset data types:")
print(customers.dtypes)

#Support tickets
num_tickets = 50000

ticket_ids = [ ]

for i in range(1, num_tickets + 1):
    ticket_id = f"TICKET{i:05d}"
    ticket_ids.append(ticket_id)

#assign customers to tickets
ticket_customer_ids = np.random.choice(
    customer_ids, size = num_tickets
)

#validate customer IDs
valid_customer_ids = set(customer_ids)

#Ticket Issue Types
issue_types = np.random.choice(
    ['Payment Issue',
     'Account Access',
     'Technical Problem',
     'Order/Service Issue',
     'Refund Request',
     'Delivery Delay'
    ], size=num_tickets,
    p=[0.20, 0.15, 0.25, 0.20, 0.10, 0.10]
)

#Ticket priorities
ticket_priorities = np.random.choice(
    ['Low', 'Medium', 'High', 'Critical'], size=num_tickets, p=[0.40, 0.35, 0.20, 0.05]
)

#Support Channels
support_channels = np.random.choice(
    ['Chat', 'Email', 'Phone', 'Web'], size=num_tickets, p=[0.35, 0.30, 0.20, 0.15]
)

#Ticket creation dates
ticket_creation_dates = pd.to_datetime(
    np.random.randint(start_date.timestamp(), end_date.timestamp(), size=num_tickets), unit='s'
)

#Ticket Statuses
ticket_status = np.random.choice(
    ["Resolved", "Open", "In Progress", "Pending", "Closed"], size=num_tickets, p=[0.50, 0.20, 0.15, 0.10, 0.05]
)

#Resolution Dates
resolution_dates = pd.to_datetime(
    np.random.randint(start_date.timestamp(), end_date.timestamp(), size=num_tickets), unit='s'
)

#Calculate Resolution Time
resolution_time_hours = []

for created,resolved in zip(ticket_creation_dates, resolution_dates):
    if pd.notna(resolved):
        resolution_time = (resolved - created).total_seconds() / 3600
        resolution_time_hours.append(resolution_time)
    else:
        resolution_time_hours.append(np.nan)

#Create SLA target based on priority
sla_target_hours = [ ]

for priority in ticket_priorities:
    if priority == "Critical":
        sla_target_hours.append(4)
    elif priority == "High":
        sla_target_hours.append(12)
    elif priority == "Medium":
        sla_target_hours.append(24)
    else:
        sla_target_hours.append(48)

#SLA Breach
sla_breached = [ ]

for resolution_time,sla_target in zip(resolution_time_hours, sla_target_hours):

    if pd.isna(resolution_time):
        sla_breached .append(False)

    elif resolution_time > sla_target:
        sla_breached.append(True)

    else:
        sla_breached.append(False)

#Ticket Escalation

ticket_escalated = [ ]

for priority,issue in zip(ticket_priorities, issue_types):
    if priority == "Critical" and issue =="Technical Problem":
        probability = 0.50

    elif priority == "Critical":
        probability = 0.35

    elif priority =="High" and issue =="Technical Problem":
        probability = 0.35

    elif priority =="High":
        probability = 0.20

    elif priority == "Technical Problem":
        probability = 0.20

    else:
        probability = 0.08

    ticket_escalated.append(np.random.random() < probability)

#Customer Satisfaction Score

satisfaction_scores = [ ]

for resolution_time, breached, escalated_flag in zip(
    resolution_time_hours,
    sla_breached,
    ticket_escalated
):

    if breached:
        score = np.random.randint(1,3)
    elif escalated_flag:
        score = np.random.randint(2,5)
    elif resolution_time < 12:
        score = np.random.randint(4,6)
    else:
        score = np.random.randint(3,6)

    satisfaction_scores.append(score)

#inspect ticket data
print("\nFirst 5 ticket IDs:")
print(ticket_ids[:5])

print("\nTotal number of tickets:")
print(len(ticket_ids))

print("\nFirst 5 ticket customer IDs:")
print(ticket_customer_ids[:5])

print("\nIssue type distribution:")
print(pd.Series(issue_types).value_counts())

print("\nTicket priority distribution:")
print(pd.Series(ticket_priorities).value_counts())

print("\nSupport channel distribution:")
print(pd.Series(support_channels).value_counts())

print("\nTicket creation date distribution:")
print(pd.Series(ticket_creation_dates).value_counts())

print("\nTicket status distribution:")
print(pd.Series(ticket_status).value_counts())

print("\nResolution time distribution:")
print(pd.Series(resolution_time_hours).value_counts())

print("\nSLA target distribution:")
print(pd.Series(sla_target_hours).value_counts())

print("\nSLA breach distribution:")
print(pd.Series(sla_breached).value_counts())  

print("\nTicket escalation distribution:")
print(pd.Series(ticket_escalated).value_counts())   

print("\nCustomer satisfaction score distribution:")
print(pd.Series(satisfaction_scores).value_counts())

#Inspect Final Ticket DataFrame
# ============================================
# FINAL TICKETS DATAFRAME
# ============================================

tickets = pd.DataFrame({
    "ticket_id": ticket_ids,
    "customer_id": ticket_customer_ids,
    "issue_type": issue_types,
    "priority": ticket_priorities,
    "support_channel": support_channels,
    "created_at": ticket_creation_dates,
    "ticket_status": ticket_status,
    "resolved_at": resolution_dates,
    "resolution_time_hours": resolution_time_hours,
    "sla_target_hours": sla_target_hours,
    "sla_breached": sla_breached,
    "escalated": ticket_escalated,
    "satisfaction_score": satisfaction_scores
})

#Validate Final Tickets DataFrame

print("\n*****FINAL DATA VALIDATION*****")

#Check Duplicate ticket IDs
print("\nDuplicate Ticket IDs:")
print(tickets['ticket_id'].duplicated().sum())

#Check duplicate rows
print("\nDuplicate Rows:")
print(tickets.duplicated().sum())

#Check missing values
print("\nMissing Values:")
print(tickets.isnull().sum())

#Check ticket status distribution
print("\nTicket Status Distribution:")
print(tickets['ticket_status'].value_counts())

#Check priority distribution
print("\nTicket Priority Distribution:")
print(tickets['priority'].value_counts())

#Check SLA breach rate
print("\nSLA Breach Rate:")
print(tickets['sla_breached'].mean())

#Check escalation rate
print("\nTicket Escalation Rate:")
print(tickets['escalated'].mean())

#Check average resolution time
print("\nAverage Resolution Time (hours):")
print(tickets['resolution_time_hours'].mean())  

#Check average satisfaction score
print("\nAverage Satisfaction Score:")
print(tickets['satisfaction_score'].mean())

#Inspect the Tickets dataframe

print("\nFinal Tickets DataFrame:")
print(tickets.head())

print("\nFinal Tickets Shape:")
print(tickets.shape)

print("\nFinal Tickets Info:")
tickets.info()

print("\nFinal Tickets Null Values:")
print(tickets.isnull().sum())

customers.to_csv("customers.csv", index=False)

tickets.to_csv("tickets.csv", index=False)

print("CSV files created successfully.")