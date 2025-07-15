input_str = "Ishita"
reverse_str = ""

for char in input_str:
    reverse_str = char + reverse_str
    
print(reverse_str)

# Summary:
# Code	Output	Meaning
# reverse_str = char + reverse_str	atihsI	Reverses the string
# reverse_str = reverse_str + char	Ishita	Keeps it in original order

# Loop Execution for char + reverse_str:
# Loop chalta hai har character ke liye "Ishita" me:

# Iteration	char	Old reverse_str	New reverse_str = char + reverse_str
# 1	'I'	""	"I"
# 2	's'	"I"	"sI"
# 3	'h'	"sI"	"hsI"
# 4	'i'	"hsI"	"ihsI"
# 5	't'	"ihsI"	"tihsI"
# 6	'a'	"tihsI"	"atihsI"

# Loop Execution for reverse_str + char
# Iteration	char	Old reverse_str	New reverse_str = reverse_str + char
# 1	'I'	""	"I"
# 2	's'	"I"	"Is"
# 3	'h'	"Is"	"Ish"
# 4	'i'	"Ish"	"Ishi"
# 5	't'	"Ishi"	"Ishit"
# 6	'a'	"Ishit"	"Ishita"