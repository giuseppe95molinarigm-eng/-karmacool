import sys
from PIL import Image, ImageOps, ImageFilter, ImageStat
src, out = sys.argv[1], sys.argv[2]
# name: (gamma, autocontrast cutoff %)  gamma<1 lightens midtones
cfg = {'image1': (0.72, 0.5), 'image2': (0.90, 0.5), 'image3': (1.25, 0.2), 'image4': (1.05, 0.3)}
for n, (gam, cut) in cfg.items():
    im = Image.open(f'{src}/{n}.jpeg').convert('RGB')
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=cut)
    lut = [round(255 * (i / 255) ** gam) for i in range(256)]
    g = g.point(lut)
    # keep paper-safe range: max black ~ 96%, no pure white blowout change
    g = g.point(lambda v: int(10 + v * (250 - 10) / 255))
    g = g.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    g.save(f'{out}/{n}_bw.jpg', quality=95, dpi=(300, 300))
    print(n, g.size, round(ImageStat.Stat(g).mean[0]))
