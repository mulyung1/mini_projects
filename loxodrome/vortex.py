            
#some default values:
#            spiral_stepping:  200
#            spiral_ratio:     0.618
#            density:          0.25
#            cut_off_points:   0.03
#            min_point_distance:   0.01

####################################################################
def frange(start, stop=None, step=None):    #python alapbol nem tud float stepet a for ciklusban, csak a numpy, azt viszont az ironpython nem tudja, ezert kell ez
    # if stop and step argument is None set start=0.0 and step = 1.0
    """
    Generator for a range of floating point numbers
    start, stop=None, step=None
    if stop and step argument is None set start=0.0 and step = 1.0
    """
    
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    #print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1
        

####################################################################
def spherical_logarithmic_spiral(center_lon, center_lat, rotate_spiral, dens, is_cw, ratio, stepping, is_limited, spiral_limit, cut_off_points, min_point_distance):
    """
    Create a spherical logarithmic spiral line in 3D space
    
    Parameters:
        center_lon (float): central longitude of the spiral
        center_lat (float): central latitude of the spiral
        rotate_spiral (float): rotation angle around z-axis in degrees
        dens (float): density of points on the spiral, in degrees
        is_cw (bool): whether the spiral is clockwise or not
        ratio (float): ratio of the spiral
        stepping (float): maximum angle from the central point, in degrees
        is_limited (bool): whether the spiral is limited or not
        spiral_limit (float): limit of the spiral, in fraction of stepping
        cut_off_points (float): distance from the center to cut off points, in km
        min_point_distance (float): minimum distance between points, in km
        
    Returns:
        The created Rhino curve object
    """
    start = timer()
    #rs.EnableRedraw(False)
    
    #phi = ((math.sqrt(5) + 1) / float(2)) - 1
    #m = (((math.sqrt(5) + 1) / float(2)) - 1 ) / float(2)
    #m = ratio / float(2)    #?????? miért osztjuk kettővel? valamiért így az oké!
    m = ratio
    r = 6378   
    
    #For lam=-stepping To stepping Step dens
    #i=0
    arrPoints = []    
    arrOutput = []   
    #for lam in range(-stepping,stepping,dens):
    #ennyi lepes: ((2*stepping)/dens)
    stepcounter=0
    steps=(2*stepping)/dens
    distance=0 #for mindistance
    prev_x=0
    prev_y=0
    prev_z=0

    for lam in frange(-stepping,stepping,dens):
        stepcounter+=1
        skip=False
        if (not is_limited) or (is_limited and stepcounter/steps<spiral_limit):
            x = r * float(math.cos(lam)) / float(math.cosh(m * lam))
            y = r * float(math.sin(lam)) / float(math.cosh(m * lam))
            z = r * float(math.tanh(m * lam))
            #If lam <= 0 Then	'ki lehet kapcsolni az egyik oldalát a spirálnak
            #	x = 0
            #	y = 0
            #	z = 0			
            #End If
            #line.append([x, y, z])
            
            if (x*x+y*y)<cut_off_points*cut_off_points: #pitagoraszi távolságmérés km-ben - ha a középponthoz közelebb van mint a cut_off_points (km-ben), akkor nem rakjuk ki a pontot. nagyon sűrű feleslegesen a közepe
                skip=True

            if stepcounter>0 and not skip:
                d = math.sqrt((prev_x - x)**2 + (prev_y - y)**2 + (prev_z - z)**2)
                if d<min_point_distance:
                    skip=True

            if not skip:
                point = rs.AddPoint((x, y, z))	
                rs.ObjectColor(point,(0,0,255))
                
                arrPoints.append( point )
                #arrOutput.append ( rs.PointCoordinates(point) ) #igy forditott a spiral, a vege lesz a piramisnal, tavmeresnel nem optimalis
                arrOutput.insert(0, rs.PointCoordinates(point) )
                
                #i = i + 1   

                prev_x=x
                prev_y=y
                prev_z=z

       
    logspiralcurve = rs.AddCurve(arrOutput, 1)
    spcolor=(0, 0, 200)
    rs.ObjectColor(logspiralcurve, spcolor)
    rs.DeleteObjects(arrPoints)
    
    #rs.MirrorObject(logspiralcurve, (0, 0, 0), (1, 0, 1))
    
    if not is_cw:
        rs.MirrorObject(logspiralcurve, (0, 0, 0), (1, 0, 1))
        
    #####logspiralcurve2 = rs.CopyObject(logspiralcurve)
    #####rs.MirrorObject(logspiralcurve2, (0, 0, 0), (1, 0, 1))
    #####rs.ObjectColor(logspiralcurve2, (255, 255, 0))
    
    
    logspiralaxis = rs.AddLine((0, 0, 10000), (0, 0, -7000))
    rs.ObjectColor(logspiralaxis, spcolor )	
    
    rs.RotateObject ( logspiralaxis, (0, 0, 0), 90 - center_lat, (1, 0, 0))		#föl / le forgatás
    rs.RotateObject ( logspiralaxis, (0, 0, 0), 180 + center_lon, (0, 0, 1)) 	#balra / jobbra forgatás
    
    rs.RotateObject ( logspiralcurve, (0, 0, 0), rotate_spiral, (0, 0, 1))		#jobbra-balra spirál forgatása
    rs.RotateObject ( logspiralcurve, (0, 0, 0), 90 + center_lat, (1, 0, 0))		#föl / le forgatás koordináta-pozícióra
    rs.RotateObject ( logspiralcurve, (0, 0, 0), 180 - center_lon, (0, 0, 1)) 	#balra / jobbra forgatás koordináta-pozícióra
    
    ####rs.RotateObject ( logspiralcurve2, (0, 0, 0), rotate_spiral, (0, 0, 1))		#jobbra-balra spirál forgatása
    #####rs.RotateObject ( logspiralcurve2, (0, 0, 0), 90 - center_lat, (1, 0, 0))	#föl / le forgatás koordináta-pozícióra
    #####rs.RotateObject ( logspiralcurve2, (0, 0, 0), 180 + center_lon, (0, 0, 1)) 	#balra / jobbra forgatás koordináta-pozícióra	    
    
    #rs.EnableRedraw(True)    
    end = timer()
    print('  spherical_logarithmic_spiral execution time (density: '+str(dens)+'):'+str(end - start)+' seconds')
    print('  lon:{}   lat:{}   rot:{}   dens:{}   iscw:{}   ratio:{}   stepping:{}   limited:{}   limit:{}   points:{}'.format(center_lon, center_lat, rotate_spiral, dens, is_cw, ratio, stepping, is_limited, spiral_limit, len(arrOutput)))
    return(logspiralcurve)

