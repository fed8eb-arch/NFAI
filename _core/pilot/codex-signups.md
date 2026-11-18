# Проверка регистрации по email

Адрес: `asdf150780@gmail.com`. Проверка выполнена в headless Chrome через Playwright. Статус «аккаунт есть» поставлен по переходу к экрану входа для введённого адреса, как указано в задании. Статус «капча» включает проверку браузера Cloudflare перед формой.

| Сервис | Итог | Текст ошибки |
|---|---|---|
| [arena.ai](codex-shots/arena.ai.png) | капча | Cloudflare: “Performing security verification” до формы. |
| [console.groq.com](codex-shots/console.groq.com.png) | ошибка | После «Continue with email» форма сбросилась. Запрос отправки ссылки прервался с `net::ERR_ABORTED`. |
| [elevenlabs.io](codex-shots/elevenlabs.io.png) | нужен пароль | — |
| [suno.com](codex-shots/suno.com.png) | ошибка | “Sign-in is not approved for this address. Please try a different method.” |
| [v0.app](codex-shots/v0.app.png) | ошибка | “Please try again or try a different sign up method. If you continue to have issues, please complete the account recovery form for further assistance.” |
| [tensor.art](codex-shots/tensor.art.png) | капча | Cloudflare: “Performing security verification” до формы. |
| [seaart.ai](codex-shots/seaart.ai.png) | аккаунт есть | — (форма «Login» с введённым email и полем пароля). |
| [dreamina.capcut.com](codex-shots/dreamina.capcut.com.png) | ошибка | Не удалось открыть форму по email. |
| [magichour.ai](codex-shots/magichour.ai.png) | ждёт код | — (запрос шестизначного кода из письма). |
| [viggle.ai](codex-shots/viggle.ai.png) | капча | Cloudflare: “Performing security verification” при переходе с главной в веб-приложение. |
| [udio.com](codex-shots/udio.com.png) | капча | После отправки email открылась hCaptcha: “Select the thing that fits inside the example”. |
| [creator.nightcafe.studio](codex-shots/creator.nightcafe.studio.png) | капча | Cloudflare: “Performing security verification” до формы. |
| [console.mistral.ai](codex-shots/console.mistral.ai.png) | аккаунт есть | — (после отправки email появилось «Please select a way to login». Для этого адреса показан вход через Google). |
| [huggingface.co/join](codex-shots/huggingface.co.png) | капча | “Let's confirm you are human” до формы. |
| [app.heygen.com](codex-shots/app.heygen.com.png) | ошибка | CloudFront: “403 ERROR. The request could not be satisfied. Bad request.” |
| [poe.com](codex-shots/poe.com.png) | капча | Cloudflare: “Performing security verification” до формы. |
