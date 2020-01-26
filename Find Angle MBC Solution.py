import math

ab, bc = int(input()), int(input())

#In, △ABC ∠B= 90∘ and Mid point = M
#After drawing line from M to A we find a new △AMB.
#AM = MB[midpoint therom]
#So, AMB is a isoceles △ and ∠MBA = ∠A
# ∠A = tan0 =(opposite / adjacent)

print("{0:.0f}°".format(math.degrees(math.atan(ab/bc))))


