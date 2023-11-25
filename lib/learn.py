# i=0
# while i <= 5 :
#     print(f"Square of {i} is {i*i}")
#     i+=1

# for i in range(10):
#       s=i+1
#       print(f"Square of {s} is {s*s}")

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 
                  0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009,
                    0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()
print()
print("----------------------- While Example --------------------------------")
print()

i=0
while i<len(player_heights):
    inch_height = player_heights[i]*7920
    inch_heights.append(inch_height)
    i+=1

print(inch_heights)

print()
print("----------------------- For Loop Example --------------------------------")
print()
# inch_heights.clear()

for height in player_heights:
    inch_height = height * 7920
    inch_heights.append(inch_height)
 
print(inch_heights)

print()
print("------------------------------ Inline Example --------------------------------")
print()

inch_heights = [height*7920 for height in player_heights]

print(inch_heights)
print()
print("----------------------- Another Inline Example with same name --------------------------")
print()
player_heights = [height*7920 for height in player_heights]

print(player_heights)

