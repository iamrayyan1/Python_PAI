def area_trap(b1,b2,h):
  area= 0.5*(b1+b2)*h
  return area

def area_parallelogram(base,height):
  area = base*height
  return area

def area_cylinder(radi,height):
  area = 2*3.142*radi*(radi+height)
  return area

def vol_cylinder(radi,height):
  vol = 3.142*radi**2*height
  return vol

print("Area of trap is: " , area_trap(2,2,3))

print("Area of para is: " , area_parallelogram(3,3))


print("Area of cylinder is: " , area_cylinder(2,2))


print("Vol of trap is: " , vol_cylinder(2,3))



