
def twoSum(nums, target):
        lista = []
        for index,number in enumerate(nums):
            for i in range(index,len(nums)):
                if (number + nums[i] == target):
                    if(index != i):
                        lista.append(index)
                        lista.append(i)
        return lista

lista = [3,3]            
lista1 = [3,2,4]

print(twoSum(lista,6))