def parabola(a, b, c):
    print ("Vertex: (" , (-b / (2 * a)) , ", "
        ,(((4 * a * c) - (b * b)) / (4 * a)) , ")" )
    print ("Focus: (" , (-b / (2 * a)) , ", "
        , (((4 * a * c) - (b * b) + 1) / (4 * a)) , ")" )
    print ("Directrix: y="
            , (int)(c - ((b * b) + 1) * 4 * a ))
# main
a = 5
b = 3
c = 2
parabola(a, b, c) 
