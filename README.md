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

Poruszanie w 8 kierunkach na touchpadzie. Co do poruszania się diagonalnie - liczone jest jako jeden ruch.

Wszystkie akcje zajmują jakiś okres czasu - szybsze bronie atakują w mniej jednostek czasu niż wolniejsze. Obciążenie wyposażenia będzie wpływać w jakimś stopniu na to, jak szybko wykonywane są akcje gracza (ktoś w zbroi płytowej będzie chodzić wolniej niż ktoś w skórzanym wyposażeniu). 
Przykładowo - co turę każdy z aktorów dostaje 100 jednostek czasu do rozdysponowania. W momencie, gdy bohater zużyje te 100 jednostek lub będzie chciał zrobić coś, co zajmuje więcej jednostek czasu niż posiada aktualnie (na przykład atak dwuręczną bronią), to mija jego tura i ruszają się przeciwni aktorzy, którzy również mają 100 jednostek czasu do rozdysponowania. W momencie, gdy nie będą już mogli wykonać akcji, to kończy się ich tura i następuje tura gracza. Przykóładowo domyślnie ruch zajmuje 100 jednostek czasu. Jeśli bohater miałby ruch zajmujący 90 jednostek czasu (za sprawą statystyk lub magicznego przedmiotu), to po 9 turach zrobi jeden ruch "za darmo"

Chciałbym zaimplementować również algorytm autoeksplorowania mapy i atakowanie najbliższego przeciwnika wciskając jeden przycisk.

# Walka

Podział na walkę wręcz, walkę dystansową i magię. Większość ataków musi najpierw trafić przeciwnika, aby zadać mu obrażenia.

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
rozwijane statystyki przy lvl-upie:
siła - obrażenia wręcz i z niektórych broni dystansowych (np bronie rzucane), zdrowie
zręczność - szansa na unik, obrażenia dystansowe i z szybszych broni wręcz (np sztylety), prędkość ruchu
inteligencja - ilość zaklęć i zasobu magicznego, siła zaklęć, dodatkowe obrażenia dla niektórych broni, lepsze efekty zwojów
szczęście - więcej złota i większa szansa na otrzymanie lepszych przedmiotów z potwórow i podczas generowania mapy (efekt dopiero na kolejnym piętrze jeśli chodzi o generowanie mapy), szansa na trafienie krytyczne, dodatkowe obrażenia dla niektórych broni
klątwa - dosyć unikatowy atrybut, bo w pewnym sensie osłabia bohatera. Zmniejsza maksymalne zdrowie bohatera i może powodować inne negatywne efekty, ale za to zwiększa potencjał ofensywny bohatera (w pewnym sensie statystyka ta jest pod tzw. glass cannon buildy). Statystyka klątwy na wysokim poziomie pozwalałaby przede wszystkim spotkać ukrytego ostatniego bossa gry.
Co level up wzrasta zdrowie i otrzymuje się 3 punkty statystyk do rozdysponowania pomiędzy 5 dostępnych statystyk.

# Lokacje
Zdecydowana większość gry dzieje się w wieżach. Każda wieża będzie różniła się designem, przeciwnikami i poziomami trudności. Na początku dostępny jest tylko pierwsza wieża. Kolejne odblokowują się po przejściu pierwszej wieży. Aby wejść do ostatniej wieży trzeba zebrać co najmniej 3 fragmenty, ale jest więcej wież możliwych do przejścia, które mają stanowić większe wyzwanie dla postaci niż samo przejście gry. Wstępnie planuję 1 wieżę startową, 3 stosunkowo proste wieże, 2 trudniejsze wieże i finałową wieżę, ale jeśli postęp gry będzie iść sprawnie może dodam więcej wież lub "alternatywne wieże" - przy generowaniu świata po raz pierwszy niektóre wieże mogą mieć kilka wariantów charakteryzujących się drobnymi zmianami.
W grze bohater pnie się w górę wieży. Można cofać się na poprzednie piętra, ale nie można wyjść z wieży przed jej ukończeniem. Na każdym poziomie wieży trzeba zrobić konkretną rzecz, aby przejść dalej. Jest to losowane przy wchodzeniu na konkretne piętro i gracz jest o tym informowany, jeśli jest to coś innego niż po prostu znalezienie przejścia na następne piętro.
##### Opcje, które przewiduję na ten moment
- pokonanie wszystkich przeciwników na mapie (przy pokonaniu przeciwnika jest informacja ilu przeciwników pozostało, w tym przypadku nowe potwory nie będą się pojawiać po wstępnym załadowaniu)
- pokonanie silnego przeciwnika (będzie odróżnialny od normalnych przeciwników, być może będzie widoczny dla gracza poza field of view)
- znalezienie przejścia na następne piętro

