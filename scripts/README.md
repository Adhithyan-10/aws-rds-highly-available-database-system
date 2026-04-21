# 🧪 Scripts — EC2 to RDS Interaction

This folder contains Python scripts used to validate connectivity between the EC2 instance and the Amazon RDS database.

---

## 📌 Purpose

These scripts demonstrate real interaction with the database, proving that the application layer can successfully communicate with the database layer.

---

## 📄 Scripts Overview

### create_table.py
- Establishes connection to the RDS MySQL instance  
- Creates a table in the database  

---

### show_tables.py
- Connects to the database  
- Retrieves and displays existing tables  

---

## 🔁 Workflow

1. EC2 instance connects to RDS using endpoint  
2. Python script establishes MySQL connection  
3. Database operations are executed  
4. Output is verified through terminal  

---

## ⚠️ Note

Database credentials are hardcoded for demonstration purposes.  
In production environments, credentials should be managed using:
- Environment variables  
- AWS Secrets Manager  

---

## 💡 Key Insight

Successful execution of these scripts confirms that:
- Network configuration is correct  
- Security groups are properly configured  
- Database is accessible only through intended sources  

---

## 🚀 Summary

These scripts provide practical validation of the system by demonstrating real database operations from the application layer.
