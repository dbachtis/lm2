This is a minimal working example of the two-lattice matching MCRG with the use of histogram reweighting for the case of the 2D Ising model.

The results are fully reproduced by executing "run".

In more detail:
1) "block.py" applies a renormalization group transformation on the original data simulated for L=64. It will then calculate the internal energy for the original system of L=64, the renormalized system of L'=32 and another original system of L=32 at beta=0.440687.
2) "reweight.py" implements histogram reweighting to obtain expectation values of observables for the original and the renormalized system in a range of inverse temperatures.
3) "map.py" creates the mappings which relate the original and the renormalized inverse temperatures
4) "magn.plt" will draw the magnetization of the renormalized L'=32 and original L=32 systems so the intersection which corresponds to the fixed point will be observed.
5) "map.plt" will draw the mappings which relate the original and the renormalized inverse temperatures. The vertical line corresponds to beta=0.440687
6) "nu.py" calculates the critical exponent nu based on the data at two values of betas.

This minimal working example has not been tested for bugs. The permitted reweighting range is additionally not verified. It is given as is for clarification of concepts behind the discussed MCRG method.
