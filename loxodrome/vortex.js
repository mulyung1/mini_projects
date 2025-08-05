
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//function coord3d_to_lonlat(sphere_radius, coord3d) {
//-90 to 90 for latitude and -180 to 180 for longitude.
function coord3d_to_lonlat(sphere_radius, x, y, z) {     //lon -180 – +180  lat -90 | +90         lat90 lon0 - északi sark      lat-90 lon0 déli sark     0 0 egyen
  var lon = ((90 + (Math.atan2(x, y) * 180 / Math.PI)) % 360) - 180;    //x,z -> x,y-re cserélve !
  var lat = 90 - (Math.acos(z / sphere_radius)) * 180 / Math.PI;    //y helyett z lett!
  //console.log('coord3d_to_lonlat xyz: '+x+','+y+','+z+' -> lon-,lat|: '+lon+'(-),'+lat+'(|)');
  //figyelem, átfordulásokat kell kezelni:
  if (lon>180) { lon=lon-360; }
  if (lon<-180) { lon=lon+360; }
  return [lon, lat];
}


//####################################################################
function lonlat_to_coord3d(sphere_radius, lon,lat) {  //lon -  lat |        lat90 lon0 - északi sark      lat-90 lon0 déli sark     0 0 egyen
  pt=new myPoint(0, 0, sphere_radius);  
  pt.rotate(new Rotation(degrees_to_radians(-lat+90), 0, 1, 0));
  pt.rotate(new Rotation(degrees_to_radians(-lon), 0, 0, 1));
  //console.log('lonlat_to_coord3d   lon-,lat|: '+lon+'(-),'+lat+'(|)  ->  xyz: '+pt.i+', '+pt.j+', '+pt.k);
  return( [ pt.i, pt.j, pt.k ] );
}

//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
class Quaternion {
	constructor(r, i, j, k) {
		this.r = r;
		this.i = i;
		this.k = k;
		this.j = j;
	}
	static mult(q1, q2) {
		var r = q1.r * q2.r - q1.i * q2.i - q1.j * q2.j - q1.k * q2.k;
		var i = q1.r * q2.i + q1.i * q2.r + q1.j * q2.k - q1.k * q2.j;
		var j = q1.r * q2.j - q1.i * q2.k + q1.j * q2.r + q1.k * q2.i;
		var k = q1.r * q2.k + q1.i * q2.j - q1.j * q2.i + q1.k * q2.r;
		return new Quaternion(r, i, j, k);
	}
	static inv(q) {
		return new Quaternion(q.r, -q.i, -q.j, -q.k);
	}
}

//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
class myPoint {
	constructor(xPos, yPos, zPos) {
		this.r = 0;
		this.i = xPos;
		this.j = yPos;
		this.k = zPos;
	}
	rotate(rotation) {
		var q = Quaternion.mult(Quaternion.mult(rotation, this), Quaternion.inv(rotation));
		this.i = q.i;
		this.j = q.j;
		this.k = q.k;
	}
}

//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
const Rotation = function(angle, x, y, z) {
	const scaleFactor = Math.sqrt(x ** 2 + y ** 2 + z ** 2);
	const c = Math.sin(angle / 2) / (scaleFactor || 1);
	return new Quaternion(Math.cos(angle / 2), c * x, c * y, c * z);
}  


//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
function render_one_spiral(center_lon, center_lat, rotation, dens, is_cw, ratio, stepping, is_limited, spiral_limit, cut_off_points, min_point_distance) {
  //dens=0.005; stepping=50;  is_limited=false; spiral_limit=0.37;  cut_off_points=0.04;  min_point_distance=0.001;
  const r = 6378 / 100; 
  const spiralpoints_3d = spherical_logarithmic_spiral_points_3d(
                            center_lon, center_lat, 0, dens, is_cw, 
                            ratio, stepping, 
                            is_limited, spiral_limit, cut_off_points, min_point_distance);
  const spiralpoints2d = [];
  spiralpoints_3d.forEach((element) => {
          pt=new myPoint(element[0], element[1], element[2]);
          pt.rotate(new Rotation(degrees_to_radians(rotate_spiral), 1, 0, 0));	//tengely körül
          pt.rotate(new Rotation(degrees_to_radians(-center_lat), 0, 1, 0));
          pt.rotate(new Rotation(degrees_to_radians(-center_lon), 0, 0, 1));          
          spiralpoints2d.push( coord3d_to_lonlat(r, pt.i, pt.j, pt.k) )
    }
  );          

  var lineString = new LineString(spiralpoints2d);
  lineString.transform('EPSG:4326', 'EPSG:3857');        // transform to EPSG:3857

  var feature = new Feature({ // create the feature
        geometry: lineString,
        name: 'Line'  //+i
  });        

  return(feature);
  //feature_array.push(feature);
}






