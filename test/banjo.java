
import java.io.*;
import java.util.*;
import java.math.*;

/**
 * Solution to Banjo
 * 
 * @author vanb
 */
public class banjo_vanb
{
    public Scanner sc;
    public PrintStream ps;
    
    public static final double EPSILON = 0.000000001;
    public static final double TWOPI = Math.PI+Math.PI;
    public static final int STEP = 3;
    
    public double xA, yA, xB, yB, xC, yC, r, t; 
    public double loA, hiA, loB, hiB;
    public double aCA, aCB, at;
    public double dAB, dAC, dBC;
    
    /**
     * Get an angle from a triangle where all three side lengths are known.
     * 
     * Law of Cosines sez: c*c = a*a + b*b - 2*a*b*cos(theta)
     * 
     * Solving for theta gives:
     * theta = arccos( (a*a + b*b - c*c) / (2*a*b) )
     * 
     * @param a Length of a side adjacent to the angle
     * @param b Length of the other side adjacent to the angle
     * @param c Length of the side opposite the angle
     * @return Angle between a and (opposite c)
     */
    public static double angle( double a, double b, double c )
    {
        return Math.acos( (a*a+b*b-c*c)/(2.0*a*b)  );
    }
    
    /**
     * Get a length of a side from a triangle where two side lengths are known,
     * and the angle between them.
     * 
     * Law of Cosines sez: c*c = a*a + b*b - 2*a*b*cos(theta)
     * 
     * Solving for c gives:
     * c = sqrt( (a*a + b*b - 2*a*b*cos(theta) )
     * 
     * @param a Length of a side adjacent to the angle
     * @param b Length of the other side adjacent to the angle
     * @param theta Angle between a and b
     * @return Length of side c, opposite angle theta
     */
    public static double length( double a, double b, double theta )
    {
        return Math.sqrt( a*a+b*b-2.0*a*b*Math.cos(theta) );
    }
    
    /**
     * Make sure an angle is between 0 and 2pi.
     * 
     * @param angle An angle
     * @return The same angle, but between 0 and 2pi
     */
    public static double positive( double angle )
    {
        while( angle<0.0 ) angle += TWOPI;
        while( angle>=TWOPI ) angle -= TWOPI;
        
        return angle;
    }
    
    /**
     * Normalize an angle to be between 0 and pi. Any two rays 
     * starting from the same point that aren't collinear
     * form 2 angles, one <pi, one >pi. We want the one <pi.
     * 
     * @param angle An angle
     * @return The same angle, but <pi, 
     */
    public static double normalize( double angle )
    {
        angle = positive( angle );
        if( angle>Math.PI ) angle = TWOPI - angle;
        
        return angle;
    }
    
    /**
     * The amount of time banjo spends walking on lava to
     * traverse an arc of angle 'angle', where 'at' is the angle of
     * the arc he can cut off which each length-t chord.
     * 
     * @param angle Angle Banjo needs to traverse
     * @return Distance covered over lava
     */
    public double lava( double angle )
    {
        double distance = 0.0;
             
        if( t==0 )
        {
            // Special case - if t=0, Banjo just walks along the perimeter of the circle.
            distance = r * angle;   
        }
        else
        {
            double ts = Math.floor( angle/at );       
            distance = ts*t + length( r, r, angle-ts*at );           
        }
        
        return distance;
    }
    
    /**
     * This interface defines a function to be minimized by the minimize() method.
     * 
     * @author vanb
     */
    public interface Function
    {
        /**
         * Function to be minimized.
         * 
         * @param x Meaning of parameters varies.
         * @param y Meaning of parameters varies.
         * @return Evaluation of function
         */
        public double f( double x, double y );
    }  
    
    /**
     * Function to minimize when looking at B angles.
     * 
     * @author vanb
     */
    public class MinB implements Function
    {
        /**
         * This is the distance Banjo must travel
         * if the A angle is x, and the B angle is y.
         * 
         * @param x A angle
         * @paray y B angle
         */
        public double f( double x, double y )
        {
            return length( r, dAC, normalize(x-aCA) ) 
                 + length( r, dBC, normalize(y-aCB) ) 
                 + lava( normalize(y-x) );
        }        
    } 
    public MinB minb = new MinB();
    
    /**
     * Function to minimize when looking at A angles
     * 
     * @author vanb
     */
    public class MinA implements Function
    {
        /**
         * This is the minimum distance Banjo must travel 
         * if the A angle is y.
         * 
         * @param x Unused
         * @param y A angle
         */
        public double f( double x, double y )
        {
            return minimize( loB, hiB, y, minb );      
        }
    }
    
    public MinA mina = new MinA();
    
