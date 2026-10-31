# BOLT market price challenge — 30 October 2026

Actual seller pages show substantially lower **commodity reference prices** than the government's recorded $0.91/EA. This is a reason to investigate price formation. It is not yet a qualified overcharge comparison: the primary NSN-to-specification mapping is missing, and no seller has accepted a quote on the government's exact terms.

The inspected government order is **SPE4A627F0588**, 906 EA at $0.9100, total $824.46, against **SPE4A626D61WS**, NSN **5306016864912**. The order is evidence of a contracted rate, not evidence of completed delivery or payment. See [current observations](../current/observations.json).

## What the public price pages actually establish

Prices were observed on 30 October 2026. Dollar amounts are interpreted as USD from US merchant context; the opened product pages do not explicitly label an ISO currency. These are posted catalog amounts, not accepted procurement quotations.

| Seller and item | Posted price | Pack/tier and availability | Evidence limit |
|---|---:|---|---|
| [Fastener SuperStore 191377](https://www.fastenersuperstore.com/products/191377/hex-cap-screws) | $342.62/carton; displayed $0.31147/piece | 1,100/carton, 1–2 cartons. Item-specific stock quantity absent. | Best explicit pack normalization; government equivalence unproved. |
| [MF Supply HH38FX3/4G8ZY](https://www.mfsupply.com/product_p/hh38fx3-fslash-4g8zy.htm) | $328.91/box; displayed $0.29901/piece | 7 boxes displayed in stock; box count not explicitly rendered. | Do not infer 1,100/box from price or weight ratios. |
| [Cox HB8F38.34](https://aspdotnetstorefront.coxhardware.com/product/713/38-24-hex-bolts-grade-8) | $0.590/EA at 1–99; $0.413 at 100–499; $0.384 at 500+ | 62 EA shown available, 0 on order. | Header says **Cox Hardware Test Site**. Reference only; bulk 906-unit availability unproved. |

All three catalog products describe 3/8"-24 × 3/4" hex bolts/cap screws, Grade 8 steel, yellow zinc. These dimensions match a **secondary** description of the target NSN. They do not yet establish that the catalog products satisfy that NSN. MF lists ASME B18.2.1 and SAE J429. Fastener SuperStore additionally specifies full thread and 9/16" width across flats; its generic linked style sheet references ASME B18.2.1-2012.

The SuperStore's 1,100-unit carton is 194 units larger than the inspected government order. Its lower $0.29315 and $0.27686 displayed piece rates require 3–4 or 5+ cartons, respectively; those must not be applied to a 906-unit order. Only carton-price ÷ carton-count arithmetic was normalized in the machine-readable matrix. No premium, loss or kickback amount was computed.

SuperStore identifies a Kanebridge 3812CH8O cross-reference. MF lists 3812CH8O as well. These are separate sellers, but their upstream product/source independence is unproved; two websites must not be counted as two independent manufacturers.

## The specification gap is material

The selected original [DLA parent page 5](../current/snapshots/parent-page5.txt) identifies the NSN, a non-government standard reference to **ASME B18.24**, and a blank part-piece-number field. It does not itself prove 3/8-24 × 3/4, Grade 8, yellow zinc, or that Kanebridge 3812CH8O is an accepted equivalent.

The official catalog route was investigated within a bounded search; all 5 opened DLA overview/training/brochure pages returned 403. No exact official NSN characteristics/reference record was acquired. A standard-number reference is not an approved-manufacturer crosswalk. Secondary “zinc” also does not establish yellow chromate, coating thickness or other finish requirements. See [SPEC-NOTE](SPEC-NOTE.md) and [spec-crosswalk.json](spec-crosswalk.json).

## Conditions that change the effective price

The DLA order is FOB origin with government freight payment. The parent calls for QUP 001, destination inspection/acceptance, bare marking and specified sampling/quality provisions. These requirements need an actual cost and compliance reconciliation; do not assume they either explain or fail to explain the entire difference.

[SuperStore's terms](https://www.fastenersuperstore.com/terms) use FOB seller warehouses. Its [FAQ](https://www.fastenersuperstore.com/faq) says freight varies with weight and destination, bulk quantities are standard, and smaller broken cartons require inquiry. Its general availability and usual delivery statements do not guarantee this SKU.

[MF's terms](https://www.mfsupply.com/terms.php) make acceptance and price correction explicit. Certification, inspection, testing, documentation and quality requirements need written agreement; they cannot be assumed included in the headline price. [Its general shipping policy](https://www.mfsupply.com/Articles.php?ID=287) describes dispatch in 1–2 days for online US orders, not a binding delivery promise for this purchase.

No comparable historical seller quotation at the 17 September 2026 parent award date was obtained. A 30 October listing is a current lead, not proof of what was offered or available then.

## What would test the user's 12% mechanism

The user's example directs a separate hypothesis: a real supplier may charge an avoidable premium while a buyer receives an undisclosed benefit. Company existence, correct invoice multiplication and an ordinary-looking contract do not resolve that question.

The next useful evidence is an exact-spec, same-date cost bridge: supplier quote → purchaser order → supplier invoice → receiving record → government billing/payment → credits/rebates. It should identify approval changes, competing quotes and any documented fees. For repeated purchases, test whether a residual proportional premium persists after item, pack, volume, delivery and compliance differences are reconciled. A 12% pattern can prioritize review; it does not establish a kickback.

Personal benefit or buyer–supplier collusion would require independently corroborated evidence of the relationship or benefit. No such evidence was found here. No actor is accused, no private payment trail was accessed, and no catalog seller was linked to the government's actual supply chain.

## Exclusions and reproducibility

Bolt Depot and Fasteners Direct showed potentially useful prices in search results, but the opened pages failed. They are excluded from verified prices. The opened Menards page contained navigation only; its search-only rebate was also dated before this review. No search snippet has been promoted to a verified offer.

This package contains [benchmark_matrix.json](benchmark_matrix.json), [sources.json](sources.json), [query_log.json](query_log.json) and selected structured fact captures. Capture hashes identify the retained extracts, **not original website bytes**. Three merchant references were obtained; two are viable provisional catalog offers, and the Cox test-site reference is explicitly downgraded. **Qualified procurement comparators: 0. Established overcharge: undetermined. Evidence of kickback: not found in this bounded review.**
