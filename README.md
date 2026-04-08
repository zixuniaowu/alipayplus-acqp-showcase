---
title: Alipay+ ACQP Integration Report
emoji: 💳
colorFrom: blue
colorTo: indigo
sdk: static
app_file: index.html
fullWidth: true
header: mini
short_description: Trilingual Alipay+ ACQP integration report with diagrams and implementation guidance.
---

# Alipay+ ACQP Integration Report

This repository publishes a static report for Alipay+ ACQP integration.

- Homepage entry: `index.html`
- Main report: `report/alipayplus-integration-report.html`
- Assets: `report/diagrams/` and `report/official-samples/`

## Local preview

Open:

- `index.html`
- or `report/alipayplus-integration-report.html`

## Hugging Face Space

This repository is configured for a **Static HTML Space**. The report is exposed as the Space homepage through `index.html`, which redirects to the full report.

If you want to publish from this machine, set one of these environment variables first:

- `HF_TOKEN`
- `HUGGINGFACEHUB_API_TOKEN`
- `HUGGINGFACE_TOKEN`

Then run:

```powershell
python scripts/publish_hf_space.py --repo-id <your-hf-username>/<space-name>
```
