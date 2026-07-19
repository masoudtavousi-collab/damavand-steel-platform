# Atlas Pipeline Architecture

## Workflow 01 — Master Controller
Node `Pipeline Configuration` با `execution_mode = OFFLINE`، `dry_run = true`، `founder_write_approved = false` و `credentials_configured = false` شروع می‌شود. `Resolve Execution Mode` مقدار ناموجود یا نامعتبر را به OFFLINE تبدیل می‌کند. OFFLINE و VALIDATE پیش از GitHub متوقف می‌شوند؛ DRY_RUN و LIVE می‌توانند Manifest را فقط از مسیر کنترل‌شده بخوانند و اسناد Pending را با Batch Size برابر 1 به Generator بفرستند.

## Workflow 02 — Document Generator
این Workflow نیز ExecutionMode را مستقل Resolve می‌کند؛ بنابراین اجرای مستقیم با Mode ناموجود Fail Closed و OFFLINE است. OFFLINE/VALIDATE پیش از Repository Read و OpenAI متوقف می‌شوند. DRY_RUN و LIVE می‌توانند Context را Read کنند، Prompt بسازند، مدل را فراخوانی و خروجی را Parse و Validate کنند.

Draft معتبر مستقیماً به GitHub نمی‌رود. Node مستقل `LIVE Remote Write Safety Gate` بلافاصله قبل از GitHub `PUT` قرار دارد و فقط با اجتماع پنج شرط دقیق مسیر Write را باز می‌کند: LIVE بودن Mode، خاموش‌بودن Dry Run، تأیید Founder، تأیید تنظیم Credentialها و Active بودن Workflow. DRY_RUN هرگز اجازه Write، Commit، Branch، PR، Publish یا Deploy نمی‌دهد.

## Workflow 03 — Repair Loop
ExecutionMode در ابتدای Workflow مستقل Resolve می‌شود. OFFLINE/VALIDATE پیش از OpenAI در خروجی Local Validation متوقف می‌شوند. DRY_RUN/LIVE می‌توانند OpenAI را فراخوانی کنند. خروجی مردود حداکثر سه بار اصلاح می‌شود و در صورت شکست برای بازبینی انسانی متوقف می‌شود؛ این Workflow هیچ GitHub Write ندارد.

## مدل چهارمرحله‌ای اجرا

| Mode | رفتار |
| --- | --- |
| `OFFLINE` | فقط Validation محلی؛ بدون Network، GitHub، OpenAI یا External API |
| `VALIDATE` | Validation محلی Manifest، Registry و Workflow؛ بدون External API |
| `DRY_RUN` | OpenAI و GitHub Read مجاز؛ تمام Remote Writeها ممنوع |
| `LIVE` | Write فقط پس از عبور هم‌زمان از تمام Gateهای Founder، Credential، Dry Run و Active State |

Mode ناموجود، malformed یا خارج از Enum همیشه OFFLINE است.

## وضعیت امنیتی
هیچ Workflow فعال نیست و هیچ Credential واقعی در فایل‌ها ذخیره نشده است. Workflowهای Importشده تا زمان تحقق همه شروط زیر نباید فعال شوند:

1. Credentialها از طریق n8n Credentials و با Least Privilege تنظیم شوند.
2. Repository، Branch، Pathها و Workflow IDها بازبینی شوند.
3. Dry-Run در محیط غیرتولیدی ثابت کند هیچ Remote Write انجام نمی‌شود.
4. Failure Pathها و حداکثر سه Repair Attempt بازبینی شوند.
5. Founder به‌صراحت Remote Write و سپس Activation را تأیید کند.

Dry Run حالت Offline نیست؛ Readهای GitHub و درخواست OpenAI قبل از Write Gate قرار دارند. هیچ عملیات Deployment یا Production در این معماری وجود ندارد یا مجاز نیست. جزئیات در `SAFETY_MODEL.md` آمده است.
