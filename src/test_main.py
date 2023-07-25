from currency_rates import currency_rates
import pytest
import os
import httpx

class Test():
    def test_example(self):
        code = 'USD'
        date = '2022-10-08'
        correct = 'USD (Доллар США): 61.2475'
        assert currency_rates(code, date) == correct

    def test_future(self):
        code = 'USD'
        date = '2024-26-08'
        with pytest.raises(ValueError):
            currency_rates(code, date)

    def test_uncorrect_code(self):
        code = 'ABCDQER'
        date = '2024-26-08'
        with pytest.raises(ValueError):
            currency_rates(code, date)
    
    def disable_network(self):
        os.environ['PYTEST_DISABLE_NETWORK']='1'
        code = 'USD'
        date = '2022-10-08'
        with pytest.raises(httpx.RequestError):
            currency_rates(code, date)


    # def test1(self):
    # def test1(self):
    # def test1(self):
