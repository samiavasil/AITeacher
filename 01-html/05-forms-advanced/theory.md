# HTML Forms - Advanced

## Textarea
- За дълги текстове (многоредови)
- `<textarea rows="4" cols="50"></textarea>`

## Select (выборен списък)
- Падащ списък
```html
<select>
  <option>Опция 1</option>
  <option>Опция 2</option>
</select>
```

## Fieldset и Legend
- Групира свързани полета
- Legend е заглавие на групата
```html
<fieldset>
  <legend>Лични данни</legend>
  <!-- полета -->
</fieldset>
```

## Checkbox и Radio
- checkbox: множествен избор
- radio: един избор от група
```html
<input type="checkbox" id="c1" />
<label for="c1">Съгласен съм</label>
```

## Валидиране (basic HTML attributes)
- required: поле е задължително
- minlength, maxlength: дължина на текст
- pattern: регулярен израз

## Бележки от урока

- Advanced form означава форма с по-добра структура, контрол и валидация.
- Целта е потребителят да попълни по-лесно и по-малко да греши.

Практичен сценарий: регистрация

- Лични данни: име и email
- Избор на пол: radio (само една опция)
- Избор на държава: select
- Съгласие с условията: checkbox
- Допълнителна бележка: textarea

Кога какво използваш:

- radio: когато трябва точно един избор от група (пример: мъж или жена)
- checkbox: когато е отметка да или не (пример: съгласен съм с условията)
- select: когато имаш списък с фиксирани стойности (пример: държава)
- textarea: когато очакваш дълъг текст

Защо fieldset и legend са важни:

- group-ват логически свързаните полета
- правят формата по-четима за хора и screen readers
- намаляват хаоса при по-дълги форми

Примерна логика на валидация без JavaScript:

- име: required и minlength 3
- email: type email и required
- пол: required radio група
- съгласие: required checkbox

Чести грешки и насоки:

- Смесване на radio и checkbox: ако е един избор, използвай radio.
- Липсващи еднакви name стойности при radio група: тогава не работи като един избор.
- Липсващи labels: прави формата неясна.
- Използване на input вместо textarea за дълги бележки.
