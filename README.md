# Tower of God - roguelike game

# Ogólny zarys fabularny

Gra jest oczywiście klasycznym roguelikiem. Cel gry polega na wejściu na szczyt tytułowej wieży, co pozwoli spełnić dowolne życzenie postaci gracza. Nie można zrobić jednak tego na samym początku gry, ponieważ aby do niej wejść należy zebrać fragmenty klucza z co najmniej 3 innych wież.

# Start gry

gracz na starcie wybiera jedynie rasę. Rasa określa jego dodatkowe umiejętności (aktywne/pasywne, negatywne/pozytywne) oraz startową walutę (Punkty Wieży). Im rasa ma lepsze bonusy startowe, tym mniej waluty na wyposażenie dostanie na start gry. Ma to w pewien sposób balansować rozgrywkę - niektóre rasy początek gry będą miały ułatwiony poprzez dostęp do dobrego ekwipunku, a niektóre poprzez bonusy za pośrednictwem umiejętności rasowych. 

Gra zaczyna się w holu, w którym od sklepikarzy można kupić wyposażenie, które wraz z przechodzeniem kolejnych lokacji będzie się aktualizować. Początkowo można wejść tylko do jednej lokacji, reszta pozostaje niedostępna.

# Rasy

# Poruszanie się, czas

Poruszanie w 8 kierunkach. Co do poruszania się diagonalnie - wydaje mi się że najlepszym rozwiązaniem jest liczenie czasu potrzebnego na przejście pola jako 1,41 zamiast 1. 

Wszystkie akcje zajmują ileś czasu - szybsze bronie atakują w mniej jednostek czasu niż wolniejsze. Być może zdecyduję się również na to, że obciążenie wyposażenia będzie wpływać w jakimś stopniu na to, jak szybko wykonywane są akcje gracza (ktoś w zbroi płytowej będzie chodzić wolniej niż ktoś w skórzanym wyposażeniu). 

Potwory spotykane przez gracza nie zawsze poruszają się z taką samą prędkością jak gracz. Mogą być lekko szybsze lub wolniejsze (co x ruchów przechodziłyby np. 2 pola zamiast 1)

# Walka

Atakowanie przeciwników poprzez "wchodzenie" w nich. Na początku skupię się głównie na walce wręcz, jeśli starczy czasu chciałbym również dodać walkę dystansową i magię.
##### Rodzaje broni
- miecze jednoręczne, umiarkowana szybkość i obrażenia, możliwość dual wieldingu/noszenia tarczy.
- sztylety, wysoka szybkość, niskie obrażenia
- kosy, niska szybkość, wysokie obrażenia, ataki trafiają więcej niż 1 przeciwnika na raz (atak wokół postaci bohatera)
- ataki bez użycia broni, umiarkowana szybkość i bez dodatkowych bonusów praktycznie zerowe obrażenia
-
# Statystyki, rozwój postaci

# Lokacje
W grze bohater cały czas pnie się w górę wieży. Nie można cofać się na poprzednie piętro. Na każdym poziomie wieży trzeba zrobić konkretną rzecz aby przejść dalej. Jest to losowane przy wchodzeniu na konkretne piętro i gracz jest o tym informowany, jeśli jest to coś innego niż znalezienie przejścia na następne piętro.
##### Opcje, które przewiduję na ten moment (wrażliwe na późniejsze zmiany)
- pokonanie wszystkich przeciwników na mapie (przy pokonaniu przeciwnika jest informacja ilu przeciwników pozostało, w tym przypadku nowe potwory nie będą się pojawiać po wstępnym załadowaniu)
- pokonanie silnego przeciwnika (będzie odróżnialny od normalnych przeciwników, być może będzie widoczny dla gracza poza field of view)
- znalezienie przejścia na następne piętro

Trzecia opcja będzie tą, która jest najczęstsza. Pozostałe będą miały mniejszą szansę na pojawienie się. Po opcji nr 1 i 2 przejście pojawia się w pobliżu gracza.

Na ostatnim piętrze każdej wieży na gracza czeka boss encounter, po którym gracz otrzymuje fragment klucza i może wrócić do startowego holu, aby wyruszyć do kolejnych lokacji.

# Inspiracja
Sam zarys fabularny jest nawiązaniem do południowokoreańskiego komiksu Tower of God, którego fabuła w skrócie opiera się o wspinanie się na tajemnicze wieże, po wejściu na które można spełnić swoje dowolne życzenie.


































## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://umcs.schneiderp.ovh/mateusz.targonski/tower-of-god-roguelike-game.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://umcs.schneiderp.ovh/mateusz.targonski/tower-of-god-roguelike-game/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
