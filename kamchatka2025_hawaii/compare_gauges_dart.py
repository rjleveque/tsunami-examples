from pylab import *
from clawpack.pyclaw.gauges import GaugeSolution


outdir1 = './_output_sift2'
outdir2 = './_output_usgs2'

fs1 = 15
fs2 = 13

#darts = [21401,21413,21414,21415,21416,21418,21419,52402]
darts = [21418]

for k,gaugeno in enumerate(darts):
    gaugeno1 = gaugeno
    gaugeno2 = gaugeno

    gauge1 = GaugeSolution(gauge_id=gaugeno1, path=outdir1)
    gauge2 = GaugeSolution(gauge_id=gaugeno2, path=outdir2)

    try:
        fname = 'DART/%s_detided.txt' % gaugeno1
        observed = loadtxt(fname)
        print('Loaded ',fname)
    except:
        observed = None

    figure(502+k,figsize=(13,5))
    clf()

    max_level = gauge1.level.max()
    eta = where(gauge1.level==max_level, gauge1.q[-1,:], nan)
    plot(gauge1.t/3600., gauge1.q[-1,:], 'r', label='SIFT source')

    max_level = gauge1.level.max()
    eta = where(gauge1.level==max_level, gauge1.q[-1,:], nan)
    plot(gauge2.t/3600., gauge2.q[-1,:], 'b', label='USGS source')

    if observed is not None:
        plot(observed[:,0]/3600, observed[:,1], 'k-', label='Obs',
             markersize=2, linewidth=1)

    xlabel('Hours after earthquake',fontsize=fs2)
    xlim(0,5)

    legend(loc='upper right',fontsize=fs1)
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    grid(True)
    ylabel('Surface (meters)',fontsize=fs2)

    title('DART %s comparison' % gaugeno1, fontsize=fs1)
    fname = 'DART%s.png' %  (gaugeno1,)
    savefig(fname, bbox_inches='tight')
    print('Created ',fname)
