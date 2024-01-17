# Tower of God - roguelike game

# Ogólny zarys fabularny

Gra jest oczywiście klasycznym roguelikiem. Cel gry polega na wejściu na szczyt tytułowej wieży, co pozwoli spełnić dowolne życzenie postaci gracza. Nie można zrobić jednak tego na samym początku gry, ponieważ aby do niej wejść należy zebrać fragmenty klucza z 2 wież.

# Start gry

gracz na starcie wybiera jedynie rasę. 

Gra zaczyna się bez jakiegokolwiek ekwipunku w holu, w którym od sklepikarzy można kupić wyposażenie. Asortyment sklepów aktualizuje się wraz z przechodzeniem kolejnych lokacji. Początkowo można wejść tylko do jednej lokacji, reszta pozostaje niedostępna.

# Rasy
Rasa określa dodatkowe umiejętności gracza (aktywne/pasywne, negatywne/pozytywne) oraz startową walutę (Punkty Wieży). Im rasa ma lepsze bonusy startowe, tym mniej waluty na wyposażenie dostanie na start gry. Ma to w pewien sposób balansować rozgrywkę - niektóre rasy początek gry będą miały ułatwiony poprzez dostęp do dobrego ekwipunku, a niektóre poprzez bonusy za pośrednictwem umiejętności rasowych. 
W grze występują 3 rasy:
- Human - sporo złota, przeciętne statystyki, bonus rasowy to lekko zwiększone zdobywanie doświadczenia
- Wraithraiser (rasa wyglądająca jak duży człekokształtny krokodyl o brunatnym kolorze skóry) - mało złota, zaczyna z lepszymi statystykami od człowieka, nie może nosić broni jednoręcznych, bronie dwuręczne klasyfikowane są jako bronie jednoręczne, ograniczony dostęp do ekwipunku - większość przedmiotów przystosowana jest pod normalne rozmiary, więc zdobywanie wyposażenia jest utrudnione.
- Rashang (ludzko wyglądająca rasa o znamieniach na twarzy wyglądających inaczej u każdej osoby) - mało złota, co 3 poziomy dostaje wybór 1 losowego zaklęcia z 3 podanych, które są mocniejszymi wersjami tych zaklęć, ale nie może uczyć się zaklęć normalnie. Wybiera też 2 zaklęcia na samym początku gry.

# Poruszanie się, czas

Poruszanie w 8 kierunkach na touchpadzie. Co do poruszania się diagonalnie - liczone jest jako jeden ruch.

Jeden akcja postaci jest interpretowana jako jedna tura. Jeśli postać jest szybsza, raz na kilka tur wykonuje dodatkową turę. Analogicznie w przypadku wolniejszych postaci.

# Walka

Podział na walkę wręcz, walkę dystansową i magię.

Cechy liczące się w walce:
- zdrowie
- broń (szansa na trafienie i obrażenia)
- pancerz (szansa na unik i redukcja obrażeń)
- siła (obrażenia)
- zręczność (szansa na trafienie i unik)
- klątwa (zwiększa zadawane obrażenia i szansę na trafienie ale jednocześnie zwiększa otrzymywane obrażenia i zmniejsza szansę na unik)

Przebieg walki:
- trafienie: szansa na trafienie broni + zręczność atakującego + klątwa atakującego - szansa na unik broniącego - zręczność broniącego + klątwa broniącego. Szansa na trafienie zawsze wynosi co najmniej 5 (5% szans)
rzut kością d100, sukces to liczba mniejsza lub równa "rzut na trafienie"


jeśli rzut się udał, to następuje losowanie od 0.50 do 1.50. Zadane obrażenia to floor((obrażenia broni) * losowanie) + siła atakującego + klątwa atakującego - redukcja obrażeń broniącego. Zadane obrażenia zawsze wynoszą co najmniej 1. Jeśli zdrowie po otrzymaniu ataku będzie mniejsze lub równe 0, to broniący umiera.

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

Postać może nauczyć się zaklęć z kamieni runicznych, niszczy to kamień i uczy postać zaklęcia. Jest limit zaklęć posiadanych w danym momencie zależny od inteligencji. Obrażenia i efekty magii skalują się zależnie od inteligencji (lub siły w przypadku magii bitewnej)
- święta Magia
Heal, Smite, Holy Intervention
- magia śmierci
Drain life, Blindness, Raise Dead
- ogień
Spark, Fireball, Flame Wall
- natura
Create Mud, Raise Terrain, Shatter
- trucizna 
Infect, Accelerate Circulation, Contagion 
- magia bitewna
Heroism, Blade Storm, Bloodlust
- transformacja 
Blade Hands, Native Form, Titan Form


# Statystyki, rozwój postaci
- zdrowie - punkty życia, zależne od siły
- zasób magiczny - rzucanie zaklęć, zależny od inteligencji

