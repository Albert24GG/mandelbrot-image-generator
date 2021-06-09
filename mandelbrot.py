from PIL import Image as image
import numpy, math, colorsys, progressbar

def mandelbrot(x, y, max_iterations):
    c = complex(x,y)
    z = 0
    i = 0

    while i <= max_iterations:
        i += 1
        z = z ** 2 + c
        if abs(z) >= 2:
            break
        if i == max_iterations:
            return -1

    smoothVal = float(i)  -  math.log( abs(math.log(abs(z))) / math.log(2) )
    smoothVal /= max_iterations
    return smoothVal; 
    
def buildFractal(min_x, max_x, min_y, max_y, width, height, max_iterations, filename = "mandelbrot"):
    img = image.new("RGB", (width, height));
    
    pixels = img.load()
    
    pixel_size_x = (max_x - min_x) / float(width);
    pixel_size_y = (max_y - min_y) / float(height);
    
    total_iterations = width * height
    current_iteration = 0
    
    widgets = [progressbar.Timer(format='Elapsed Time: %(elapsed)s')," Processing: ", progressbar.Percentage(), progressbar.Bar()]
    progress = progressbar.ProgressBar(widgets=widgets, max_value = total_iterations).start()
    
    for x in range(width):
        
        coord_x = min_x + x * pixel_size_x;
        
        for y in range(height):
            
            coord_y = min_y + y * pixel_size_y;
            
            iters = mandelbrot(coord_x, coord_y, max_iterations);
            
            if iters == -1:
                pixels[x, y] = (0, 0, 0)
                continue
            
            color = colorsys.hsv_to_rgb(iters*5+10, 0.8, 0.95)
            
            pixels[x, y] = tuple(map(lambda x : math.floor(x * 255), color))
            
            current_iteration += 1
            progress.update(current_iteration)
    
    file = filename + ".png";
    img.save(file)
