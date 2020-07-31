def focal_length_concave(R):
    return R / 2
def focal_length_convex(R):
    return - ( R/ 2 )
# Driver function
R = 30 ;
print("Focal length of spherical concave mirror is :",
        focal_length_concave(R)," units")
print("Focal length of spherical convex mirror is : ",
        focal_length_convex(R)," units") 
