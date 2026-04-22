[![CI/CD Pipeline](https://github.com/click2jay1/son_mro_optimizer/actions/workflows/test.yml/badge.svg)](https://github.com/click2jay1/son_mro_optimizer/actions/workflows/test.yml)

# SON MRO Optimizer - 4G/5G Network Optimization PoC

## Purpose
This Proof of Concept (PoC) demonstrates a **Self Organizing Network (SON)** use case called **Mobility Robustness Optimization (MRO)** for 4G/5G radio access networks. It simulates handover log analysis and suggests optimal handover thresholds.

## SON Use Case Covered
- **MRO (Mobility Robustness Optimization)**: Detect and correct:
  - Too-late handovers
  - Too-early handovers
  - Ping-pong handovers

## Technologies Used
- Python 3.9+
- Pandas (data analysis)
- Matplotlib (visualization)
- Pytest (testing)

## Folder Structure
son_mro_optimizer/
├── src/ # Source code
├── tests/ # Unit tests
├── data/ # Generated handover logs
├── output/ # Optimization reports
└── requirements.txt # Dependencies


## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Generate sample handover data
python src/generate_sample_data.py

3. Run MRO analysis
python src/mro_analyzer.py

4. Generate visualization
python src/visualizer.py

5. Run tests
pytest tests/ -v

Sample Output
=== MRO Analysis Report ===

Cell 101: Too-late handovers rate = High priority
  -> Increase TimeToTrigger (TTT) by 40ms

Optimization applied to 4 cells.
Expected handover failure reduction: ~30-40%


Author
Jay Raj Prakash — Created for Nokia Senior System Specification Engineer application

GitHub Repository
https://github.com/click2jay1/son_mro_optimizer

