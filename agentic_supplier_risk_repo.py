# Folder structure for the Agentic Supplier Risk & Sourcing project

# agentic-supplier-risk/
# ├── README.md
# ├── docker-compose.yml
# ├── requirements.txt
# ├── ml/
# │   ├── __init__.py
# │   ├── train_risk_model.py
# │   └── models/
# │       ├── __init__.py
# │       └── baseline_model.py
# ├── services/
# │   ├── __init__.py
# │   ├── ingest/
# │   │   ├── __init__.py
# │   │   └── kafka_consumer.py
# │   ├── orchestrator/
# │   │   ├── __init__.py
# │   │   └── agent_core.py
# │   ├── executor/
# │   │   ├── __init__.py
# │   │   └── action_executor.py
# │   └── simulator/
# │       ├── __init__.py
# │       └── generate_events.py
# ├── frontend/
# │   ├── package.json
# │   ├── src/
# │   │   ├── App.js
# │   │   ├── index.js
# │   │   └── components/
# │   │       └── SupplierDashboard.js
# ├── infra/
# │   ├── docker-compose.yml
# │   └── k8s/
# │       └── deployment.yaml
# ├── docs/
# │   ├── architecture.md
# │   └── data_dictionary.md
# └── .github/
#     └── workflows/
#         └── ci.yml

# Below are the starter contents for key files:

### README.md
"""md
# Agentic Supplier Risk & Sourcing (ASRS)

Autonomous AI system for supplier risk monitoring and sourcing recommendations.

## Components
- **ml/**: Risk scoring models (baseline + GNN)
- **services/**: Agentic services (ingestion, orchestrator, executor)
- **frontend/**: React dashboard for visualization
- **infra/**: Deployment configuration

## Quickstart
```bash
git clone https://github.com/<your-username>/agentic-supplier-risk.git
cd agentic-supplier-risk
pip install -r requirements.txt
python services/simulator/generate_events.py
```

Then open [http://localhost:3000](http://localhost:3000).
"""

### ml/train_risk_model.py
"""python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Placeholder: load supplier data
def train():
    data = pd.DataFrame({
        'on_time_rate': [0.9, 0.6, 0.8],
        'defect_rate': [0.01, 0.05, 0.02],
        'label': [0, 1, 0]
    })

    X = data[['on_time_rate', 'defect_rate']]
    y = data['label']
    model = RandomForestClassifier().fit(X, y)
    print('Model trained successfully!')

if __name__ == '__main__':
    train()
"""

### services/orchestrator/agent_core.py
"""python
import json

def evaluate_risk(supplier_score):
    if supplier_score > 0.8:
        return {"action": "start_rfq", "priority": "high"}
    return {"action": "monitor", "priority": "low"}

if __name__ == '__main__':
    print(json.dumps(evaluate_risk(0.9), indent=2))
"""

### services/simulator/generate_events.py
"""python
import random, json

SUPPLIERS = ['S1', 'S2', 'S3']
EVENTS = ['on_time', 'delay', 'quality_issue']

def generate_event():
    event = {
        'supplier_id': random.choice(SUPPLIERS),
        'event': random.choice(EVENTS),
        'risk_score': round(random.random(), 2)
    }
    print(json.dumps(event))

if __name__ == '__main__':
    for _ in range(5):
        generate_event()
"""

### .github/workflows/ci.yml
"""yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          pip install -r requirements.txt
      - name: Run simulator test
        run: |
          python services/simulator/generate_events.py
"""
