# Two further historical award routes

This lane attempted original documents for SPE4A626P5931 (14 November 2025) and SPE4A625PK654 (24 March 2025), using their exact identifiers and dates already recorded in official award captures. The download paths were derived from a previously observed DIBBS convention; they were not links acquired from those awards' own pages.

Four opener operations were performed: two GETs and two acknowledgments of the ordinary public DoD notice. The first route timed out during notice submission; the second returned HTML rather than a PDF. **No historical original PDF was acquired.** These outcomes cannot establish that either award, document or payment is absent, nor that anything was concealed.

Two later web-tool opens of the corresponding public award-record paths also returned inaccessible responses. Those are separately recorded in [additional-route-checks.json](additional-route-checks.json); they are not successful acquisitions. Opener counts do not separately count automatic redirect hops and must not be described as a complete HTTP trace.

The [acquisition receipt](acquisition.json) preserves outcomes, original route derivation, times and the notice-parser code hash. [acquire_history.py](acquire_history.py) is a bounded reproduction helper; its default run is two exact routes, at most four opener operations and five megabytes per response. After independent review, the helper enforces a fresh raw-source directory outside this repository and uses exclusive creation for complete PDFs; it also refuses an existing receipt. The retained run preceded this hardening and acquired no PDF, so no source was overwritten or published. Hidden notice values and cookies are not retained. No account login or external contact was attempted.

The earlier seven-row history and exact official award joins remain intact. Historical CLIN units, quantities and applicable terms are still not authenticated by these failed requests. The separate bids lane attempted the highest-price and latest historical routes and retains its own failures.
