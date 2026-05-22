
# Meta Tags

## Основни meta тагове (в head)
- `<meta charset="UTF-8" />`: Определя кодирането на страницата (най-често UTF-8)
- `<meta name="viewport" content="width=device-width, initial-scale=1" />`: За правилно мащабиране на мобилни устройства

## SEO meta тагове
- `<meta name="description" content="..." />`: Кратко описание на страницата (за търсачки)
- `<meta name="keywords" content="..." />`: Ключови думи (днес почти не се използва от търсачките)

## Open Graph (за социални мрежи)
- `<meta property="og:title" content="..." />`: Заглавие за споделяне в социални мрежи
- `<meta property="og:description" content="..." />`: Описание за споделяне
- `<meta property="og:image" content="..." />`: Картинка за preview

## Други полезни meta тагове
- `<meta name="author" content="..." />`: Автор на страницата
- `<meta name="robots" content="index, follow" />`: Дава инструкции на търсачките дали да индексират страницата

## Подробно за http-equiv
`http-equiv` е специален атрибут на `<meta>`, който изпраща инструкции към браузъра, подобно на HTTP header-и. Използва се по-рядко, но е важен в някои случаи.

### Често използвани http-equiv meta тагове:
- `<meta http-equiv="refresh" content="5; url=https://example.com">` — Презарежда страницата след 5 секунди и пренасочва към друг адрес.
- `<meta http-equiv="content-type" content="text/html; charset=UTF-8">` — Определя типа съдържание и кодирането (днес се предпочита charset="UTF-8" без http-equiv).
- `<meta http-equiv="X-UA-Compatible" content="IE=edge">` — Казва на Internet Explorer да използва най-новия рендериращ режим.

### Други примери:
- `<meta http-equiv="cache-control" content="no-cache">` — Контролира кеширането на страницата.
- `<meta http-equiv="expires" content="0">` — Задава кога страницата изтича (остарява).

## Обобщен списък с често използвани meta тагове
| Таг | Описание |
|-----|----------|
| `<meta charset="UTF-8">` | Кодиране на страницата |
| `<meta name="viewport" content="width=device-width, initial-scale=1">` | Мобилна оптимизация |
| `<meta name="description" content="...">` | Описание за търсачки |
| `<meta name="keywords" content="...">` | Ключови думи |
| `<meta name="author" content="...">` | Автор |
| `<meta name="robots" content="index, follow">` | Индексиране от търсачки |
| `<meta property="og:title" content="...">` | Open Graph заглавие |
| `<meta property="og:description" content="...">` | Open Graph описание |
| `<meta property="og:image" content="...">` | Open Graph изображение |
| `<meta http-equiv="refresh" content="5; url=https://example.com">` | Автоматично пренасочване |
| `<meta http-equiv="X-UA-Compatible" content="IE=edge">` | IE режим |
| `<meta http-equiv="cache-control" content="no-cache">` | Кеширане |

## Защо е важно?
- Търсачките използват meta description
- Социалните мрежи използват OG тагове за preview
- Viewport е задължителен за мобилни
- http-equiv може да контролира поведение на браузъра
