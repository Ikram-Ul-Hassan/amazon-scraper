<!--
████████████████████████████████████████████████████████████████████
README.md for Amazon Scraper Project
Author: Ikram Ul Hassan
Experience: 3+ Years Python & Web Scraping
Date: 2025-09-01
-->

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Beta-yellow?style=for-the-badge"/>
</p>

---

# <p align="center" style="background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; color: transparent;">🛒 Amazon Scraper</p>

<p align="center">
High-performance Python scraper for Amazon products with automated pagination and detailed data extraction.
</p>

---

## 👤 Author
### **Name:** Ikram Ul Hasan
- **Experience:** Python, SQL, ML, Web Scraping & Automation  
- **GitHub:** [github.com/Ikram-Ul-Hassan](https://github.com/Ikram-Ul-Hassan)   
- **LinkedIn:** [linkedin.com/in/Ikram-Ul-Hassan](https://linkedin.com/in/Ikram-Ul-Hassan)
- **Kaggle:** [kaggle.com/ikramshah512](https://www.kaggle.com/ikramshah512)
- **Email:** shahikram295@gmail.com 

---

## 📌 Project Overview
**Amazon Scraper** is a high-performance Python tool designed to automatically scrape thousands of products from Amazon, including detailed product information, prices, ratings, reviews, and more. It supports **pagination**, handles **dynamic headers** for anti-bot detection, and exports data into CSV format for seamless analysis.  

This project is ideal for **data analysts, e-commerce researchers, and developers** who want structured Amazon product data for research, analytics, or pricing insights.  

---

## ✨ Key Features
- 🔹 Scrapes **title, rating, reviews, current price, variant prices, listed price**  
- 🔹 Retrieves **best seller, sponsored, coupon, buy box, shipping, sustainability badges**  
- 🔹 Supports **thousands of products via automated pagination**  
- 🔹 Handles **dynamic User-Agent headers** for bot avoidance  
- 🔹 Automatic **retry & error handling** for robust scraping  
- 🔹 Saves results to **CSV** using Pandas  
- 🔹 Human-like delays to **mimic real browsing behavior**  

---

## 🛠 Technology Stack
- **Python 3.x**  
- **Requests** – HTTP requests  
- **BeautifulSoup** – HTML parsing  
- **Pandas & NumPy** – Data handling  
- **Datetime** – Timestamping data  

---

## ⚙️ Installation
```bash
# Clone the repo
git clone https://github.com/yourusername/amazon-scraper.git
cd amazon-scraper

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage
1. Set the starting page in app.py if resuming scraping.
2. Run the scraper:

```
python app.py
```
## Sample Data Collected

| Title           | Rating | Reviews | Current Price | Listed Price | Best Seller | Sponsored | Coupon    | Category    | Product URL                                   |
| --------------- | ------ | ------- | ------------- | ------------ | ----------- | --------- | --------- | ---------   | --------------------------------------------- |
| Example Product | 4.5    | 120     | \$29.99       | \$39.99      | Yes         | Organic   | No Coupon | Laptop      | [https://amazon.com/](https://amazon.com/)... |


## 📂 Kaggle Dataset & Notebook

I have published the scraped dataset and a data cleaning + feature engineering notebook on Kaggle for open access:

📊 Dataset: [Amazon Products Sales Dataset 42K+ Items - 2025](https://www.kaggle.com/datasets/ikramshah512/amazon-products-sales-dataset-42k-items-2025)

(42,000+ Amazon products with detailed attributes for analysis and ML projects)

📓 Notebook:[ Amazon Products Data Cleaning & Feature Engineering](https://www.kaggle.com/code/ikramshah512/amazon-products-data-cleaning-feature-engineering)

(Step-by-step cleaning, handling missing values, feature engineering for price analysis and recommendations)


## 🧩 How it Works

1. app.py sends HTTP requests to Amazon search pages using randomized headers.

2. HTML content is passed to scraper.py which parses all product containers.

3. Each product's title, price, ratings, reviews, badges, URLs, shipping info, and more are extracted.

4. Data is aggregated into a list and exported to CSV for analysis.

5. Automatic pagination ensures scraping of thousands of products.

## ⚠️ Notes & Best Practices

- Avoid scraping too frequently; use human-like delays (time.sleep) to reduce risk of blocking.

- Amazon may change HTML structure, so selectors in scraper.py may need updates over time.

- This scraper is for educational and research purposes. Always comply with Amazon's terms of service.

## 🤝 Contributing

- Contributions are welcome!

- Fork the repository

- Create a branch (feature/xyz)

- Submit a pull request with a clear description

## 📝 License

This project is licensed under the MIT License.
---
Made with ❤️ by **Ikram Ul Hassan** | Python Web Scraping Specialist & Data Analyst

