# Modified from https://www.ks.uiuc.edu/Research/vmd/current/ug/node205.html
# When coloring by BETA:
#  1. BURRIED will be colored white
#  2. Exposed HYDROPHOBIC will be colored cyan
#  3. The OTHERS will be colored yellow

proc tricolor_scale {} {
    set color_start [colorinfo num]
    display update off
    for {set i 0} {$i < 1024} {incr i} {
        if {$i == 0} {
            set r 1;  set g 1;  set b 0
        }
        if {$i == 511} {
            set r 1;  set g 1;  set b 1
        }
        if {$i == 513} {
            set r 0;  set g 1;  set b 1
        }
        color change rgb [expr $i + $color_start ] $r $g $b
    }
    display update on
}

tricolor_scale

set burried   [atomselect top "beta 0"]
$burried set beta 0

set hydrophob [atomselect top "beta > 0 and hydrophobic"]
$hydrophob set beta 1

set others [atomselect top "beta > 0 and not hydrophobic"]
$others set beta -1