//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
function render_one_spiral_in_multiple_segments(center_lon, center_lat, rotation, dens, is_cw, ratio, stepping, is_limited, spiral_limit, cut_off_points, min_point_distance) { //ha lon átmenne a -180 <-> 180 fokon, akkor több szakaszban rajzolja ki
  //console.log('render_one_spiral_in_multiple_segments');
  //dens=0.005; stepping=50;  is_limited=false; spiral_limit=0.37;  cut_off_points=0.04;  min_point_distance=0.001;
  const r = 6378 / 100; 
  const spiralpoints_3d = spherical_logarithmic_spiral_points_3d(
                            center_lon, center_lat, 0, dens, is_cw, 
                            ratio, stepping, 
                            is_limited, spiral_limit, cut_off_points, min_point_distance);
  
  const spiralpoints2d = [];  //egy spirál összes pontja egyben
  const spiralpoints2d_feature_arr = [];  //egy spirál összes szegmense

  var perv_pt=undefined;
  var prev_lonlat=undefined;
  var lonlat=undefined;
  var pt=undefined;
  //lon 180 -180 közötti átmeneteket keresünk
  spiralpoints_3d.forEach((element) => {
          //let pt;
          //let lonlat;

          if (pt===undefined) { 
            perv_pt=new myPoint(element[0], element[1], element[2]); 
          } else {
            prev_pt=pt;
          }
          pt=new myPoint(element[0], element[1], element[2]);
          pt.rotate(new Rotation(degrees_to_radians(rotate_spiral), 1, 0, 0));	//tengely körül
          pt.rotate(new Rotation(degrees_to_radians(-center_lat), 0, 1, 0));
          pt.rotate(new Rotation(degrees_to_radians(-center_lon), 0, 0, 1));    

          if (lonlat===undefined) {  //első pont
            //console.log('first point');
            lonlat=coord3d_to_lonlat(r, pt.i, pt.j, pt.k);
            prev_lonlat=lonlat; 
          } else {
            prev_lonlat=lonlat;
            lonlat=coord3d_to_lonlat(r, pt.i, pt.j, pt.k);
          }

          if (
            (lonlat[0]>150 && prev_lonlat[0]<-150) || (lonlat[0]<-150 && prev_lonlat[0]>150)
          ) { //új szegmens kezdete
            //console.log('NEW SEGMENT - lon: '+prev_lonlat[0]+'  -> '+lonlat[0]);
            linefeature=createLineFeatureFromPoints(spiralpoints2d);
            spiralpoints2d_feature_arr.push(linefeature);
            spiralpoints2d.length = 0; // clear the array for the new segment
          } else {  //folytatódik a szegmens
            //console.log('lon: '+prev_lonlat[0]+'  -> '+lonlat[0]);
          }
          spiralpoints2d.push(lonlat) //coord3d_to_lonlat returns [lon, lat];
    }
  );    
  linefeature=createLineFeatureFromPoints(spiralpoints2d);
  spiralpoints2d_feature_arr.push(linefeature);  //utolsó szegmens      

  return(spiralpoints2d_feature_arr);
}





//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
function degrees_to_radians(degrees)
{
  // Store the value of pi.
  var pi = Math.PI;
  // Multiply degrees by pi divided by 180 to convert to radians.
  return degrees * (pi/180);
}


//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
function frange(start, stop = null, step = null) {
  start = parseFloat(start);
  if (stop === null) {
      stop = start + 0.0;
      start = 0.0;
  }
  if (step === null) {
      step = 1.0;
  }

  let count = 0;
  const result = [];
  while (true) {
      const temp = parseFloat(start + count * step);
      if ((step > 0 && temp >= stop) || (step < 0 && temp <= stop)) {
          break;
      }
      result.push(temp);
      count += 1;
  }
  return result;
}

//WMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMWWMWMWMW
function spherical_logarithmic_spiral_points_3d(center_lon, center_lat, rotate_spiral, dens, is_cw, ratio, stepping, is_limited, spiral_limit, cut_off_points, min_point_distance) {
  const start = performance.now();
  
  const m = ratio;
  const r = 6378 / 100; 

  const arrPoints = [];
  let stepcounter = 0;
  const steps = (2 * stepping) / dens;
  let prev_x = 0;
  let prev_y = 0;
  let prev_z = 0;

  cwmultiply=1;
  if (!is_cw) { cwmultiply=-1; }

  for (const lam of frange(-stepping, stepping, dens)) {
      stepcounter++;
      let skip = false;
      
      if (!is_limited || (is_limited && stepcounter / steps < spiral_limit)) {
          //const x = r * Math.cos(lam) / Math.cosh(m * lam);
          //const y = r * Math.sin(lam) / Math.cosh(m * lam);
          //const z = r * Math.tanh(m * lam);

          //FIGYELEM A TÉRKÉPEN MÁSHOGY KELL:
          const z = r * Math.cos(lam) / Math.cosh(m * lam);
          const y = (r * Math.sin(lam) / Math.cosh(m * lam))*cwmultiply;
          const x = r * Math.tanh(m * lam);       

          //if ((z * z + x * x) < cut_off_points * cut_off_points) {
          if ((x * x + y * y) < cut_off_points * cut_off_points) {
              //skip = true;
          }

          if (stepcounter > 0 && !skip) {
              const d = Math.sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2 + (prev_z - z) ** 2);
              if (d < min_point_distance) {
                  skip = true;
              }
          }

          if (!skip) {
              arrPoints.push([x, y, z]);
              prev_x = x;
              prev_y = y;
              prev_z = z;
          }
      }
  }
  //arrPoints.push( lonlat_to_coord3d(r, center_lon, center_lat) ); //elejére és végére pontot teszünk, hogy jól látszódjék a közepe!

  const end = performance.now();
  //console.log('  spherical_logarithmic_spiral execution time (density: ' + dens + '): ' + (end - start) + ' milliseconds');
  //console.log('  lon: ' + center_lon + '   lat: ' + center_lat + '   rot: ' + rotate_spiral + '   dens: ' + dens + '   iscw: ' + is_cw + '   ratio: ' + ratio + '   stepping: ' + stepping + '   limited: ' + is_limited + '   limit: ' + spiral_limit + '   points: ' + arrPoints.length);
  //console.log(arrPoints.length);
  return arrPoints;
  }
