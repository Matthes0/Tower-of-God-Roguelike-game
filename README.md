# Tower of God - roguelike game

# Ogólny zarys fabularny

Gra jest oczywiście klasycznym roguelikiem. Cel gry polega na wejściu na szczyt tytułowej wieży, co pozwoli spełnić dowolne życzenie postaci gracza. Nie można zrobić jednak tego na samym początku gry, ponieważ aby do niej wejść należy zebrać fragmenty klucza z co najmniej 3 innych wież.

# Start gry

gracz na starcie wybiera jedynie rasę. 

Gra zaczyna się bez jakiegokolwiek ekwipunku w holu, w którym od sklepikarzy można kupić wyposażenie. Asortyment sklepów aktualizuje się wraz z przechodzeniem kolejnych lokacji. Początkowo można wejść tylko do jednej lokacji, reszta pozostaje niedostępna.

# Rasy
Rasa określa dodatkowe umiejętności gracza (aktywne/pasywne, negatywne/pozytywne) oraz startową walutę (Punkty Wieży). Im rasa ma lepsze bonusy startowe, tym mniej waluty na wyposażenie dostanie na start gry. Ma to w pewien sposób balansować rozgrywkę - niektóre rasy początek gry będą miały ułatwiony poprzez dostęp do dobrego ekwipunku, a niektóre poprzez bonusy za pośrednictwem umiejętności rasowych. 
Na początku chciałbym skupić się na 3 rasach, wraz z rozwojem gry i nowymi pomysłami prawdopodobnie pojawi się ich więcej:
- człowiek - sporo złota, przeciętne statystyki, bonus rasowy to lekko zwiększone zdobywanie doświadczenia
- olbrzym - mało złota, zaczyna z o wiele lepszymi statystykami od człowieka, nie może nosić broni jednoręcznych, bronie dwuręczne klasyfikowane są jako bronie jednoręczne, ograniczony dostęp do zakładania ekwipunku - większość rzeczy przystosowana jest pod normalny rozmiar, więc konieczne jest szukanie olbrzymich wersji wyposażenia.
- pradawny - mało złota, co 3 poziomy dostaje wybór 1 losowego zaklęcia z 3 podanych, które są mocniejszymi wersjami tych zaklęć, ale nie może uczyć się zaklęć normalnie. Wybiera też 2 zaklęcia na samym początku gry.

# Poruszanie się, czas

Poruszanie w 8 kierunkach na touchpadzie. Co do poruszania się diagonalnie - wydaje mi się że najlepszym rozwiązaniem jest liczenie czasu potrzebnego na przejście pola jako 1,41 zamiast 1. 

Wszystkie akcje zajmują jakiś okres czasu - szybsze bronie atakują w mniej jednostek czasu niż wolniejsze. Obciążenie wyposażenia będzie wpływać w jakimś stopniu na to, jak szybko wykonywane są akcje gracza (ktoś w zbroi płytowej będzie chodzić wolniej niż ktoś w skórzanym wyposażeniu). 

Potwory spotykane przez gracza nie zawsze poruszają się z taką samą prędkością jak gracz. Mogą być lekko szybsze lub wolniejsze (co x ruchów przechodziłyby np. 2 pola zamiast 1)

chciałbym zaimplementować również algorytm autoodkrywania mapy i algorytm atakowania celu najbliżej postaci.

# Walka

Podział na walkę wręcz, walkę dystansową i magię.

##### Walka wręcz

Atakowanie przeciwników poprzez "wchodzenie" w przeciwnika. Spora różnorodność typów broni, w planach każda broń (poza atakami bez broni) będzie miała 3 "tiery" wymagające lepszych statystyk do ich efektywnego noszenia. Przykładowe typy broni planowane na ten moment:

- miecze jednoręczne, umiarkowana szybkość i obrażenia, możliwość dual wieldingu/noszenia tarczy.
- sztylety, wysoka szybkość, niskie obrażenia, bonus do ciosów krytycznych
- kosy, niska szybkość, wysokie obrażenia, ataki trafiają więcej niż 1 przeciwnika na raz (atak przeciwników wokół postaci bohatera)
- ataki bez użycia broni, umiarkowana szybkość i bez dodatkowych bonusów niskie obrażenia
- młoty dwuręczne, niska szybkość, wysokie obrażenia, możliwe do pewnego stopnia niszczenie terenu - nie umożliwiające wyjście poza mapę, ale pozwalające dostosowywać teren do walki z przeciwnikami
- miecze dwuręczne, niska szybkość, wysokie obrażenia, okazjonalnie przeciwnik zostaje zjawiskowo pokonany (z dodatkowym opisem jako komunikat), co powoduje że inni przeciwnicy w okolicy zostają w jakiś sposób osłabieni (zmniejszenie ataku lub obrony, uciekanie z walki przez kilka tur)
- różdżki/kostury (jedno lub dwuręczne), przystosowane pod rzucanie zaklęć 
##### Walka dystansowa

Atakowanie poprzez celowanie na pole. Zasięg zależny od broni. 

