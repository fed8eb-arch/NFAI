const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require('/usr/local/lib/pnpm/5/.pnpm/playwright-core@1.59.1/node_modules/playwright-core');

const project = path.resolve(__dirname, '..');
const results = path.join(project, 'results');
const email = 'asdf150780@gmail.com';
const confirmed = new Set([1, 3, 4, 6, 7, 8, 9, 10, 11, 15, 16, 17, 18, 22, 25, 27, 32, 42]);
const excluded = new Set([19, 31]);
const skips = new Map([
  [2, 'Только вручную по брифу'],
  [5, 'Аккаунт не требуется, только ручной доступ по брифу'],
  [20, 'Аккаунт уже создан, для активации нужен телефон по брифу'],
  [21, 'Только личное использование по брифу'],
  [23, 'Нужен ручной вход владельца в существующий аккаунт по брифу'],
]);
const entry = new Map([
  [28, 'https://designer.microsoft.com'], [33, 'https://huggingface.co/join'],
  [35, 'https://chat.deepseek.com/'], [40, 'https://chatgpt.com/'],
  [41, 'https://www.perplexity.ai/'], [45, 'https://klingai.com/'],
  [46, 'https://hailuoai.video/'], [47, 'https://pixverse.ai/'],
  [48, 'https://www.vidu.com/'], [51, 'https://www.freepik.com/'],
]);
const signup = /^(sign\s*up(?: for free| - it.s free)?|register|create (?:an? |your )?account|join now|регистрация|зарегистрироваться|создать аккаунт)$/i;
const gateway = /^(get started(?: for free)?|try for free|start creating(?: free)?|create with google flow|open krea|launch app|log\s*in|sign\s*in|войти|вход|начать)$/i;
const next = /^(continue|next|continue with email|продолжить|далее)$/i;
const magic = /magic link|sign[- ]?in link|log[- ]?in link|passwordless|we.ll (?:send|email) you a link|ссылк[ауи] для входа/i;
const password = 'input[type=password]:visible, input[autocomplete="new-password"]:visible, input[autocomplete="current-password"]:visible';
const card = 'input[autocomplete^=cc-]:visible, iframe[title*=payment i]:visible';
const phone = 'input[type=tel]:visible, input[autocomplete="tel"]:visible';
const mail = 'input[type=email]:visible, input[autocomplete="email"]:visible, input[name="email" i]:visible, input[placeholder*="email" i]:visible';
const captcha = 'iframe[src*="captcha" i]:visible, iframe[src*="challenges.cloudflare.com"]:visible';
const blocked = /verify (?:that )?you are human|verify you.re human|human verification|are you (?:a human|a robot)|checking your browser|just a moment|security verification|access denied|forbidden|not available in your (?:country|region)|unsupported.country|something went wrong|this site can.t be reached|verify (?:your )?(?:email|phone)|check your (?:email|inbox)|enter (?:the |your )?(?:verification |security |confirmation )?code|payment required|(?<!no )credit card required|confirm (?:that )?you are (?:at least )?18|age verification/i;
const success = /^(?:your account has been created[.!]?|account created successfully[.!]?|registration (?:complete|successful)[.!]?|вы успешно зарегистрировались[.!]?)$/i;
const cell = value => String(value).replaceAll(email, '[email]').replace(/\b\d{4,8}\b/g, '[число скрыто]').replaceAll('|', '&#124;').replaceAll('\n', '<br>');
const normalize = value => value.replace(/\s+/g, ' ').trim();

async function inspect(page) {
  const body = page.locator('body');
  const lines = (await body.innerText({ timeout: 1200 }).catch(() => '')).split('\n').map(normalize).filter(Boolean);
  const alert = await page.getByRole('alert').first().innerText({ timeout: 350 }).catch(() => '');
  const stop = lines.find(line => blocked.test(line));
  if (stop && stop.length < 220) return stop;
  if (alert.trim() && alert.length < 240 && /error|invalid|failed|denied|blocked|unavailable|ошибка/i.test(alert)) return alert.trim();
  for (const [selector, kind] of [[card, 'Оплата'], [captcha, 'CAPTCHA'], [phone, 'Телефон'], [password, 'Пароль']]) {
    const field = page.locator(selector).first();
    if (await field.isVisible()) {
      const label = await field.evaluate(el => el.labels?.[0]?.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || el.title || el.closest('label')?.innerText || '');
      return label || `${kind}: видимый элемент без текстовой подписи`;
    }
  }
  return null;
}

