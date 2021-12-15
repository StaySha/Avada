import json
import requests


class Jokes(object):
    def __init__(self):
        self.good_jokes = 0
        self.bad_jokes = 0
        self.gets = 0
        self.jokes = []

    def site(self):
        for i in range(1, 11):
            res = requests.get(
                "https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php"
            )
            joke = res.text
            if len(joke) >= 60:
                self.jokes.append(joke)
                if "код" in joke.lower():
                    self.good_jokes += 1
                else:
                    self.bad_jokes += 1
            else:
                self.bad_jokes += 1
            self.gets += 1

        the_list = []
        i = 0
        for j in self.jokes:
            i += 1
            the_list.append({f"joke_{i}": j})

        print_out = [
            {"data": the_list},
            {"Количество запросов": self.gets},
            {"Количетсво сохраненных шуток": len(self.jokes)},
            {"Количество неудачных шуток": self.bad_jokes},
            {"количество удачных шуток": self.good_jokes},
        ]

        with open("jokes.json", "w") as file:
            json.dump(print_out, file, indent=2, ensure_ascii=False)


jokes = Jokes()
jokes.site()
