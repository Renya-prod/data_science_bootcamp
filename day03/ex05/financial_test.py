#!/usr/bin/env python3
import pytest
import sys
import os
sys.path.append(os.path.abspath("../ex03"))
from financial import fetch_financial_data

def test_valid_ticker_and_field():
    """
    Тестируем функцию на корректный тикер и поле.
    """
    ticker = "MSFT"
    field = "Total Revenue"
    result = fetch_financial_data(ticker, field)
    
    assert result, "Результат не должен быть пустым"
    
    assert field.lower() in result[0].lower(), "Поле Total Revenue не найдено в результате"

def test_return_type():
    """
    Проверяем, что функция возвращает кортеж.
    """
    ticker = "MSFT"
    field = "Total Revenue"
    result = fetch_financial_data(ticker, field)
    
    assert isinstance(result, tuple), "Результат должен быть кортежем"

def test_invalid_ticker():
    """
    Проверяем, что функция выбрасывает исключение при некорректном тикере.
    """
    ticker = "INVALID_TICKER"
    field = "Total Revenue"
    
    with pytest.raises(Exception, match=r"(?i)^Financial data for ticker 'invalid_ticker' not found\.$"):
        fetch_financial_data(ticker, field)


def test_invalid_field():
    """
    Проверяем, что функция выбрасывает исключение при некорректном поле.
    """
    ticker = "MSFT"
    field = "Invalid Field"
    
    with pytest.raises(Exception, match=r"(?i)^Field 'Invalid Field' not found for ticker 'msft'\.$"):
        fetch_financial_data(ticker, field)
