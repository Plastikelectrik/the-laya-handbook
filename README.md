# The LAYA Handbook — Code Examples

Source code for the code examples in **The LAYA Handbook** by Oscar Gómez Fernández, published by Packt.

The examples are organized by chapter and numbered in the order they appear in the book, so you can follow along section by section. Each file starts with a header naming the chapter and section it comes from.

## Requirements

- Python 3.9 or later
- The `laya` package, version pinned to the release this book targets:

```bash
python -m venv laya-env
source laya-env/bin/activate        # Windows: laya-env\Scripts\activate
pip install -r requirements.txt
```

The first call to `laya.load("convaiinnovations/laya")` downloads the model checkpoint from Hugging Face and caches it locally; after that, everything runs offline.

## Repository structure

| Folder | Chapter | Files |
|---|---|---|
| [`chapter_03/`](chapter_03/) | Chapter 3: Installing Laya: pip, Hugging Face Checkpoints, and Apache 2.0 | 7 |
| [`chapter_04/`](chapter_04/) | Chapter 4: Your First Prediction: agent.predict() End to End | 5 |
| [`chapter_05/`](chapter_05/) | Chapter 5: The State Object: Giving Laya Something to Reason About | 3 |
| [`chapter_06/`](chapter_06/) | Chapter 6: Choice: Calibrated Classification in One Forward Pass | 2 |
| [`chapter_07/`](chapter_07/) | Chapter 7: Score: Ordinal Judgments on a Rubric | 3 |
| [`chapter_08/`](chapter_08/) | Chapter 8: Noul: Calibrated Yes/No Questions | 3 |
| [`chapter_09/`](chapter_09/) | Chapter 9: Asking Several Questions at Once: Shared Encoding, Independent Answers | 3 |
| [`chapter_10/`](chapter_10/) | Chapter 10: Understanding Calibration: What a Probability From Laya Actually Means | 1 |
| [`chapter_11/`](chapter_11/) | Chapter 11: The Router: Automatic Model Selection and Multilingual Text | 7 |
| [`chapter_12/`](chapter_12/) | Chapter 12: Writing Criteria That Produce Calibrated Answers, and a First End-to-End Example | 2 |
| [`chapter_14/`](chapter_14/) | Chapter 14: Production Architecture and the Router(preload=True) Pattern | 5 |
| [`chapter_15/`](chapter_15/) | Chapter 15: Batched Prediction at Scale | 3 |
| [`chapter_16/`](chapter_16/) | Chapter 16: Confidence Gating and the Escalation Pattern | 4 |
| [`chapter_17/`](chapter_17/) | Chapter 17: Designing Production Criteria: The Department, Urgency, and Churn Model | 4 |
| [`chapter_18/`](chapter_18/) | Chapter 18: Golden-Set Testing Discipline | 4 |
| [`chapter_19/`](chapter_19/) | Chapter 19: Calibration Drift: Detecting When Confidence Stops Meaning What It Used To | 2 |
| [`chapter_20/`](chapter_20/) | Chapter 20: Degraded-Mode Design: What Happens When Inference Fails | 4 |
| [`chapter_21/`](chapter_21/) | Chapter 21: Multi-Tenant and Team Threshold Governance | 3 |
| [`chapter_22/`](chapter_22/) | Chapter 22: Cost Modeling: Laya vs. Rules vs. LLM Calls | 1 |
| [`chapter_23/`](chapter_23/) | Chapter 23: Security and Reliability for a Self-Hosted Model | 1 |
| [`chapter_25/`](chapter_25/) | Chapter 25: Scaling Beyond a Single Checkpoint: Hierarchical and High-Cardinality Routing | 2 |
| [`chapter_26/`](chapter_26/) | Chapter 26: Observability: Logging, Auditing, and Dashboards for Decision Systems | 3 |
| [`chapter_27/`](chapter_27/) | Chapter 27: Capstone Part 1: Designing the Ticket-Routing Pipeline | 1 |
| [`chapter_28/`](chapter_28/) | Chapter 28: Capstone Part 2: Building, Testing, and Deploying the Pipeline | 6 |
| [`chapter_29/`](chapter_29/) | Chapter 29: Deployment and Monitoring in Practice | 1 |
| [`chapter_31/`](chapter_31/) | Chapter 31: Laya Alongside LLMs: Where System 1 Fits in a Larger System | 1 |
| [`appendix_a/`](appendix_a/) | Appendix A: API and Primitive Quick Reference | 20 |
| [`appendix_c/`](appendix_c/) | Appendix C: Capstone Full Source Listing | 1 |
| [`appendix_d/`](appendix_d/) | Appendix D: Golden-Set Example Bank | 4 |
| [`appendix_e/`](appendix_e/) | Appendix E: Worked Case Studies | 3 |

Chapters 1, 2, 13, 24 and 30, Appendix B (Troubleshooting Index) and Appendix F (FAQ) contain no code listings.

## How to use these examples

- **Most files are excerpts.** As in the book, many listings build on names defined in earlier sections or chapters (for example `agent`, `state`, `TICKET_QUESTIONS`, `router`) or call application-specific helpers you provide yourself (such as `escalate_to_human()` or `audit_log`). Read them alongside the chapter.
- **Complete examples:**
  - `chapter_12/01_complete_working_classifier.py` — a complete, self-contained ticket classifier you can run directly (`python chapter_12/01_complete_working_classifier.py`).
  - `appendix_c/capstone_pipeline.py` — the full capstone ticket-routing pipeline from Chapters 27–28 in a single file. It still expects a few integration points from your own system (`audit_log`, `InferenceError`, `effective_threshold()` from Chapter 21, the golden-set evaluation from Chapter 18).
- `appendix_d/` contains the golden-set example bank as Python lists you can import into your own evaluation harness.
- Files marked with *"excerpt of dictionary entries"* show only a few entries of a larger dictionary and are not runnable on their own.

## License

The code in this repository is released under the [MIT License](LICENSE).

This license applies only to the source code and code examples. The text, illustrations and other content of the book are not covered by it.
