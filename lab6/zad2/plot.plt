set term pdf size 8, 8
set key autotitle columnhead


set grid
set output "before0.pdf"
plot "before0.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "after0.pdf"
plot "after0.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "before1.pdf"
plot "before1.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "after1.pdf"
plot "after1.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "before2.pdf"
plot "before2.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "after2.pdf"
plot "after2.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "before3.pdf"
plot "before3.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "after3.pdf"
plot "after3.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "before4.pdf"
plot "before4.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"
set output "after4.pdf"
plot "after4.dat" using 1:2 with linespoint \
pt 7 ps 0.8 lt rgb "dark-green"