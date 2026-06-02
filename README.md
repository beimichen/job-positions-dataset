# Job Positions & Industries Dataset

An open dataset of **job positions, an industry taxonomy, and job-title
lookups**, plus a small toolkit for editing the data in spreadsheets and
converting it back to JSON.

Originally assembled to power a job-application assistant, the data is generic
and reusable for resume/cover-letter tooling, job-board categorization,
title normalization, autocomplete, and NLP experiments.

## What's in `data/`

| File | Rows / entries | Description |
|------|----------------|-------------|
| `positions.json` | **3,627 positions** | Per-position content keyed by title. Each entry has `body`, `intro`, `outro`, `parent_industry`, `sub_industry` — including ready-made cover-letter sentence templates. |
| `industries.json` | **30 industries** | Industry → sub-industry taxonomy. |
| `positions_lookup.csv` | ~22.9k | Flat position lookup list (good for autocomplete). |
| `job_titles_matched.csv` | ~79.3k | Raw job titles matched to canonical positions. |

### `positions.json` shape

```json
{
  "3d animator": {
    "intro": "...",
    "body": [ { "default_response": "...", "custom_text_response": "" } ],
    "outro": "...",
    "parent_industry": "...",
    "sub_industry": "..."
  }
}
```

## Tools (`tools/`)

| Script | Purpose |
|--------|---------|
| `excel_to_json.py` | Convert spreadsheet templates of positions into `positions.json`. Reads from `input/positions` and `input/templates`. |
| `json_to_excel.py` | Export positions back out to spreadsheets for hand-editing. |
| `validate_json.py` | Validate a JSON file against a schema. |
| `validate_csv.py`  | Sanity-check the lookup CSV for empty rows. |

Spreadsheet templates live in `templates/` (`.xlsx` and `.ods`).

> Note: the converters use repo-relative paths (`input/`, `data/`). Create an
> `input/` folder with your spreadsheets before running them.

## Install

```bash
pip install -r requirements.txt
```

## License

MIT — see [LICENSE](LICENSE). The dataset is provided as-is; verify suitability
before using generated text in production applications.
