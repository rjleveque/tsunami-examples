from pylab import *
from clawpack.pyclaw.gauges import GaugeSolution


outdir1 = './_output_sift'
outdir2 = './_output_usgs'
#outdir2 = './_output'


gaugeno1 = 5680
gaugeno2 = gaugeno1

gauge1 = GaugeSolution(gauge_id=gaugeno1, path=outdir1)
gauge2 = GaugeSolution(gauge_id=gaugeno2, path=outdir2)

try:
    fname = 'DART/%s_detided.txt' % gaugeno1
    observed = loadtxt(fname)
    print('Loaded ', fname)
except:
    observed = None

fs1 = 15
fs2 = 13

figure(500,figsize=(13,5))
clf()

max_level = gauge1.level.max()
eta = where(gauge1.level==max_level, gauge1.q[-1,:], nan)
plot(gauge1.t/3600., eta, 'b', label='SIFT source')

max_level = gauge2.level.max()
eta = where(gauge2.level==max_level, gauge2.q[-1,:], nan)
plot(gauge2.t/3600., eta, 'r', label='USGS source')

if observed is not None:
    plot(observed[:,0]/3600, observed[:,1], 'k-o',
         markersize=5, label='Observed')

xlabel('Hours after earthquake',fontsize=fs2)

legend(loc='upper left',framealpha=1,fontsize=fs1)
xlim(5,9)
ylim(-4,4)
grid(True)
ylabel('Surface (meters)',fontsize=fs2)
xticks(fontsize=fs2)
yticks(fontsize=fs2)

title('Gauge 5680 comparison ',fontsize=fs1)

fname = 'Gauge5680.png'
savefig(fname, bbox_inches='tight')
print('Created ',fname)
