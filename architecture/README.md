# 🏗️ Architecture Overview

This project demonstrates a **Highly Available Database System on AWS** using Amazon RDS Multi-AZ deployment with secure EC2 integration.

---

## 🖼️ Architecture Diagram

![Architecture](ARCH_main.png)

---

## 🔁 System Flow

EC2 Instance → RDS Endpoint → Primary DB → Standby DB

---

## 🧩 Components

### 🟢 Application Layer
- EC2 instance hosted in a **public subnet**
- Acts as the application server
- Connects to the database using MySQL (Port 3306)

---

### 🔵 Database Layer (RDS Multi-AZ)
- Amazon RDS MySQL deployed across **multiple Availability Zones**
- Consists of:
  - **Primary Instance** → Handles all database operations  
  - **Standby Instance** → Maintains synchronous replica  

---

### 🌐 DB Subnet Group
- Configured across multiple AZs:
  - Public Subnet (AZ1)  
  - Private Subnet (AZ2)  
- Enables high availability and failover capability  

---

## 🔁 High Availability & Failover

- Data is **synchronously replicated** from Primary → Standby  
- In case of failure:
  - Standby is automatically promoted to Primary  
  - Application reconnects using the **same RDS endpoint**  

💡 This ensures **zero manual intervention and minimal downtime**

---

## 🔐 Security Design

### EC2 Security Group
- Allows outbound:
  - Port 3306 (MySQL) → RDS Security Group  

---

### RDS Security Group
- Allows inbound:
  - Port 3306 (MySQL) from EC2 Security Group  
- All other traffic is denied  

---

## 🔗 Connectivity

- EC2 connects to RDS using the **RDS Endpoint**
- Communication happens via **VPC internal networking**
- Database is **not publicly accessible**

---

## 💡 Key Insights

- Multi-AZ deployment eliminates **single point of failure**
- Security groups enforce **controlled access**
- RDS endpoint ensures **seamless failover handling**

---

## 🚀 Summary

This architecture demonstrates how to design a **secure, fault-tolerant, and highly available database system** on AWS by combining EC2 application logic with RDS Multi-AZ deployment.
