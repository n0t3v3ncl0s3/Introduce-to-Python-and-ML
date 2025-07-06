
# =====================================================
# I. CẤU TRÚC DỮ LIỆU
# =====================================================

# TODO 1: Tạo một danh sách chứa các số từ 1 đến 10.
list_numbers = [1,2,3,4,5,6,7,8,9,10]

# TODO 2: Tạo một dictionary ánh xạ tên con vật với số chân của nó (3 con). VD {dog : 4}, trả về danh sách key và value
num_legs = {
    'dog' : 4,
    'cat' : 4,
    'chicken': 2
}
keys = list(num_legs.keys())
values = list(num_legs.values())

# TODO 4: Trả về các giá trị riêng biệt trong list sau
lst = [1, 2, 2, 3, 4, 4, 5]
unique_value = set(lst)

# =====================================================
# II. LIST COMPREHENSION
# =====================================================

# TODO 5: Sử dụng list comprehension để tạo danh sách bình phương của các số từ 1 đến 10.
squares = [i*i for i in range(1,11)]

# TODO 6: Tạo danh sách chỉ chứa các số chẵn từ danh sách [1, 2, ..., 20] dùng list comprehension.
even_numbers = [i for i in range(1,21) if i%2==0]

# TODO 7: Tạo một danh sách chứa chiều dài các từ trong câu sau:
sentence = "I love ML&IoT lab so much"
word_lengths = [len(word) for word in sentence.split()]  # TODO: Viết list comprehension tính độ dài từng từ


# =====================================================
# III. LAMBDA FUNCTION
# =====================================================

# TODO 8: Viết một lambda function tính bình phương của một số.
square = lambda x : x*x

# TODO 9: Viết lambda function kiểm tra một số có chia hết cho 3 hay không.
divisible_by_3 = lambda x : x%3==0

# TODO 10: Cho danh sách các số, dùng `filter()` và lambda để lọc ra các số lớn hơn 5.
numbers = [1, 4, 6, 7, 2, 9, 3]
greater_than_5 = list(filter(lambda x:x>5,numbers))  # TODO: Dùng filter + lambda

# TODO 11: Sử dụng `map()` và lambda để nhân đôi các số trong danh sách [1, 2, 3, 4, 5].
numbers_to_double = [1, 2, 3, 4, 5] 
doubled_numbers = list(map(lambda x:2*x,numbers_to_double))  # TODO: Dùng map + lambda

# TODO 12: Sử dụng `reduce()` và lambda để tính tổng các số trong danh sách [1, 2, 3, 4, 5].
from functools import reduce
numbers_to_sum = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x,num:x+num,numbers_to_sum,0)  # TODO: Dùng reduce + lambda