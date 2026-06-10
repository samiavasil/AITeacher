# HTML Accessibility (Достъпност)

## Alt текст (за img)
- Описва изображението за screen readers
- `<img src="pic.jpg" alt="Мъж, който пише код" />`

## Semantic HTML
- header, nav, main, section, article, footer
- Помага на screen readers да разберат структурата

## ARIA labels
- `aria-label`: за елементи без текст
- `aria-describedby`: свързване със описание
- `<button aria-label="Затвори менюто">×</button>`

## Form labels
- Всяко input трябва да има label
- `<label for="email">Имейл:</label><input id="email" type="email" />`

## Heading структура
- h1 -> h2 -> h3 (без пропускане)
- Един h1 на страницата

## Color и контраст
- Не разчитай только на цвят за информация
- Добър контраст между текст и фон

## Keyboard навигация
- Всички функционалности трябва да са достъпни с Tab и Enter
