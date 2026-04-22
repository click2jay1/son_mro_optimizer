import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from mro_analyzer import MROAnalyzer
import pandas as pd
import tempfile

class TestMROAnalyzer:
    
    def test_failure_rate_calculation(self):
        test_data = pd.DataFrame({
            'source_eNB': [101, 101, 101, 102, 102],
            'target_eNB': [102, 103, 104, 101, 103],
            'handover_type': ['too_late', 'normal', 'too_late', 'ping_pong', 'normal']
        })
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_data.to_csv(f.name, index=False)
            temp_path = f.name
        
        analyzer = MROAnalyzer(temp_path)
        rates = analyzer.calculate_failure_rates()
        
        assert rates[101]['too_late_rate'] == 2/3
        assert rates[101]['total'] == 3
        assert rates[102]['ping_pong_rate'] == 0.5
        
        os.unlink(temp_path)
    
    def test_recommendations_for_too_late(self):
        test_data = pd.DataFrame({
            'source_eNB': [101, 101, 101, 101],
            'target_eNB': [102, 102, 102, 102],
            'handover_type': ['too_late', 'too_late', 'too_late', 'normal']
        })
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_data.to_csv(f.name, index=False)
            temp_path = f.name
        
        analyzer = MROAnalyzer(temp_path)
        rates = analyzer.calculate_failure_rates()
        recommendations = analyzer.recommend_optimizations(rates)
        
        assert len(recommendations) > 0
        assert recommendations[0]['issue'] == 'Too-late handovers'
        
        os.unlink(temp_path)
    
    def test_no_recommendations_for_healthy_network(self):
        test_data = pd.DataFrame({
            'source_eNB': [101, 101, 101, 102, 102],
            'target_eNB': [102, 103, 104, 101, 103],
            'handover_type': ['normal', 'normal', 'normal', 'normal', 'normal']
        })
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_data.to_csv(f.name, index=False)
            temp_path = f.name
        
        analyzer = MROAnalyzer(temp_path)
        rates = analyzer.calculate_failure_rates()
        recommendations = analyzer.recommend_optimizations(rates)
        
        assert len(recommendations) == 0
        
        os.unlink(temp_path)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
