
from utilities import read_utils

Product_choose = [
    ("Proteus Fitness Jackshirt","M"),
    ("kim", "kim123", "Invalid credentials")
]
test_valid_login_data = read_utils.get_csv_as_list("../test_data/test_valid_login_data.csv")
login_data_invalid = read_utils.get_sheet_as_list("../test_data/Data_magento.xlsx","Invalid_login_test")
product_names= read_utils.get_sheet_as_list("../test_data/Data_magento.xlsx","Products")
Create_account= read_utils.get_sheet_as_list("../test_data/Data_magento.xlsx","create_account")