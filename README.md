<h1>VAE Experimentation on Stellar Spectra</h1>

Testing and experimentation with Variational Autoencoders using APOGEE DR16 stellar spectra.

![image](https://user-images.githubusercontent.com/35126600/148812543-016f0822-4870-47ae-80a7-524c1d125577.png)

---

<h2>Core Files</h2>

<h3>Current WIP Files</h3>

**vae_test_errors.ipynb** (*main training loop*)
- Current implementation, 7514 -> 28 dimensions at latent layer
- Data cleaning: No stars with bad flags, SNR > 200, 4000 < teff < 5500, logg < 3.5
- GELU activation function
- MSE loss with bad pixels masked 
- Adam optimizer, `amsgrad = True`
- *~800 minutes to run 10k epochs on RTX 3080*

**vae_eval.ipynb**
- Post-training evaluation, latent space analysis and plotting, `corner.py` testing

---

<h3>Previous files for testing</h3>

**data_test.py**
- FITS file loading, basic star info, retrieval of ASPCAP and `AstroNN` parameters

**vae_test local.ipynb** (*obsolete*)
- Implemented CUDA support for training on local machine (shift from Colab)

**vae_test.ipynb** (*obsolete*)
- Initial experimentation: Build rudimentary MLP encoder/decoder and training loop 

**vae_test_gelu.ipynb** (*obsolete*)
- Switch from sigmoid to GELU, modify from BCE to MSE loss


