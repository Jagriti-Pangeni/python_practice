# lambda arguments:expression

# mod3= lambda x : x%3
# print(mod3(10))

points3D=[(1,2,4),(4,3,2),(9,0,6),(6,7,5)]
sort= sorted(points3D, key=lambda a: a[0]) #a[1] for sorting in y-axis, a[2] in sorting in z-axis
print(sort)