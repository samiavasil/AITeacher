# HTML Forms - Basics

## Основно
- Формите служат за събирането на информация от потребителя.
- Основни елементи: form, input, button, label.
- input е self-closing таг: `<input type="text" />`

## Видове input
- type="text": обикновен текстов кутия
- type="email": валидиран имейл
- type="password": скрит текст (точки вместо символи)
- type="checkbox": поле за избор
- type="radio": един избор от группа
- type="submit": бутон за изпращане

## Label елемент
- Обвързва текста със input за по-добра UX
- `<label for="username">Име:</label><input id="username" type="text" />`

## Button
- `<button type="submit">Изпрати</button>`
- type="submit": изпраща формата
- type="reset": отчиства полета
- type="button": функционален бутон (за JavaScript)

## Бележки от урока

- `form` е контейнерът, който събира всички полета и бутони за действие.
- `label` казва какво се очаква в полето и помага за по-добра достъпност.
- `input` е за кратки едноредови стойности, като име и email.
- `textarea` е за по-дълъг текст, като съобщение или обратна връзка.
- `button type="submit"` изпраща формата.

Как да избираш правилния елемент:

- Име: `input type="text"`
- Email: `input type="email"`
- Съобщение: `textarea`
- Изпращане: `button type="submit"`

Чести грешки и насоки:

- Използване на `input` вместо `textarea` за дълги съобщения.
- Липсващ или неясен `label`.
- Грешен `type` на input полето.
