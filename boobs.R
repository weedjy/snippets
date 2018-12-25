par(bg = "white");
a <- seq(-12, 12, length = 120);
b <- seq(-12, 12, length = 120);
z <- outer(a, b, function(x, y) exp((-(((x-4)^2+(y-4)^2)^2))/1000) + exp((-(((x+4)^2+(y+4)^2)^2))/1000) + 0.1*exp(-(((x+4)^2+(y+4)^2)^2)) 
                                + 0.1*exp(-(((x-4)^2+(y-4)^2)^2)));
nrz <- nrow(z);
ncz <- ncol(z);
jet.colors <- colorRampPalette( c("yellow", "coral") );
nbcol <- 1200;
color <- jet.colors(nbcol);
zfacet <- z[-1, -1] + z[-1, -ncz] + z[-nrz, -1] + z[-nrz, -ncz];
facetcol <- cut(zfacet, nbcol);
persp(a, b, z, col = color[facetcol], phi = 30, theta = 55);
