import requests


class Jokes():

    def __init__(self):
        self.good_jokes = 0
        self.bad_jokes = 0
        self.cod = 0

    def site(self):
        with open('jokes.txt', 'w') as f:
            for i in range(1, 20):
                res = requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')
                joke = res.text
                f.write(f'{joke}\n')

    def count_jokes(self):
        with open('jokes.txt', 'r') as f:
            for line in f:
                if 'это' in line or len(line) >= 60:
                    with open('saved_jokes.txt', 'w') as saves:
                        saves.write(f'{line}\n')
                    self.good_jokes += 1
                else:
                    self.bad_jokes +=1
                # elif len(line) < 60:
                #     self.bad_jokes += 1


    def counting(self):
        print(f'Количество запросов: {self.good_jokes + self.bad_jokes + self.cod}')
        print(f'Количество сохраненных шуток: {self.good_jokes}')
        print(f'Количество удачных шуток: {self.good_jokes}')
        print(f'Количество неудачных шуток: {self.bad_jokes}')


jokes = Jokes()

jokes.site()
jokes.count_jokes()
jokes.counting()
