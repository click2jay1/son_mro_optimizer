import pandas as pd
import random
from datetime import datetime, timedelta

def generate_handover_logs(num_records=500):
    cells = [101, 102, 103, 104, 105]
    ho_types = ['normal', 'too_late', 'too_early', 'ping_pong']
    weights = [0.7, 0.12, 0.1, 0.08]
    
    data = []
    start_time = datetime(2025, 4, 1, 0, 0, 0)
    
    for i in range(num_records):
        source_cell = random.choice(cells)
        target_cell = random.choice([c for c in cells if c != source_cell])
        ho_type = random.choices(ho_types, weights=weights)[0]
        timestamp = start_time + timedelta(seconds=random.randint(0, 86400))
        
        data.append({
            'timestamp': timestamp,
            'source_eNB': source_cell,
            'target_eNB': target_cell,
            'handover_type': ho_type,
            'rlf_after_ms': random.randint(10, 5000) if ho_type != 'normal' else None
        })
    
    df = pd.DataFrame(data)
    df.to_csv('data/handover_sample_logs.csv', index=False)
    print(f"Generated {num_records} handover logs at data/handover_sample_logs.csv")

if __name__ == "__main__":
    generate_handover_logs()
