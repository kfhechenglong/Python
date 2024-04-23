import requests

cookies = {
    'acw_tc': '2760825e17124793313702847eb133fdc0bbf77cb3bdfc855dd5b83dca9e20',
    'xq_a_token': '4b8bc7136c9fd7b4395f9ca0a65c38363243df2b',
    'xqat': '4b8bc7136c9fd7b4395f9ca0a65c38363243df2b',
    'xq_r_token': '3f230866347670b258c76aecd81456e63e6aa98b',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNDk1NjQ2MiwiY3RtIjoxNzEyNDc5MjgzMjkwLCJjaWQiOiJkOWQwbjRBWnVwIn0.dslBZycPuPkXh-haiq5ZZZ6_v69ENOeJ1_7iS34scFKAT7ebw00CkAI8nihSUlZndF11fNmjKuHKKTpMrlVtb-gPCIoDxkBWBaEbCcwAY5IwlHSZPxhTmBvapfwawVH3Y1eJ9CCJtwHNzG_qhLUbCocYh4Q8t6azQ5-eow6oCurQkp5iZ6IDwc5WebF76_7gou6vWCp6g06lZtRdhag_kY0dZ2D8iR9YZW6gXWlGw3KjdnHhJWJ8D5EqSjTldGl5lkA7B4c0l4Gh1qSrtNVYU7pUIR4KryYs42y9POVhsYnHOz3lATH1yJuVTyG2cXFVgshjsX6p8jzsEgJV6LZlLQ',
    'cookiesu': '461712479331393',
    'u': '461712479331393',
    'device_id': '34bb8b5191938f9863b92cee34738f54',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1712479029',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1712479332',
    '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7': 'rRgR49nzn1iHxtZQn1gyudXDooAYNuHgszwgJPjKLgNVPzhzEknsw0amUJQv8tjLbNBCMEglAFqyyCepoRi5UQ%3D%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=2760825e17124793313702847eb133fdc0bbf77cb3bdfc855dd5b83dca9e20; xq_a_token=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; xqat=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; xq_r_token=3f230866347670b258c76aecd81456e63e6aa98b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNDk1NjQ2MiwiY3RtIjoxNzEyNDc5MjgzMjkwLCJjaWQiOiJkOWQwbjRBWnVwIn0.dslBZycPuPkXh-haiq5ZZZ6_v69ENOeJ1_7iS34scFKAT7ebw00CkAI8nihSUlZndF11fNmjKuHKKTpMrlVtb-gPCIoDxkBWBaEbCcwAY5IwlHSZPxhTmBvapfwawVH3Y1eJ9CCJtwHNzG_qhLUbCocYh4Q8t6azQ5-eow6oCurQkp5iZ6IDwc5WebF76_7gou6vWCp6g06lZtRdhag_kY0dZ2D8iR9YZW6gXWlGw3KjdnHhJWJ8D5EqSjTldGl5lkA7B4c0l4Gh1qSrtNVYU7pUIR4KryYs42y9POVhsYnHOz3lATH1yJuVTyG2cXFVgshjsX6p8jzsEgJV6LZlLQ; cookiesu=461712479331393; u=461712479331393; device_id=34bb8b5191938f9863b92cee34738f54; Hm_lvt_1db88642e346389874251b5a1eded6e3=1712479029; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1712479332; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=rRgR49nzn1iHxtZQn1gyudXDooAYNuHgszwgJPjKLgNVPzhzEknsw0amUJQv8tjLbNBCMEglAFqyyCepoRi5UQ%3D%3D',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://xueqiu.com/today', cookies=cookies, headers=headers).text
print(response)

with open('./11.html', 'w', encoding='utf-8') as f:
  f.write(response)