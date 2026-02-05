def function_that_adds_commas_to_numbers(num):
    print(f"{num:,}")
function_that_adds_commas_to_numbers(110010000)

def function_that_adds_two_zeros_to_numbers(num):
    print(f"{num:.2f}")
function_that_adds_two_zeros_to_numbers(11001)

def function_that_adds_plus_sign_to_numbers(num):
    print(f"+{num}")
function_that_adds_plus_sign_to_numbers(11001)

def function_that_adds_minus_sign_to_numbers(num):
    print(f"-{num:,}")
function_that_adds_minus_sign_to_numbers(110010000)

def function_that_converts_to_2_decimal_places(num):
    print(f"{num:.2f}")
function_that_converts_to_2_decimal_places(11001.12345)

def function_that_converts_to_whole_number(num):
    print(f"{num:,.2f}")
function_that_converts_to_whole_number(9999.999)

def function_that_adds_k_after_3_zeros(num):
    print(f"{num/1000:.0f}k")
function_that_adds_k_after_3_zeros(10000)

def function_that_adds_m_after_6_zeros(num):
    print(f"{num/1000000:.0f}m")
function_that_adds_m_after_6_zeros(10000000)

