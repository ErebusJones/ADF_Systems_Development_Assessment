from datetime import datetime
from datecalc import when


#test simple 10 day addition
def test_simple_addition():
    
    #Arrange
    start_date = datetime(2022,8,15)
    days_between = 10
    
    #Act
    expected_date = when(start_date, days_between)
    
    #Assert
    assert expected_date == datetime(2022,8,25)


#test leap year addition
def test_leap_year_addition():
    
    #Arrange
    start_date = datetime(2024,2,1)
    days_between = 29
    
    #Act
    expected_date = when(start_date, days_between)
    
    #Assert
    assert expected_date == datetime(2024,3,1)


#test non leap year addition
def test_non_leap_year_addition():
    
    #Arrange
    start_date = datetime(2023,2,1)
    days_between = 28
    
    #Act
    expected_date = when(start_date, days_between)
    
    #Assert
    assert expected_date == datetime(2023,3,1)


#test extreme value
def test_extreme_value():
    
    #Arrange
    start_date = datetime(1,1,1)
    days_between = 3652058
    
    #Act
    expected_date = when(start_date, days_between)
    
    #Assert
    assert expected_date == datetime(9999,12,31)