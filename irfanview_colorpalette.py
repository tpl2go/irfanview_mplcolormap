import numpy as np
import matplotlib.pyplot as plt
import os



# colormaps
# reference from https://matplotlib.org/2.0.1/users/colormaps.html
colormaps = [
            # perceptually uniform sequential colormaps
            ("viridis.pal", plt.cm.viridis),
            ("plasma.pal", plt.cm.plasma),
            ("inferno.pal", plt.cm.inferno),
            ("magma.pal", plt.cm.magma),
            
            # sequential colormaps
            ("Greys.pal", plt.cm.Greys),
            ("Purples.pal", plt.cm.Purples),
            ("Blues.pal", plt.cm.Blues),
            ("Greens.pal", plt.cm.Greens),
            ("Oranges.pal", plt.cm.Oranges),
            ("Reds.pal", plt.cm.Reds),
            
            # sequential colormaps
            ("YlOrBr.pal", plt.cm.YlOrBr),
            ("OrRd.pal", plt.cm.YlOrRd),
            ("OrRd.pal", plt.cm.OrRd),
            ("PuRd.pal", plt.cm.PuRd),
            ("RdPu.pal", plt.cm.RdPu),
            ("BuPu.pal", plt.cm.BuPu),
            
            # sequential colormaps
            ("GnBu.pal", plt.cm.GnBu),
            ("PuBu.pal", plt.cm.PuBu),
            ("YlGnBu.pal", plt.cm.YlGnBu),
            ("PuBuGn.pal", plt.cm.PuBuGn),
            ("BuGn.pal", plt.cm.BuGn),
            ("YlGn.pal", plt.cm.YlGn),
            
            # sequential colormaps
            ("binary.pal", plt.cm.binary),
            ("gist_yarg.pal", plt.cm.gist_yarg),
            ("gist_gray.pal", plt.cm.gist_gray),
            ("gray.pal", plt.cm.gray),
            ("bone.pal", plt.cm.bone),
            ("pink.pal", plt.cm.pink),
            
            # sequential colormaps
            ("spring.pal", plt.cm.spring),
            ("summer.pal", plt.cm.summer),
            ("autumn.pal", plt.cm.autumn),
            ("winter.pal", plt.cm.winter),
            ("cool.pal", plt.cm.cool),
            ("Wistia.pal", plt.cm.Wistia),
            
            # sequential colormaps
            ("hot.pal", plt.cm.hot),
            ("afmhot.pal", plt.cm.afmhot),
            ("gist_heat.pal", plt.cm.gist_heat),
            ("copper.pal", plt.cm.copper),
            
            # diverging colormaps
            ("PiYG.pal", plt.cm.PiYG),
            ("PRGn.pal", plt.cm.PRGn),
            ("BrBG.pal", plt.cm.BrBG),
            ("PuOr.pal", plt.cm.PuOr),
            ("RdGy.pal", plt.cm.RdGy),
            ("RdBu.pal", plt.cm.RdBu),
            
            
            # diverging colormaps
            ("RdYlBu.pal", plt.cm.RdYlBu),
            ("RdYlGn.pal", plt.cm.RdYlGn),
            ("Spectral.pal", plt.cm.Spectral),
            ("coolwarm.pal", plt.cm.coolwarm),
            ("bwr.pal", plt.cm.bwr),
            ("seismic.pal", plt.cm.seismic),
            
            
            # qualitative colormaps
            ("Pastel1.pal", plt.cm.Pastel1),
            ("Pastel2.pal", plt.cm.Pastel2),
            ("Paired.pal", plt.cm.Paired),
            ("Accent.pal", plt.cm.Accent),
            ("Dark2.pal", plt.cm.Dark2),
            ("Set1.pal", plt.cm.Set1),
            ("Set2.pal", plt.cm.Set2),
            ("Set3.pal", plt.cm.Set3),
            ("tab10.pal", plt.cm.tab10),
            ("tab20.pal", plt.cm.tab20),
            ("tab20b.pal", plt.cm.tab20b),
            ("tab20c.pal", plt.cm.tab20c),
            
            # miscellaneous colormaps
            ("flag.pal", plt.cm.flag),
            ("prism.pal", plt.cm.prism),
            ("ocean.pal", plt.cm.ocean),
            ("gist_earth.pal", plt.cm.gist_earth),
            ("terrain.pal", plt.cm.terrain),
            ("gist_stern.pal", plt.cm.gist_stern),
            ("gnuplot.pal", plt.cm.gnuplot),
            ("gnuplot2.pal", plt.cm.gnuplot2),
            ("CMRmap.pal", plt.cm.CMRmap),
            ("cubehelix.pal", plt.cm.cubehelix),
            ("brg.pal", plt.cm.brg),
            ("hsv.pal", plt.cm.hsv),
            ("gist_rainbow.pal", plt.cm.gist_rainbow),
            ("rainbow.pal", plt.cm.rainbow),
            ("jet.pal", plt.cm.jet),
            ("nipy_spectral.pal", plt.cm.nipy_spectral),
            ("gist_ncar.pal", plt.cm.gist_ncar),
            ]

header = "JASC-PAL\n0100\n256"
a = np.linspace(0,1,256,endpoint=False)
            
os.makedirs("palettes", exist_ok=True)
for name, cm in colormaps :
    b = cm(a)
    c = np.round(b*255).astype(np.uint8)
    
    with open(os.path.join("palettes", name), "w") as f:
        print(header, file=f)
        np.savetxt(f,c[:,:3], fmt="%d")
#%%     
        
demo_image = np.arange(256)
demo_image = np.repeat(demo_image, 5)
demo_image = np.expand_dims(demo_image,0)
demo_image = np.repeat(demo_image,128, axis=0)
#%%
from PIL import Image
demo_image = demo_image.astype(np.uint8)
demo_image = Image.fromarray(demo_image)
demo_image.save("demo_image.png")