# Ручна перевірка витягнутих фактів

## Як проходила перевірка

Модель витягла з текстів 302 факти. Для перевірки взято 20 випадкових (їх вибирає скрипт `sample_check.py` з фіксованим `random.seed(42)`, тож при повторному запуску вибірка та сама).

Кожен факт порівнювався з цитатою з тексту. Також у самій статті знаходилося це місце і читалося речення навколо нього, щоб перевірити не лише слова, а й тип сутностей та напрямок зв'язку. Якщо факт у тексті справді так сказаний, стоїть ✔, якщо ні, ✘ і коротко написано, що не так.

## Підсумкова таблиця

| № | Факт | Вердикт |
|:-:|---|:-:|
| 1 | James (Person) → founded → Rephlex Records (Label) | ✔ |
| 2 | Pauline Oliveros (Person) → member_of → The San Francisco Tape Music Center (Label) | ✘ |
| 3 | Jeff Mills (Person) → member_of → Underground Resistance (Artist) | ✔ |
| 4 | Sandison brothers (Artist) → influenced_by → Joni Mitchell (Artist) | ✔ |
| 5 | Skam Records (Label) → released → Hi Scores (Album) | ✔ |
| 6 | James (Person) → released → 2 Remixes By AFX (Album) | ✔ |
| 7 | Max Richter (Artist) → released → Sleep (Album) | ✔ |
| 8 | Jarvis Cocker (Person) → member_of → Pulp (Artist) | ✔ |
| 9 | Slowdive (Artist) → released → Pygmalion (Album) | ✔ |
| 10 | Jon-5 (Person) → member_of → Cybotron (Artist) | ✔ |
| 11 | King Tubby (Artist) → has_genre → dub (Genre) | ✔ |
| 12 | Ralf Hutter (Person) → member_of → Kraftwerk (Artist) | ✔ |
| 13 | Roger Karmanik (Person) → member_of → Brighter Death Now (Artist) | ✔ |
| 14 | Mike Sandison (Person) → member_of → Boards of Canada (Artist) | ✔ |
| 15 | Boards of Canada (Artist) → released → Inferno (Album) | ✔ |
| 16 | jungle (Genre) → influenced_by → house (Genre) | ✔ |
| 17 | Terry Riley (Person) → member_of → The San Francisco Tape Music Center (Label) | ✘ |
| 18 | Boards of Canada (Artist) → signed_to → Warp (Label) | ✔ |
| 19 | Boards of Canada (Artist) → released → Geogaddi (Album) | ✔ |
| 20 | Juan Atkins (Person) → member_of → Cybotron (Artist) | ✔ |

## Деталі по кожному факту

**1. James (Person) → founded → Rephlex Records (Label)** ✔

> He and James founded Rephlex Records in 1991.
> *— Aphex_Twin.txt*

**2. Pauline Oliveros (Person) → member_of → The San Francisco Tape Music Center (Label)** ✘

> Other composers working with tape recorders became members and collaborators including Pauline Oliveros
> *— Ambient_music.txt*

Помилка: зв'язок правильний (у статті Oliveros — «founding member and director of the San Francisco Tape Music Centre»), але тип неправильний: це студія і місце для концертів, а не Label

**3. Jeff Mills (Person) → member_of → Underground Resistance (Artist)** ✔

> Underground Resistance (featuring Mike Banks, Jeff Mills, and Robert Hood)
> *— Detroit_techno.txt*

**4. Sandison brothers (Artist) → influenced_by → Joni Mitchell (Artist)** ✔

> Sandison brothers have named several acts that influence their work including Joni Mitchell
> *— Boards_of_Canada.txt*

Примітка: сутність не об'єднана: «Sandison brothers» — це Boards of Canada

**5. Skam Records (Label) → released → Hi Scores (Album)** ✔

> contacting Skam Records, leading to the release of Hi Scores in 1996 on the label.
> *— Boards_of_Canada.txt*

**6. James (Person) → released → 2 Remixes By AFX (Album)** ✔

> In 2001 James also released a short EP, 2 Remixes By AFX
> *— Aphex_Twin.txt*

Примітка: EP записано як Album; James не пов'язаний з Aphex Twin

