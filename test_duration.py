from datetime import datetime
from datecalc import duration


#test simple week date gap
def test_basic_gap():
    
    #Arrange
    start_date = datetime(2022,8,15)
    end_date = datetime(2022,8,22)
    
    #Act
    diff = duration(start_date, end_date)
    
    #Assert
    assert diff == 7


#test leap year february
def test_leap_year():
    
    #Arrange
    start_date = datetime(2024,2,1)
    end_date = datetime(2024,3,1)
    
    #Act
    diff = duration(start_date, end_date)
    
    #Assert
    assert diff == 29


#test non leap year february
def test_non_leap_year():
    
    #Arrange
    start_date = datetime(2023,2,1)
    end_date = datetime(2023,3,1)
    
    #Act
    diff = duration(start_date, end_date)
    
    #Assert
    assert diff == 28


#test negative dates
def test_negative_dates():
    
    #Arrange
    start_date = datetime(2022,8,19)
    end_date = datetime(2022,8,18)
    
    #Act
    diff = duration(start_date, end_date)
    
    #Assert
    assert diff == 1


#test out of bounds
def test_out_of_bounds():
    
    #Arrange
    start_date = datetime(2033,8,15)
    end_date = datetime(2033,8,22)
    
    #Act
    diff = duration(start_date, end_date)
    
    #Assert
    assert diff == 7