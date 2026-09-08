# Damavand Steel — Product Catalog Staging Manifest v1.0

## Purpose

This manifest records the product-candidate dataset used for the 2026-09-08 WordPress staging pass. It is a traceability artifact; it does not authorize publication and does not invent commercial values.

## Source fingerprint

- Source file: `Damavand_Product_Data_Collected_v0_1.xlsx`
- Source SHA-256: `a4d718a7d8e81f08794dbc0a5861ecfa104d06692df9386a9c24be35f1febf92`
- Source data rows: `130`
- Confirmed family-data rows: `3`
- Recovered candidate rows: `126`
- One row with incomplete exact size/type evidence: `1`

## Family counts

| Family | Source rows |
|---|---:|
| لوله استیل طلایی | 3 |
| زانو | 6 |
| نعلبکی | 12 |
| قیفی/ناخنی | 8 |
| گوی/ست گوی | 8 |
| رابط | 9 |
| حلقه/رینگ | 10 |
| درپوش | 17 |
| چاکدار ناخنی | 31 |
| کف‌کوب | 10 |
| آسانسوری | 16 |
| **Total** | **130** |

## WordPress staging policy

- All recovered product records were staged as `draft` records or equivalent non-public candidates.
- No price, SKU, stock quantity, sales unit, shipping length, supplier, or availability claim was fabricated.
- The confirmed gold stainless pipe family contains alloys `201 / 304`, sizes `16 / 38 / 51 mm`, thickness options `0.35 / 0.50 mm`, and `Gold` finish. Exact thickness-to-SKU mapping remains unconfirmed.
- Hybrid Commerce is the Founder-approved direction; purchase capability is represented in the runtime architecture, but a product is not publicly purchasable until required commercial truth exists.

## Cleanup performed during staging

Three duplicate ball records were identified and moved to WordPress Trash, preserving the earlier records:

- duplicate of `گوی استیل 70`: product `182`
- duplicate of `گوی استیل 80`: product `183`
- duplicate of `گوی کریستال 60`: product `184`

One missing source candidate was then added:

- `چاکدار ناخنی 2 تیکه 25 استیل`: product `282`

Five missing cap candidates were then added:

- `درپوش ABS 38 طلایی`: product `277`
- `درپوش ABS 38 مشکی`: product `278`
- `درپوش ABS 51 سیلور`: product `279`
- `درپوش ABS 51 طلایی`: product `280`
- `درپوش ABS 51 مشکی`: product `281`

## Commercial gate

The catalog is structurally staged, not sales-ready. Required fields before publication of a purchase SKU remain:

1. exact SKU identity
2. public price
3. real stock quantity or governed stock rule
4. sales unit
5. any required bar/pack length
6. exact variation mapping where applicable
7. payment and delivery readiness

Source evidence explicitly identifies these as required before online purchase activation.
