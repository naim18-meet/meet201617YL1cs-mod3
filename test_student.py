from student import Student 

Naim=Student('Naim', 'Haifa', '45', '100', 'vanilla')
Sama=Student('Sama', 'Kathmandou', '67', '410', 'avocado')
Ted=Student('Ted', 'New York', '31', '175', 'lettuce')

Naim.print_summary()
Sama.print_summary()
Ted.print_summary()

Naim.get_giraffe_gap()
x=Naim.get_giraffe_gap()
print(str(x))
Sama.get_giraffe_gap()
y=Sama.get_giraffe_gap()
print(str(y))
Ted.get_giraffe_gap()
z=Ted.get_giraffe_gap()
print(str(z))
