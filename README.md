# Automation API Testing

## How to Setup

### Configuration B.E

| Variable  | Description          | Default Value            |
| --------- | -------------------- | ------------------------ |
| `API_URL` | base API URL to test | `https//:sample.com/api` |

1. Create python venv

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## How to run the test

## activate path

```bash
export PYTHONPATH=$(pwd)
```

```bash
pytest
```
