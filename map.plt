set terminal pngcairo size 440,200 enhanced font 'Verdana,10'
set output "map.png"


set key top left
set xlabel "β"
set ylabel "β'"

set style line 8 lt rgb "#8B0000"

set xrange[0.436:0.444]
set yrange[0.436:0.444]

f(x)=x

set arrow from 0.440687,0.436 to 0.440687,0.444 nohead

plot "map.dat" u 2:1 w lines ls 8 lw 1.5 title "Mappings", \
f(x) w lines ls 8 dt 4 title "f(x)=x"