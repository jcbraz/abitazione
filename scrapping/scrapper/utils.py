from typing import List

def build_url(
    regions: List[str], intentions: List[str], tipologies: List[str]
) -> List[str]:
    urls = []
    for region in regions:
        for intention in intentions:
            for tipology in tipologies:
                if tipology != "nuove-construzione":
                    url = f"https://www.immobiliare.it/{intention}-{tipology}/{region}/?criterio=rilevanza&pag=1"
                else:
                    url = f"https://www.immobiliare.it/{tipology}/{region}/?criterio=rilevanza&pag=1"
                urls.append(url)

    return urls