    /**
     * Minimize a function within a range.
     * 
     * @param lo One end of the range
     * @param hi The other end of the range
     * @param x A fixed parameter
     * @param fun Function to minimize
     * @return Minimum value of the function in the range
     */
    public double minimize( double lo, double hi, double x, Function fun )
    {
        double minimum = Double.MAX_VALUE;
        
        while( Math.abs(hi-lo)>EPSILON )
        {
            // Chop the interval into STEP subintervals
            double increment = (hi-lo)/(double)STEP;
            minimum = Double.MAX_VALUE;
            int where = 0;
            for( int i=0; i<=STEP; i++ )
            {
                double y = lo + i*increment;
                double v = fun.f(x,y);
                if( v<minimum )
                {
                    where = i;
                    minimum = v;
                }
            }
            
            // Adjust lo & hi to be on opposite sides
            // of the minimum value, except if it's
            // on the edges.
            if( where<STEP-1 ) hi = lo+(where+1)*increment;
            if( where>1 ) lo = lo+(where-1)*increment;
        }
        
        return minimum;
    }
        
    /**
     * Driver.
     * @throws Exception
     */
    public void doit() throws Exception
    {
        sc = new Scanner( new File( "banjo.in" ) );
        ps = new PrintStream( new FileOutputStream( "banjo.vanb" ) );
        
        for(;;)
        {
            xA = sc.nextInt();
            yA = sc.nextInt();
            xB = sc.nextInt();
            yB = sc.nextInt();
            xC = sc.nextInt();
            yC = sc.nextInt();
            r = sc.nextInt();
            t = sc.nextInt();
            if( r<0.5) break;
            
            double mindist = -1.0;
            
            // Distances
            dAB = Math.hypot( yB-yA, xB-xA );
            dAC = Math.hypot( yC-yA, xC-xA );
            dBC = Math.hypot( yC-yB, xC-xB );
                                    
            // Let's check to see if we can get from A to B directly.
            // First, do we bypass the circle entirely?
            // Are the points A, B and C on a straight line, with C *NOT* between A and B?
            if( Math.abs( dAB + dBC - dAC ) < EPSILON ) mindist = dAB;
            else if( Math.abs( dAB + dAC - dBC ) < EPSILON ) mindist = dAB;            
            else if( Math.abs( dAC + dBC - dAB ) < EPSILON ) // Line AB goes through C
            {
                if(r+r<t) mindist = dAB;
            }
            else
            {
                // We need to find the shortest distance between the line AB 
                // and the center of the circle, C. First, get the angle BAC.
                double aBAC = angle( dAB, dAC, dBC );
                
                // Call the point of intersection P. Then APC is a right triangle, with AC as the hypotenuse.
                // So is BPC, with BC as the hypotenuse.
                double dCP = Math.sin( aBAC ) * dAC;
                double dAP = Math.sqrt( dAC*dAC - dCP*dCP );
                double dBP = Math.sqrt( dBC*dBC - dCP*dCP );

                if( dCP>=r || dAP>dAB || dBP>dAB ) mindist = dAB;
                else
                {
                    // Is the distance we cross less than t?
                    double cross = 2.0*Math.sqrt( r*r-dCP*dCP );    
                    if( cross<t ) mindist = dAB;
                }
            }

            if( mindist < -0.5 )
            {
                // First, get the angle of a chord of length t
                at = angle( r, r, t );
                
                // Get the angles from the center C to the two points A and B
                aCA = positive( Math.atan2( yA-yC, xA-xC ) );
                aCB = positive( Math.atan2( yB-yC, xB-xC ) );
                
                // Figure out the lo & hi angles for point A.
                // The lo angle will just be straight at the center.
                // The hi angle will be where a line from A is tangent to the circle.
                // There will be two of these, we'll take the one that's closer to B.
                loA = aCA;
                double diff = positive( Math.acos( r / dAC ) );
                double up = positive( loA+diff );
                double dn = positive( loA-diff );                
                double diffA = hiA = ( normalize(aCB-up) < normalize(aCB-dn) ) ? up : dn;                
                if( positive(hiA-loA) > Math.PI )
                {
                    double t = loA;
                    loA = hiA;
                    hiA = t;
                }
                if( hiA>loA && hiA-loA > Math.PI ) loA += TWOPI;
                if( hiA<loA && loA-hiA > Math.PI ) hiA += TWOPI;
                
                // Same for B
                loB = aCB;
                diff = positive( Math.acos( r / dBC ) );
                up = positive( loB+diff );
                dn = positive( loB-diff );                
                hiB = ( normalize(diffA-up) < normalize(diffA-dn) ) ? up : dn;
                if( positive(hiB-loB) > Math.PI )
                {
                    double t = loB;
                    loB = hiB;
                    hiB = t;
                }
                if( hiB>loB && hiB-loB > Math.PI ) loB += TWOPI;
                if( hiB<loB && loB-hiB > Math.PI ) hiB += TWOPI;
                        
                mindist = minimize( loA, hiA, 0.0, mina );
            }
            
            ps.printf( "%.2f", mindist );
            ps.println();
            
            String answer = String.format( "%.5f", mindist );
            if( answer.endsWith( "499" ) || answer.endsWith( "500" ) ) 
            {
                System.err.println( "Too close to cusp!! " + mindist );
            }
        }
    }
            
    /**
     * @param args
     */
    public static void main( String[] args ) throws Exception
    {
        //long start = System.currentTimeMillis();
        new banjo_vanb().doit();     
        //System.out.println( System.currentTimeMillis() - start );        
    }   
}