# 🌐 Sitemap Generator

A Python CLI tool that automatically generates an `sitemap.xml` file for any website by crawling its internal pages.

---

## ✅ Features

- Crawls a website and finds all internal links.
- Automatically generates a valid XML sitemap.
- Supports basic SEO structure for search engine crawling.
- Saves the sitemap as `sitemap.xml` in your directory.

---

## 🛠️ Tech Stack

- `requests` – for sending HTTP requests
- `BeautifulSoup` – for parsing HTML
- `xml.etree.ElementTree` – for building the XML sitemap

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
https://github.com/Aditi-Rani/sitemap-generator
```
```bash
cd sitemap-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Script
```bash
python sitemap_generator.py
```