async function action(page, pattern, links = true) {
  const buttons = page.getByRole('button', { name: pattern });
  const matches = links ? buttons.or(page.getByRole('link', { name: pattern })) : buttons;
  for (const target of await matches.all()) {
    if (await target.isVisible() && await target.isEnabled()) return target;
  }
  return null;
}

async function visit(browser, item) {
  const context = await browser.newContext({ acceptDownloads: false });
  let page = await context.newPage();
  page.setDefaultTimeout(3500);
  let timer;
  let expired = false;
  let shot = '—';
  async function run() {
    const response = await page.goto(entry.get(item.id) || item.url, { waitUntil: 'domcontentloaded', timeout: 26000 });
    if (response?.status() >= 400) {
      const heading = await page.locator('h1:visible, h2:visible').first().innerText({ timeout: 800 }).catch(() => '');
      return { reason: `HTTP ${response.status()}${heading.trim() ? ' · «' + heading.trim() + '»' : ''}` };
    }
    let registration = item.id === 33;
    for (let step = 0; step < 4; step++) {
      await page.waitForTimeout(450);
      const reason = await inspect(page);
      if (reason) return { reason };
      const emailField = page.locator(mail).first();
      const body = await page.locator('body').innerText({ timeout: 1500 });
      if (new URL(page.url()).hostname === 'accounts.google.com') {
        const heading = await page.getByRole('heading').first().innerText({ timeout: 1000 }).catch(() => 'Google Accounts');
        return { reason: heading };
      }
      const authHeading = page.getByRole('heading', { name: /sign up below|create an account|register|регистрация/i }).first();
      const codeFlow = /send a code to your inbox|verification code|one.time code|код подтверждения/i;
      if (await authHeading.isVisible() || /sign up below to unlock/i.test(body) || (item.id === 66 && codeFlow.test(body))) registration = true;
      if (await emailField.isVisible() && registration) {
        const form = emailField.locator('xpath=ancestor::form[1]');
        const formText = await form.innerText({ timeout: 500 }).catch(() => body);
        const method = formText.split('\n').map(normalize).find(line => magic.test(line));
        if (method) return { reason: method };
        await emailField.fill(email);
        const explicit = codeFlow.test(body) ? null : await action(page, signup, false);
        const proceed = explicit || await action(page, next, false);
        if (!proceed) return { reason: 'Кнопка продолжения регистрации не найдена' };
        const name = normalize(await proceed.innerText());
        // Generic email-only continuation can send a login link. Require a distinct code flow.
        if (!explicit && !codeFlow.test(formText) && !codeFlow.test(body)) {
          return { reason: `«${name}» — способ продолжения с email на форме не указан` };
        }
        if (expired) return { reason: 'Таймаут 40 с' };
        await proceed.click();
        await page.waitForTimeout(1700);
        const after = await page.locator('body').innerText({ timeout: 1800 });
        const created = after.split('\n').map(normalize).find(line => success.test(line));
        return created ? { reason: created, done: true } : {
          reason: await inspect(page) || 'Подтверждение создания аккаунта на странице не найдено',
        };
      }
      const signUp = await action(page, signup);
      const emailGateway = !await emailField.isVisible() && await action(page, /^continue with email$/i);
      const control = emailGateway || signUp || await action(page, gateway);
      if (!control) return { reason: 'Элемент регистрации на открытой странице не найден' };
      await control.click();
      const newTab = context.pages().at(-1);
      if (newTab !== page) {
        await page.close();
        page = newTab;
        page.setDefaultTimeout(3500);
      }
      registration ||= Boolean(signUp);
    }
    return { reason: 'Форма регистрации с email не открылась' };
  }

  let result;
  try {
    result = await Promise.race([
      run().catch(error => ({ reason: error.message.split('\n')[0].replace(/https?:\/\/\S+/gi, item.url) })),
      new Promise(resolve => { timer = setTimeout(() => {
        expired = true;
        resolve({ reason: 'Таймаут 40 с' });
      }, 37000); }),
    ]);
    const file = `signup-evidence/${item.id}.jpg`;
    try {
      await page.screenshot({ path: path.join(results, file), timeout: 2400, mask: [page.locator('input:visible'), page.getByText(email, { exact: false })] });
      shot = `[Снимок](${file})`;
    } catch (error) {
      shot = `Снимок недоступен (${error.name})`;
    }
  } finally {
    clearTimeout(timer);
    await context.close();
  }
  return { ...item, ...result, shot };
}

