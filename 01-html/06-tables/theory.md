# HTML Tables

## Основна структура
```html
<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1</td>
    <td>Data 2</td>
  </tr>
</table>
```

## Елементи
- table: контейнер
- tr (table row): ред
- th (table header): заголовна клетка
- td (table data): обикновена клетка

## Допълнителни елементи
- thead, tbody, tfoot: структури за големи таблици
- colspan, rowspan: свързване на клетки

## Употреба
- Таблици за структурирани данни (не за оформление!)
- Всяка колона има смислена глава

## Честа грешка
- Използване на таблици за подредба на страницата: това е мало, ползвай CSS Grid/Flexbox!

## Бележки от урока

Пример за подредена таблица с `thead`, `tbody` и `tfoot`:

```html
<table>
  <thead>
    <tr>
      <th>Име</th>
      <th>Математика</th>
      <th>Английски</th>
      <th>Химия</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Иван</td>
      <td>5</td>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Мария</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Петър</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Средно</td>
      <td>5.0</td>
      <td>5.7</td>
      <td>5.3</td>
    </tr>
  </tfoot>
</table>
```

Бърза проверка при подредба:

- Всеки `tr` има еднакъв брой клетки.
- Заглавията са в `th`, данните в `td`.
- Използвай `thead` за заглавия и `tbody` за основни данни.