Trzecia opcja będzie tą, która jest najczęstsza. Pozostałe będą miały mniejszą szansę na pojawienie się. Po opcji nr 1 i 2 przejście pojawia się w pobliżu gracza.

Na ostatnim piętrze każdej wieży na gracza czeka boss encounter, po którym gracz otrzymuje fragment klucza i może wrócić do startowego holu, aby wyruszyć do kolejnych lokacji.

# ekwipunek
body armour, hełm, płaszcz, pierścienie (2), naszyjnik, buty, rękawice, main hand, offhand(jeśli mainhand jest jednoręczny)
Rzadkości przedmiotów - normalny, magiczny, epicki, legendarny, unikatowy. Unikatowe przedmioty są pregenerowanymi przedmiotami, reszta jest generowana losowo. Normalne przedmioty nie mają żadnych dodatkowych efektów. Im rzadkość przedmiotu jest wyższa, tym więcej dodatkowych efektów może posiadać. Przedmioty mogą mieć również negatywne statystyki, które balansują się z bonusami - na przykład unikatowy naszyjnik może nie pozwalać używać zwojów, ale wszystkie znajdowane przedmioty zostają automatycznie zidentyfikowane.
każdy element wyposażenia ma statystyki i wymagania do efektywnego noszenia, np. zbroja płytowa będzie wymagała jakąś ilość siły, aby móc ją nosić bez negatywnych efektów.

Wstępnie wszystkie znalezione przedmioty są niezidentyfikowane, więc wymagają założenia lub użycia zwoju identyfikacji. Pierwsza opcja jest ryzykowna, gdyż przedmiot może być przeklęty - nie można go zdjąć bez wcześniejszego usunięcia klątwy.

# przedmioty użytkowe (jednorazowe)
- kamienie runiczne - nauka zaklęć, wymagają identyfikacji aby móc się ich nauczyć. Kolejna znaleziona instancja tego zaklęcia jest już zidentyfikowana. Mogą zostać użyte jako jednorazowe zaklęcie o mocniejszym efekcie niż nauczone permanentnie.
- mikstury - efekty pozytywne lub negatywne, można ich użyć bez identyfikacji, po napiciu się mikstury jest ona zidentyfikowana do końca aktualnego podejścia. Przykładowe efekty to uleczenie, trucizna (na pijącym), buff do obrażeń na kilkanaście tur. Można nimi rzucić w przeciwnika. Ich efekt działania nie skaluje się od statystyk, zawsze działają podobnie.
- zwoje - działają podobnie do mikstur. Efekty to np. identyfikacja przedmiotu, ulepszenie przedmiotu, teleportacja. Nie można nimi rzucić tak jak miksturami. Ich efekt działania skaluje się zależnie od inteligencji.
# przeciwnicy

Przeciwnicy mają te same statystyki co gracz. Jeśli jest humanoidem, to może również używać tych samych przedmiotów, co gracz. Jeśli przeciwnik jest wyposażony w jakieś przedmioty, to ma szansę na ich upuszczenie po śmierci. Przeciwnicy mogą respawnować się na mapie, ale tylko na obszarze jeszcze niezeksplorowanym przez gracza.

# Inspiracja
Sam zarys fabularny jest nawiązaniem do południowokoreańskiego komiksu Tower of God, którego fabuła w skrócie opiera się o wspinanie się na tajemnicze wieże, po wejściu na które można spełnić swoje dowolne życzenie.