- krótki łuk, większa szybkość ataku kosztem mniejszego zasięgu
- długi łuk, większy zasięg kosztem mniejszej szybkości ataku, większe obrażenia od krótkiego łuku
- bomby, przy ataku robią obszarowy atak o kształcie +/ 3x3 / 5x5 zależnie od tieru bomby. 
- bronie rzucane, najmniejszy zasięg ze wszystkich i duże obrażenia

##### Magia

Postać może nauczyć się zaklęć z kamieni runicznych, niszczy to kamień i uczy postać zaklęcia do momentu jego oduczenia. Jest limit zaklęć posiadanych w danym momencie zależny od inteligencji. Obrażenia i efekty magii skalują się od inteligencji. Wiele szkół magii:
- święta Magia (głównie buffy i leczenie)
- nekromancja (przyzywanie jednostek, debuffy)
- ogień (głównie obrażenia)
- woda (ataki i buffy ochronne)
- ziemia (buffy ochronne, modyfikowanie otoczenia)
- trucizna (debuffy i obrażenia w czasie)
- magia bitewna (close-ranged ataki i buffy do walki wręcz)
- transformacja (buffy skupiające się głównie na walce bez użycia broni)

kilka "tierów" zaklęć. Im wyższy tier, tym zaklęcia są silniejsze, ale i rzadziej dostępne.

# Statystyki, rozwój postaci
zdrowie - punkty życia
zasób magiczny - rzucanie zaklęć, zależna od inteligencji
siła - obrażenia wręcz i z niektórych broni dystansowych (np bronie rzucane), zdrowie
zręczność - szansa na unik, obrażenia dystansowe i z szybszych broni wręcz (np sztylety)
inteligencja - ilość zaklęć, zasobu magicznego, siła zaklęć, dodatkowe obrażenia dla niektórych broni
szczęście - szansa na drop przedmiotów z potworów, szansa na wygenerowanie lepszych przedmiotów, szansa na trafienie krytyczne, dodatkowe obrażenia dla niektórych broni
Co level up zdrowie wzrasta i dodatkowo 3 punkty statystyk do rozdysponowania. 

# Lokacje
Zdecydowana większość gry dzieje się w wieżach. Każda wieża będzie różniła się designem, przeciwnikami i poziomami trudności. Na początku dostępny jest tylko pierwsza wieża. Kolejne odblokowują się po przejściu pierwszej wieży. Aby wejść do ostatniej wieży trzeba zebrać co najmniej 3 fragmenty, ale jest więcej wież możliwych do przejścia, które mają stanowić większe wyzwanie dla postaci niż samo przejście gry. Wstępnie planuję 1 wieżę startową, 3 stosunkowo proste wieże, 2 trudniejsze wieże i finałową wieżę, ale jeśli postęp gry będzie iść sprawnie może dodam więcej wież lub "alternatywne wieże" - przy generowaniu świata po raz pierwszy niektóre wieże mogą mieć kilka wariantów charakteryzujących się drobnymi zmianami.
W grze bohater pnie się w górę wieży. Nie można cofać się na poprzednie piętro. Na każdym poziomie wieży trzeba zrobić konkretną rzecz, aby przejść dalej. Jest to losowane przy wchodzeniu na konkretne piętro i gracz jest o tym informowany, jeśli jest to coś innego niż po prostu znalezienie przejścia na następne piętro.
##### Opcje, które przewiduję na ten moment (wrażliwe na późniejsze zmiany)
- pokonanie wszystkich przeciwników na mapie (przy pokonaniu przeciwnika jest informacja ilu przeciwników pozostało, w tym przypadku nowe potwory nie będą się pojawiać po wstępnym załadowaniu)
- pokonanie silnego przeciwnika (będzie odróżnialny od normalnych przeciwników, być może będzie widoczny dla gracza poza field of view)
- znalezienie przejścia na następne piętro

Trzecia opcja będzie tą, która jest najczęstsza. Pozostałe będą miały mniejszą szansę na pojawienie się. Po opcji nr 1 i 2 przejście pojawia się w pobliżu gracza.

Na ostatnim piętrze każdej wieży na gracza czeka boss encounter, po którym gracz otrzymuje fragment klucza i może wrócić do startowego holu, aby wyruszyć do kolejnych lokacji.

# ekwipunek
body armour, hełm, płaszcz, pierścienie (2), naszyjnik, buty, rękawice, main hand, offhand(jeśli mainhand jest jednoręczny)

każdy element wyposażenia ma statystyki i wymagania do efektywnego noszenia, np zbroja płytowa będzie wymagała jakąś ilość siły, aby móc ją nosić bez negatywnych efektów.

# przeciwnicy

Każdy przeciwnik ma te same statystyki co gracz. Jeśli jest humanoidem, to może również nosić te same przedmioty co gracz. 

# Inspiracja
Sam zarys fabularny jest nawiązaniem do południowokoreańskiego komiksu Tower of God, którego fabuła w skrócie opiera się o wspinanie się na tajemnicze wieże, po wejściu na które można spełnić swoje dowolne życzenie.

