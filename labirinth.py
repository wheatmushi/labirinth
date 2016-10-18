import sys

lab = '''
...........
.#.###.###.
.#...#...#.
.#.#####.#.
.#.....#.#.
##.###.###.
.....#.#.#.
.#.###.#.##
.#...#.#...
##.#.###.##
...#.......
'''.split()
heigth=len(lab)-1
width =len(lab[0])-1
exit_point=(heigth,width)

lab_map=set()

def search_next_point(start_point):
    next_points=set()
    s=start_point
    if s[0]>0 and lab[s[0]-1][s[1]]!='#' and (s[0]-1,s[1]) not in lab_map:
        next_points.add((s[0]-1,s[1]))
    if s[0]<heigth and lab[s[0]+1][s[1]]!='#' and (s[0]+1,s[1]) not in lab_map:
        next_points.add((s[0]+1,s[1]))
    if s[1]>0 and lab[s[0]][s[1]-1]!='#' and (s[0],s[1]-1) not in lab_map:
        next_points.add((s[0],s[1]-1))    
    if s[1]<width and lab[s[0]][s[1]+1]!='#' and (s[0],s[1]+1) not in lab_map:
        next_points.add((s[0],s[1]+1))
    return next_points

def exit_search(start_point):
    lab_map.add(start_point)
    if start_point==exit_point:
        print 'YES'
        sys.exit()
    else:
        next_points=search_next_point(start_point)
        for point in next_points:
            exit_search(point)

exit_search((0,0))
print 'NO'
