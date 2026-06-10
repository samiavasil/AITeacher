# HTML Media Elements

## Video
```html
<video width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4" />
  Браузърът не поддържа видео елемент.
</video>
```

## Audio
```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg" />
  Браузърът не поддържа аудио елемент.
</audio>
```

## Атрибути
- controls: показва плейър
- autoplay: автоматично възпроизвеждане
- loop: повтаря
- muted: без звук

## Source елемент
- Позволява множество формати за съвместимост
- Браузърът избира първия поддържан формат

## Честа грешка
- Прескачане на fallback текст за браузъри, които не поддържат

## Бележки от урока

- Ако имаш повече от един формат, записваш всеки файл като отделен `source` елемент.
- Браузърът чете `source` елементите отгоре надолу и използва първия поддържан формат.

Пример с няколко source за video:

```html
<video controls width="640">
  <source src="movie.webm" type="video/webm" />
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.ogv" type="video/ogg" />
  Браузърът не поддържа видео елемент.
</video>
```

Пример с няколко source за audio:

```html
<audio controls>
  <source src="song.ogg" type="audio/ogg" />
  <source src="song.mp3" type="audio/mpeg" />
  Браузърът не поддържа аудио елемент.
</audio>
```

Важно разграничение:

- `video` и `audio` работят директно с файлове, които имаш локално или които сървърът ти подава като реални медийни файлове.
- YouTube не се подава като директен `source` в `video` или `audio`.
- Ако искаш YouTube съдържание в страница, обичайният начин е `iframe` embed, а не `audio` или `video` със `source`.

Плейване на видео стрийм:

- Ако имаш директен видео файл, можеш да го пуснеш с обикновен `video` елемент.
- Ако имаш streaming URL, най-често срещаните формати са HLS (`.m3u8`) и MPEG-DASH (`.mpd`).
- Не всички браузъри поддържат streaming форматите директно.

Практично правило:

- Обикновен `.mp4` файл: `video` + `source`
- YouTube/Vimeo: `iframe` embed
- HLS/DASH stream: често се използва JavaScript player библиотека, например `hls.js` или `Shaka Player`
