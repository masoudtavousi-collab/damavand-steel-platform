# Atlas Pipeline Architecture

## Workflow 01 — Master Controller
Node `Pipeline Configuration` با `execution_mode = OFFLINE`، `dry_run = true`، `founder_write_approved = false` و `credentials_configured = false` شروع می‌شود. مسیر پیش‌فرض Manifest برابر `n8n/config/ATLAS_MASTER_MANIFEST.json` است. `Resolve Execution Mode` مقدار ناموجود یا نامعتبر را به OFFLINE تبدیل می‌کند. پیش از اولین Read، هویت Repository و Branch، مسیر Manifest، Schema، Template و فهرست Governance مستقل اعتبارسنجی می‌شود. OFFLINE و VALIDATE پیش از GitHub متوقف می‌شوند؛ DRY_RUN و LIVE فقط پس از این کنترل‌ها می‌توانند Manifest را بخوانند و اسناد Pending را با Batch Size برابر 1 به Generator بفرستند.

## Workflow 02 — Document Generator
این Workflow نیز ExecutionMode را مستقل Resolve می‌کند؛ بنابراین اجرای مستقیم با Mode ناموجود Fail Closed و OFFLINE است. OFFLINE/VALIDATE پیش از Repository Read و OpenAI متوقف می‌شوند. در DRY_RUN/LIVE، Manifest دوباره از مسیر Canonical خوانده و با SHA و Version مورد انتظار تطبیق داده می‌شود. شناسه سند از Registry داخل Manifest به Path واقعی Resolve می‌شود؛ Dependencyها از همان Registry به Path Canonical نگاشت می‌شوند. `PROJECT_BIBLE.md`، `AGENTS.md`، منابع Governance اعلام‌شده، Schema و Template همگی Context اجباری هستند. خطای Read، محتوای خالی، شناسه یا Path نادرست، Dependency ناشناخته، Repository یا Branch ناسازگار اجرای Generation را با خطای صریح متوقف می‌کند.

خروجی OpenAI یک Object ساختاریافته مطابق `atlas/DOCUMENT_OUTPUT_SCHEMA.json` است، نه Markdown. Propertyهای ناشناخته، `sections` ناقص یا malformed، محتوای خالی، نسخه Schema نادرست، هویت سند نادرست و Dependency ناسازگار رد می‌شوند. تنها پس از عبور کامل از این Validation، `atlas/DOCUMENT_TEMPLATE.md` به‌صورت Deterministic به Markdown تبدیل می‌شود.

Draft معتبر مستقیماً به GitHub نمی‌رود. Node مستقل `LIVE Remote Write Safety Gate` بلافاصله قبل از GitHub `PUT` قرار دارد و فقط با اجتماع پنج شرط دقیق مسیر Write را باز می‌کند: LIVE بودن Mode، خاموش‌بودن Dry Run، تأیید Founder، تأیید تنظیم Credentialها و Active بودن Workflow. DRY_RUN هرگز اجازه Write، Commit، Branch، PR، Publish یا Deploy نمی‌دهد.

## Workflow 03 — Repair Loop
ExecutionMode در ابتدای Workflow مستقل Resolve می‌شود. OFFLINE/VALIDATE پیش از OpenAI در خروجی Local Validation متوقف می‌شوند. DRY_RUN/LIVE فقط با Context، Schema، Template، Registry Entry و Attempt معتبر می‌توانند OpenAI را فراخوانی کنند. Attempt باید عدد صحیح 1 تا 3 باشد؛ مقدار خالی، منفی، غیرعددی یا بیشتر از 3 Fail Closed است. این Workflow به Generator به‌صورت خودکار متصل نیست و هر Invocation جداگانه و کنترل‌شده است. خروجی Repair باید همان Contract ساختاریافته را پاس کند و سپس به‌صورت Deterministic Render شود؛ هیچ GitHub Write ندارد.

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
