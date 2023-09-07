set terminal pngcairo size 440,200 enhanced font 'Verdana,10'
set output "m.png"


set key top left
set xlabel "β"
set ylabel "<m>"


set style line 2 lt rgb "#A00000"
set style line 3 lt rgb "#FF8C00"
set style line 8 lt rgb "#8B0000"
set xrange[0.436:0.444]

plot "enorig32.dat" u 1:3 w lines ls 8 lw 1.5 title "L=32", \
"enblock32.dat" u 1:3 w lines ls 8 lw 1.5 dt 4 title "L'=32"