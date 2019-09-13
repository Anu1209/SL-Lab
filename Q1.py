def Remove(list1):
	final_list=[] #adding dynamically to the list
	for num in list1:
		if num not in final_list:
			final_list.append(num)
	return final_list


list1=['ak','bk','ak','aj','bk','sj','aj'];
print(Remove(list1))

