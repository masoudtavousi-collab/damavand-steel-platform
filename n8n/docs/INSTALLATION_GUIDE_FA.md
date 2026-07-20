# راهنمای نصب Pipeline اطلس در n8n

> **وضعیت ایمنی: NO-GO.** Workflowهای واردشده باید غیرفعال بمانند. Import یا Validation موفق، مجوز اجرا، فعال‌سازی، نوشتن در GitHub، انتشار یا Deployment نیست.

## پیش‌نیازها

1. فقط از Repository خصوصی و غیرتولیدی تأییدشده برای تست استفاده کنید.
2. Mirror اجرایی Manifest را در مسیر دقیق `n8n/config/ATLAS_MASTER_MANIFEST.json` نگه دارید؛ آن را به مسیر دیگری کپی نکنید.
3. وجود و محتوای `PROJECT_BIBLE.md`، `AGENTS.md` و منابع Governance اجباری را در Repository بررسی کنید.
4. یک Branch با نام `atlas-drafts` ایجاد کنید.
5. Credentialهای GitHub و OpenAI را فقط در بخش **n8n Credentials** و با کمترین سطح دسترسی لازم تعریف کنید؛ هیچ مقدار واقعی را داخل JSON یا فایل Repository قرار ندهید.
6. برای تست از Repository و Branch جدا، محدود و غیرتولیدی استفاده کنید.

## واردکردن Workflowها

به‌ترتیب وارد کنید:

1. `WF-03_REPAIR_LOOP.json`
2. `WF-02_DOCUMENT_GENERATOR.json`
3. `WF-01_ATLAS_MASTER_CONTROLLER.json`

پس از Import، شناسه Workflow دوم را در Node «Pipeline Configuration» از Workflow اصلی وارد کنید.

## تنظیمات ضروری

در `Pipeline Configuration` این موارد را تغییر دهید:

- `github_owner`
- `github_repo`
- `branch`
- `expected_repository`
- `expected_branch`
- `manifest_path` با مقدار دقیق `n8n/config/ATLAS_MASTER_MANIFEST.json`
- `schema_path` با مقدار دقیق `atlas/DOCUMENT_OUTPUT_SCHEMA.json`
- `template_path` با مقدار دقیق `atlas/DOCUMENT_TEMPLATE.md`
- `required_governance_paths`
- `generator_workflow_id`

چهار Mode مجاز عبارت‌اند از:

- `OFFLINE`: بدون Network، GitHub، OpenAI یا External API؛ مقدار پیش‌فرض.
- `VALIDATE`: فقط Validation محلی Manifest، Registry و Workflow؛ بدون External API.
- `DRY_RUN`: OpenAI و GitHub Read مجاز، ولی هر نوع GitHub Write، Commit، Branch، PR، Publish و Deploy ممنوع.
- `LIVE`: تنها Mode بالقوه برای GitHub Write و فقط پس از عبور از تمام Gateها.

Mode ناموجود، خالی، malformed یا با حروف متفاوت به OFFLINE تبدیل می‌شود.

در شروع و تمام تست‌های ایمنی، این مقادیر باید بدون تغییر بمانند:

- `dry_run = true`
- `founder_write_approved = false`
- `execution_mode = OFFLINE`
- `credentials_configured = false`

GitHub Write فقط با اجتماع همه شروط دقیق زیر ممکن است: `execution_mode === LIVE`، `dry_run === false`، `founder_write_approved === true`، `credentials_configured === true` و Active بودن Workflow. مقدار خالی، ناموجود، متنی یا malformed به‌صورت Fail Closed تفسیر می‌شود. فایل‌های Importشده Active نیستند.

## نکته امنیتی

فایل‌های Import فقط نام Environment Variable را به‌عنوان Placeholder نشان می‌دهند و Credential واقعی ندارند. پیش از هر تست دستی یا فعال‌سازی، Headerهای احراز هویت باید به **n8n Credentials** منتقل و Scope، Repository، Branch و سطح دسترسی آن‌ها بازبینی شود.

Workflowها نباید فعال شوند مگر آنکه همه موارد زیر انجام شده باشد:

1. Credentialها با Least Privilege در n8n Credentials تنظیم شده باشند.
2. مقادیر Repository، Branch، Path و Workflow ID بازبینی شده باشند.
3. Validation در OFFLINE/VALIDATE بدون Network پاس شده باشد.
4. تست DRY_RUN در محیط غیرتولیدی با موفقیت ثابت کرده باشد که هیچ Write انجام نمی‌شود.
5. Founder به‌طور صریح Remote Write را تأیید کرده باشد.
6. فعال‌سازی نیز به‌عنوان Gate جداگانه تأیید شده باشد.

## اولین تست

1. Workflowها را غیرفعال نگه دارید و در Modeهای OFFLINE/VALIDATE فرمان `python3 scripts/validate_manifest.py` را اجرا کنید.
2. تأیید کنید Network Violation و ExecutionMode Policy Error برابر صفر است.
3. فقط در n8n و Repository آزمایشی و غیرتولیدی، یک سند کنترل‌شده را روی `pending` نگه دارید و صحت Repository، Branch، Manifest SHA، Registry Path، Schema، Template و Context اجباری را ثبت کنید.
4. پس از تنظیم Credentialهای Read-Only، `execution_mode = DRY_RUN`، `dry_run = true` و `founder_write_approved = false` را نگه دارید و یک اجرای دستی محدود انجام دهید.
5. خروجی باید `status = dry_run_blocked_write` و `write_performed = false` باشد و GitHub نباید تغییری کرده باشد.
6. LIVE، خاموش‌کردن Dry Run، تأیید Founder، تأیید Credential و فعال‌سازی هرکدام Gate صریح و قابل‌ردیابی می‌خواهند.

## محدودیت نسخه 1.0

- اتصال Repair Loop به Generator عمداً خودکار نشده است؛ هر Attempt باید جداگانه با عدد صحیح 1 تا 3 و Context معتبر فراخوانی شود.
- به‌روزرسانی Status داخل Manifest در نسخه بعدی اضافه می‌شود.
- Founder Approval یک فیلد صریح Fail-Closed است، اما هنوز به کانال اعلان، هویت‌سنجی یا فرم تأیید متصل نشده است.
- Dry Run مانع GitHub Write می‌شود، ولی Readهای GitHub و درخواست OpenAI پیش از Gate را متوقف نمی‌کند.
- جزئیات کامل در `SAFETY_MODEL.md` ثبت شده است.
