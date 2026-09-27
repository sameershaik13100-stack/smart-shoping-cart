product_list=["loptop","mouse","keybord","headphones","useb cable"]
product_list.remove("useb cable")
product_list.append("webcam")
product_list.remove("webcam")
product_list.insert(3,"webcam")

print("complete_cart:-",product_list)
print("first_product:-",product_list[0])
print("last_product:-",product_list[-1])
print("total_products:-",len(product_list))

price_list=[55000,800,1500,2500,2000]

print("total prices:-",sum(price_list))
print("cheapest price:-",min(price_list))
print("expincive price:-",max(price_list))
print("position of webcam:-",product_list.index("webcam"))
print("number of times 2000:-",price_list.count(2000))
print("original prices:-",price_list)
price_list.sort()
print("lowest-highest:-",price_list)
price_list.reverse()
print("highest-lowest:-",price_list)
