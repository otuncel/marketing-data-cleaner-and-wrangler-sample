# CRM Ready Marketing Data Cleaner & Wrangler

A production-ready Python data pipeline designed to clean, standardize, and deduplicate messy marketing lead datasets. This project demonstrates intermediate-to-advanced data wrangling techniques using Pandas and NumPy, transforming raw, high-variance human-input data into high-integrity structured profiles ready for CRM integration.

## 📌 Business Case & Problem Statement

Marketing campaigns often capture high volumes of customer data, but manual user input leads to structural corruption (broken casing, duplicate registrations, missing contact info, inconsistent phone formats). 

This script automates the end-to-end data cleansing process for a marketing agency dataset, addressing the following production bottlenecks:
- **Data Deduplication:** Identifying and removing duplicate sign-ups based on unique identifier keys (Email), while preserving the latest timeline state.
- **Missing Value Strategy:** Dropping dead/uncontactable records while systematically tagging partial profiles for verification pipelines.
- **String Normalization:** Eliminating leading/trailing whitespaces and enforcing standard text layout constraints.
- **Regex Phone Standardization:** Stripping structural noise (dashes, spaces, symbols) to unify telecommunication values.

## 🛠️ Tech Stack & Methods

- **Language:** Python 3.10+
- **Core Library:** Pandas & NumPy (Vectorized data operations)
- **Techniques Used:** Row-wise data lambda mapping, subset conditional drop mechanisms, regex filtering, and structural indexing resets.

## 🚀 Getting Started

### Installation & Execution
1. Clone the repository and install the dependencies:
   ```bash
   git clone [https://github.com/](https://github.com/)[Your-GitHub-Username]/marketing-data-cleaner-and-wrangler-sample.git
   cd marketing-data-cleaner-and-wrangler-sample
   pip install -r requirements.txt
2. Run the cleaning script:
```bash
   python sample_data_cleaner.py
