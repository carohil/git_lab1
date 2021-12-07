import pandas as pd

def validate_phone(phone_number):    
    """ Ensure that phone numbers are valid        

    Arguments:        
        phone_number: A pandas series of phone numbers        
    
    Return:        
        boolean pandas series.  True means valid. False means invalid.    
    """    
    bool_phone = phone_number.str.contains("^[0-9]{3}-[0-9]{3}-[0-9]{4}")    
    return bool_phone
    

numbers = pd.Series(['574-252-6263', '574-631-7770', '$12.99'])
print(validate_phone(numbers))
