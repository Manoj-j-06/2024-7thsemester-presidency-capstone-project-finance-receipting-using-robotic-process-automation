# author : Manoj
# Main execution

from customer import Customer
from parser import parse_source_files

# source file path
source_file_path = 'D:\\7th-Sem-PROJECT\\CODE\\Python\\source_files'

#delimiter
delimiter = '$^#'

# c1 = Customer('Manoj','manoj@gmail.com','7996047060','Nagasandra','560073','P001','Laptop','2','25-10-2024 10:02','50000','UPI','2783746')

# Parse all the source files present in the directory
parse_source_files(source_file_path, delimiter)

