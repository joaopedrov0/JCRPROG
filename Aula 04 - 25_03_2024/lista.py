fruits = ["Pineapple", "Banana", "Khaki", "Damascus"]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
data = ["Carlos", 19, True, 1.78, 2001]


a = list(range(10))
a = list()
companies = list(["Toyota", "Volkswagen", "Ford"])
ifsp = list("IFSP")

# print(letters[-10000])

nums = [0, 1, 2, 3, 4, 5]
nums[2:4] = ["A", "B"]
print(nums) # Retorna [0, 1, 'A', 'B', 4, 5]
nums[2:4] = [8, 8, 8]
print(nums) # Retorna [0, 1, 8, 8, 8, 4, 5]
nums[4:6] = []
print(nums) # Retorna [0, 1, 8, 8, 5]