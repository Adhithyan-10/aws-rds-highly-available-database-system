# 🗄️ Database Layer — Highly Available RDS Implementation

This module demonstrates the implementation of a **highly available database system on AWS** using Amazon RDS MySQL with Multi-AZ deployment and secure EC2 connectivity.

---

## 🔁 System Overview

The application running on EC2 connects to the database using the RDS endpoint:

EC2 Instance → RDS Endpoint → Primary DB → Standby DB

---

## ⚙️ RDS Configuration

- Engine: MySQL  
- Deployment Type: Multi-AZ Enabled  
- Public Access: Disabled  
- DB Subnet Group: Configured across multiple Availability Zones  

---

## 🔁 High Availability Design

- A **Primary database instance** handles all read/write operations  
- A **Standby instance** is maintained in a different Availability Zone  
- Data is **synchronously replicated** from Primary → Standby  

---

## 🔁 Failover Mechanism

- If the primary instance fails:
  - Standby is automatically promoted to Primary  
  - The application reconnects using the **same RDS endpoint**  

💡 This ensures **minimal downtime and zero manual intervention**

---

## 🔐 Security Configuration

### EC2 Security Group
- Outbound:
  - Port 3306 (MySQL) → RDS Security Group  

---

### RDS Security Group
- Inbound:
  - Port 3306 (MySQL) from EC2 Security Group  
- All other traffic is denied  

---

## 🌐 Networking

- RDS is deployed within the VPC  
- Database is **not publicly accessible**  
- Communication between EC2 and RDS happens via **VPC internal networking**  

---

## 🧪 Implementation (Proof of Work)

The database connectivity and operations were validated using Python scripts:

- `create_table.py` → Establishes connection and creates table  
- `show_tables.py` → Retrieves and verifies database tables  

---

## 📸 Implementation Proof

All implementation screenshots (RDS setup, security groups, Multi-AZ, connectivity, and outputs) are available in the `screenshots/` folder.

---

## ⚠️ Note

Credentials are hardcoded in scripts for demonstration purposes.  
In production systems, use:
- Environment Variables  
- AWS Secrets Manager  

---

## 💡 Key Insight

A database should never be a single point of failure in a production system.  
Multi-AZ deployment ensures high availability and automatic recovery.

---

## 🚀 Summary

This module demonstrates how to design a **secure, highly available, and fault-tolerant database system** on AWS by integrating EC2 with RDS Multi-AZ deployment.