async function main() {
  const retry = new Set(process.argv.slice(2).map(Number));
  await fs.mkdir(path.join(results, 'signup-evidence'), { recursive: true });
  const brief = await fs.readFile(path.join(project, 'brief/brief.md'), 'utf8');
  const queue = [...brief.matchAll(/^\| (\d+) \| (.*?) \| (https?:\/\/[^\s|]+)/gm)]
    .map(([, id, service, url]) => ({ id: Number(id), service, url }));
  if (queue.length !== 72 || new Set(queue.map(item => item.id)).size !== 72) throw new Error('Ожидалось 72 уникальных позиции брифа');
  const pending = queue.filter(item => !confirmed.has(item.id) && !excluded.has(item.id) && (!retry.size || retry.has(item.id)));
  const output = [];
  const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true });
  try {
    await Promise.all(Array.from({ length: 4 }, async () => {
      while (pending.length) {
        const item = pending.shift();
        const skip = skips.get(item.id);
        const outcome = skip ? { ...item, reason: skip, shot: '[Бриф](../brief/brief.md)' } : await visit(browser, item);
        output.push(outcome);
        console.log(`${item.id} ${item.service} ${outcome.done ? 'OK' : 'STOP'}`);
      }
    }));
  } finally {
    await browser.close();
  }
  output.sort((a, b) => a.id - b.id);
  const header = '| Сервис | Причина или наблюдение | Доказательство |\n|---|---|---|\n';
  const rows = list => list.map(item => `| ${cell(item.service)} | ${cell(item.reason)} | ${item.shot} |`).join('\n');
  const failed = output.filter(item => !item.done);
  const done = output.filter(item => item.done);
  if (retry.size) {
    const failedPath = path.join(results, 'failed.md');
    const donePath = path.join(results, 'done.md');
    const previous = await fs.readFile(failedPath, 'utf8');
    const updatedByName = new Map(output.map(item => [cell(item.service), item]));
    const updated = previous.split('\n').flatMap(line => {
      const item = updatedByName.get(line.split(' | ')[0].slice(2));
      if (!item) return [line];
      return item.done ? [] : [rows([item])];
    });
    await fs.writeFile(failedPath, updated.join('\n'));
    if (done.length) {
      const previousDone = await fs.readFile(donePath, 'utf8');
      const empty = 'Новых подтверждённых регистраций нет.';
      const updatedDone = previousDone.includes(empty)
        ? previousDone.replace(empty, header + rows(done))
        : previousDone.trimEnd() + '\n' + rows(done) + '\n';
      await fs.writeFile(donePath, updatedDone);
    }
    return;
  }
  await fs.writeFile(path.join(results, 'failed.md'), '# Регистрация не завершена\n\nВерсия 1.0. Текст интерфейса приведён в строках со снимками. Диагностика браузера и наблюдения скрипта указаны, когда страница не показала причину. Ручные ограничения взяты из брифа.\n\n' + header + rows(failed) + '\n');
  await fs.writeFile(path.join(results, 'done.md'), '# Регистрации этого прогона\n\nВерсия 1.0.\n\n' + (done.length ? header + rows(done) : 'Новых подтверждённых регистраций нет.') + '\n');
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
