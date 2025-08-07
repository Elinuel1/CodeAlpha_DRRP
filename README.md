# Data Redundancy Removal System (DRRS) 🧹🔐

This project detects and prevents redundant or duplicate data entries using AWS DynamoDB and Python, ensuring data integrity, reducing cost, and reducing storage overhead. This is my second CodeAlpha projecct in line with my internship journey with them.

---

## 🔍 Problem Statement

Redundant data wastes storag, and it can lead to misleading analysis and undue cost. This system identifies:

- ✅ Unique entries
- ❌ Exact duplicates
- ⚠️ Near-duplicates (e.g. minor spelling changes)

---

## 💡 Key Features

- **AWS DynamoDB** for storing unique entries with deduplication via hashing
- **Python** application for validation and intelligent detection
- **Levenshtein distance** for near-duplicate detection
- **Double-layered security** using:
  - Hash-based matching
  - Similarity scoring for fuzzy matches
- **Terraform Infrastructure as Code** 
- **Unit testing** with `unittest` and mocked AWS using `moto`

---

## 🛠️ Technologies Used

- **Language:** Python
- **Cloud:** AWS DynamoDB
- **Infrastructure as Code (IaC):** Terraform
- **VS Code**
- **Git & GitHub**
- **DynamoDB** (NoSQL)
- **WSL Ubuntu**
- **Testing:** `unittest`, `moto`
- **Hashing:** SHA-256
- **Similarity Detection:** `Levenshtein` distance (via `python-Levenshtein`)

---

## 🚀 Setup & Usage

### 1. Clone the repo

```bash
git clone https://github.com/your-username/CodeAlpha_DRRP.git
cd CodeAlpha_DRRP
