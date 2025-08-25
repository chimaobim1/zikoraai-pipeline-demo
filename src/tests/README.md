# ZikoraAI Pipeline Demo

A safe, redacted demonstration of the data pipeline stages on toy data: ingestion, preprocessing, feature engineering, storage, and serving.

![CI](https://github.com/chimaobim1/zikoraai-pipeline-demo/actions/workflows/ci.yml/badge.svg)
![Coverage](./coverage.svg)

## Quick start
```bash
python -m venv .venv
# macOS or Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
