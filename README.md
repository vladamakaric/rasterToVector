# Vectorization project

This was a research project for my bachelor thesis:
"Comparison of Algorithms for Bezier Curve Fitting", which deals with fitting Bezier curves to polygons.

The goal of this project is to produce a vector image (e.g. SVG)
from a raster, this process is known as [image tracing](https://en.wikipedia.org/wiki/Image_tracing) or vectorization.

Example of input and output:

![Alt text](/screenshot.png?raw=true "Optional Title")

There are several stages to this:

1. Extracting the polygonal pixel contour from the raster image.
2. Simplifying the contour, i.e. finding the optimal subpoligon of the original polygon using a modification of Floyd-Warshall.
3. Further optimizing the polygon by minimizing the variance between every edge and the part of the pixel contour it represents (using Principal Component Analysis).
4. Corner detection, deciding which points on the polygon will be cusps and which will be smoothed out (G0 and G1 continuity, respectively) in the next phase.
5. Bezier curve fitting, the polylines between each pair of corners (cusps) are fitted with a smooth (G1 continuous) chain of 1 or more Bezier curves.

This implementation is inspired by [potrace](http://potrace.sourceforge.net/) and Philip J. Schneider's "An Algorithm for Automatically Fitting Digitized Curves", published in Graphics Gems 1.

This implementation is not efficient or robust (there are many corner cases not delt with).




