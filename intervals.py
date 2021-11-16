intervals = [ [1,3], [2,4], [5,7], [6,8] ]
new_intervals = []

def merge ( array1, array2 ) :
    new_interval = []
    ans=[]
    index1=0
    index2=0
    
    while ( index1 < 2 and index2 < 2 ):
        
        if array1 [ index1 ] > array2 [ index2 ] :
            ans.append ( array2 [ index2 ] )
            if index2 != 1 : index2 += 1
            else : ans.append ( array1 [ index1 ] )
            
        elif array1 [ index1 ] < array2 [ index2 ] :
            ans.append ( array1 [ index1 ] )
            if index1 != 1 : index1 += 1
            else : ans.append ( array2 [ index2 ] )
            
        else:   # array1[index1]==array2[index2]:
            ans.append ( array1 [ index1 ] )
            ans.append ( array2 [ index2 ] )
            if index1 != 1 : index1 += 1
            if index2 != 1 : index2 += 1
            
        if len( ans ) == 4 : break
    
    new_interval.append ( ans[0] )
    new_interval.append ( ans[3] )
    return (new_interval)

for index in range ( 0, len(intervals)-1 ) :
    x = intervals [ index ]
    y = intervals [ index+1 ]

    if  ( ( x[0]<y[0] and y[0]<x[1] ) or ( y[0]>x[0] ) and x[1]>y[0]) :
        #   merge and sort
        temp = merge ( x , y )
        new_intervals.append ( temp )

    elif ( x[0]==y[1] or x[1]==y[0] or x[0]==y[0] or x[1]==y[1] ) :
        #   merge and sort because interval has a common element
        temp = merge ( x , y )
        new_intervals.append ( temp )
        
print ( new_intervals )