**7. Max Richter (Artist) → released → Sleep (Album)** ✔

> Max Richter's album Sleep
> *— Ambient_music.txt*

**8. Jarvis Cocker (Person) → member_of → Pulp (Artist)** ✔

> Jarvis Cocker, a member of the Sheffield band Pulp
> *— Warp_record_label.txt*

**9. Slowdive (Artist) → released → Pygmalion (Album)** ✔

> Dream pop band Slowdive's 1995 album Pygmalion
> *— Ambient_music.txt*

**10. Jon-5 (Person) → member_of → Cybotron (Artist)** ✔

> Atkins began recording with musical partner Richard Davis (and later with a third member, Jon-5) as Cybotron.
> *— Techno.txt*

**11. King Tubby (Artist) → has_genre → dub (Genre)** ✔

> Jamaican dub musicians such as King Tubby
> *— Ambient_music.txt*

**12. Ralf Hutter (Person) → member_of → Kraftwerk (Artist)** ✔

> Ralf Hutter of early electronic pioneers Kraftwerk
> *— Ambient_music.txt*

**13. Roger Karmanik (Person) → member_of → Brighter Death Now (Artist)** ✔

> Roger Karmanik of Brighter Death Now
> *— Ambient_music.txt*

**14. Mike Sandison (Person) → member_of → Boards of Canada (Artist)** ✔

> Boards of Canada became a duo of brothers Mike Sandison and Marcus Eoin.
> *— Boards_of_Canada.txt*

**15. Boards of Canada (Artist) → released → Inferno (Album)** ✔

> On 29 May 2026, Boards of Canada released their fifth studio album, Inferno.
> *— Boards_of_Canada.txt*

Примітка: у цитаті «On» написано з великої літери, у статті з маленької; сам факт правильний

**16. jungle (Genre) → influenced_by → house (Genre)** ✔

> jungle (drum and bass) demonstrated influences ranging from hip hop, soul, and reggae to techno and house.
> *— Techno.txt*

**17. Terry Riley (Person) → member_of → The San Francisco Tape Music Center (Label)** ✘

> Other composers working with tape recorders became members and collaborators including Pauline Oliveros, Terry Riley and Steve Reich.
> *— Ambient_music.txt*

Помилка: та сама, що в №2: Tape Music Center названо Label, хоча це студія. Сам зв'язок правильний (у статті Riley серед «members and collaborators»)

**18. Boards of Canada (Artist) → signed_to → Warp (Label)** ✔

> In 1998, Warp signed the electronic duo Boards of Canada
> *— Warp_record_label.txt*

**19. Boards of Canada (Artist) → released → Geogaddi (Album)** ✔

> This was followed by their second studio album Geogaddi (2002)
> *— Boards_of_Canada.txt*

**20. Juan Atkins (Person) → member_of → Cybotron (Artist)** ✔

> Atkins began recording with musical partner Richard Davis (and later with a third member, Jon-5) as Cybotron.
> *— Techno.txt*

## Що вийшло

З 20 перевірених фактів **18 правильні, тобто 90%**. Якихось вигаданих фактів, яких немає в тексті, я не знайшов.

## Які помилки трапляються

Помилок небагато, і вони схожі між собою:

- **Не той тип.** Двічі (факти 2 і 17) модель назвала «The San Francisco Tape Music Center» лейблом. Насправді це була студія і місце для концертів. У нашій схемі такого типу немає, тож модель взяла найближчий.
- **Одна людина чи гурт під різними іменами.** «James» і «Aphex Twin» це одна людина, а «Sandison brothers» це гурт Boards of Canada. Модель їх не з'єднала, тому в графі вони стануть окремими вузлами (факти 1, 4, 6).
- **Неточний тип.** У факті 6 міні-альбом (EP) записаний просто як альбом.
- **Цитата не зовсім дослівна.** У факті 15 модель написала «On» з великої літери, а в статті слово стоїть посеред речення з маленької. Сам факт правильний, просто скрипт через це показав «ні».

## Чого ця перевірка не показує

Перевірялося тільки те, що модель знайшла. А чи не пропустила вона щось важливе в тексті, цією вибіркою не дізнатись: для цього треба було б читати статті і шукати факти самому.
