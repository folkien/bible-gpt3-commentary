import requests
from bs4 import BeautifulSoup
import openai

def get_bible_reading():
    url = "https://deon.pl/czytania"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    readings_div = soup.find("div", class_="readings-module")
    return readings_div.text.strip()

def get_gpt4_commentary(text):
    openai.api_key = "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"
    prompt = (f"{text}\n\nKomentarz do czytania:\n\n"
              "3 najważniejsze myśli z czytania:\n\n"
              "Cytat świętego Kościoła Katolickiego:\n\n"
              "Najważniejsza myśl czytania:")
    response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200, n=1, stop=None, temperature=0.7)
    return response.choices[0].text.strip()


def post_to_facebook(comment, image_url):
    import facebook
    fb_access_token = "your_facebook_access_token"
    page_id = "your_facebook_page_id"
    graph = facebook.GraphAPI(access_token=fb_access_token, version="3.0")
    attachment = {
        "message": comment,
        "link": image_url,
    }
    graph.put_wall_post("", attachment=attachment, profile_id=page_id)

def main():
    bible_reading = get_bible_reading()
    print(bible_reading)
    gpt4_comment = get_gpt4_commentary(bible_reading)
    print(gpt4_comment)
    #post_to_facebook(gpt4_comment, dalle2_image_url)

if __name__ == "__main__":
    main()