rozwijane statystyki przy lvl-upie:
- siła - obrażenia wręcz i z niektórych broni dystansowych (np bronie rzucane), zdrowie
- zręczność - szansa na unik, obrażenia dystansowe, prędkość ruchu
- inteligencja - ilość zaklęć i zasobu magicznego, siła zaklęć, dodatkowe obrażenia dla niektórych broni, lepsze efekty zwojów
- szczęście - więcej złota i większa szansa na otrzymanie lepszych przedmiotów z potwórow i podczas generowania mapy (efekt dopiero na kolejnym piętrze jeśli chodzi o generowanie mapy), szansa na trafienie krytyczne, dodatkowe obrażenia dla niektórych broni
- klątwa - dosyć unikatowy atrybut, bo w pewnym sensie osłabia bohatera. zwiększa szansę na otrzymanie obrażeń, ale za to zwiększa potencjał ofensywny bohatera (w pewnym sensie statystyka ta jest pod tzw. glass cannon buildy). Statystyka klątwy na wysokim poziomie pozwalałaby przede wszystkim spotkać ukrytego ostatniego bossa gry.

Co level up wzrasta zdrowie i otrzymuje się 3 punkty statystyk do rozdysponowania pomiędzy 5 dostępnych statystyk.

# Lokacje
Zdecydowana większość gry dzieje się w wieżach. Każda wieża będzie różniła się designem, przeciwnikami i poziomami trudności. Na początku dostępny jest tylko pierwsza wieża. Aby wejść do trzeciej wieży trzeba zebrać 2 fragmenty z poprzednich wież. 
W grze bohater pnie się w górę wieży. Można cofać się na poprzednie piętra, ale nie można wyjść z wieży przed jej ukończeniem. Warunkiem skończenia wieży jest pokonanie przeciwnika na jej szczycie.
# ekwipunek
body armour, hełm, płaszcz, pierścienie (2), naszyjnik, buty, main hand, offhand(jeśli mainhand jest jednoręczny)
Rzadkości przedmiotów - normalny, magiczny, epicki, legendarny, unikatowy. Unikatowe przedmioty są pregenerowanymi przedmiotami, reszta jest generowana losowo. Normalne przedmioty nie mają żadnych dodatkowych efektów. Im rzadkość przedmiotu jest wyższa, tym więcej dodatkowych efektów może posiadać.

# przedmioty użytkowe (jednorazowe)
- kamienie runiczne - nauka zaklęć. Każdy kamień runiczny może pojawić się tylko raz. Od początku wiadomo, jakiego zaklęcia uczy dany kamień runiczny.
- mikstury - efekty pozytywne lub negatywne, można ich użyć bez identyfikacji, po napiciu się mikstury jest ona zidentyfikowana do końca aktualnego podejścia. Przykładowe efekty to uleczenie, trucizna (na pijącym), buff do obrażeń na kilkanaście tur. Ich efekt działania nie skaluje się od statystyk, zawsze działają tak samo.
- zwoje - mechanicznie działają podobnie do mikstur. Efekty to np. identyfikacja przedmiotu, ulepszenie przedmiotu, teleportacja. Ich efekt działania nie skaluje się od statystyk, zawsze działają tak samo.
# przeciwnicy

Przeciwnicy mają te same statystyki co gracz. Jeśli jest humanoidem, to może również używać tych samych przedmiotów, co gracz. Jeśli przeciwnik jest wyposażony w jakieś przedmioty, to ma szansę na ich upuszczenie po śmierci. Przeciwnicy mogą respawnować się na mapie, ale tylko na obszarze jeszcze niezeksplorowanym przez gracza.


Przeciwnicy dodani na ten moment:

Human with leather armor and longsword
hp: 10
siła: 5
zręczność: 5
szczęście: 5
klątwa: 0
broń: Longsword
pancerz: Leather armor

Human with plate armor and warhammer
hp: 10
siła: 5
zręczność: 5
szczęście: 5
klątwa: 0
broń: Warhammer
pancerz: Plate armor

Dog 
hp: 5
siła: 1
zręczność: 2
szczęście: 3
klątwa: 1
broń: Claws
pancerz: Hide

Green Jelly
hp: 9 
siła: 2
zręczność: 3
szczęście: 5
klątwa: 1
broń: Tentacle
pancerz: Jelly body

Blue Jelly
hp: 18
siła: 3
zręczność: 5
szczęście: 5
klątwa: 1
broń: Tentacle
pancerz: Jelly body 

Oni 
hp: 60
siła: 15
zręczność: 3
szczęście: 5
klątwa: 3
broń: Warhammer 
pancerz: Hide

Tower Master
hp: 250
siła: 45
zręczność: 45
szczęście: 15
klątwa: 15
broń: Warhammer
pancerz: Hide




# Inspiracja
Sam zarys fabularny jest nawiązaniem do południowokoreańskiego komiksu Tower of God, którego fabuła w skrócie opiera się o wspinanie się na tajemnicze wieże, po wejściu na które można spełnić swoje dowolne życzenie.

