import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
import time

visited = set()
domain = ""

def is_internal(link):
    parsed_link = urlparse(link)
    return parsed_link.netloc == "" or parsed_link.netloc == domain

def crawl(url):
    if url in visited:
        return []

    visited.add(url)
    links = []

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for a_tag in soup.find_all("a", href=True):
            full_url = urljoin(url, a_tag['href'])
            parsed = urlparse(full_url)
            if parsed.scheme in ["http", "https"] and is_internal(full_url):
                if full_url not in visited:
                    links.append(full_url)
    except Exception as e:
        print(f"❌ Failed to crawl {url}: {e}")

    return links

def generate_sitemap(start_url):
    global domain
    parsed = urlparse(start_url)
    domain = parsed.netloc

    print(f"🔍 Crawling started at: {start_url}")
    urls_to_visit = [start_url]

    for url in urls_to_visit:
        new_links = crawl(url)
        urls_to_visit.extend([link for link in new_links if link not in visited])

    print(f"✅ Total pages found: {len(visited)}")
    return visited

def save_to_xml(urls):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_tag = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_tag, "loc")
        loc.text = url
        lastmod = ET.SubElement(url_tag, "lastmod")
        lastmod.text = time.strftime("%Y-%m-%d")

    tree = ET.ElementTree(urlset)
    with open("sitemap.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print("📄 Sitemap saved as sitemap.xml")

if __name__ == "__main__":
    start_url = input("Enter the full website URL (include https://): ").strip()
    found_urls = generate_sitemap(start_url)
    save_to_xml(found_urls)
