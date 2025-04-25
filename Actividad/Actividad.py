import re
from collections import Counter


with open('Actividad/access (1).log', 'r', encoding='utf-8') as file:
    log_data = file.read()

# Expresión regular
browser_regex = re.compile(
    r"(Chrome|Firefox|Safari|Opera|Edg|MSIE|Trident|Brave|Vivaldi|SamsungBrowser)[/\s]?\d*\.?\d*",
    re.IGNORECASE
)


browsers_found = browser_regex.findall(log_data)


normalized_browsers = [b.capitalize() for b in browsers_found]


browser_counts = Counter(normalized_browsers)

#  resultados
print("Frecuencia de uso por navegador:")
for browser, count in browser_counts.most_common():
    print(f"{browser}: {count} veces")
