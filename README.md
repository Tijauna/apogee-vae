<h1>VAE Experimentation on Stellar Spectra</h1>

🚧 🚧 🚧 Please note: Repository is Work In Progress. Apologies for any inconsistencies. 🚧 🚧 🚧


Testing and experimentation with Variational Autoencoders using APOGEE DR16 stellar spectra.

![poster_v2](https://user-images.githubusercontent.com/35126600/168721754-23a79258-450e-4c64-9975-3ebbbfa6d738.png)
![model_diagram_v2](https://user-images.githubusercontent.com/35126600/168725167-fe86723a-a786-4937-a44d-f98a2d923e61.png)
![image](https://user-images.githubusercontent.com/35126600/151688313-0b84ace6-390a-410a-8255-795f42330d1f.png)


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
- Post-training evaluation
- Latent space analysis and plotting using `corner.py` 
- Effect of various parameters on latent space (e.g. metallicity, logg, Teff)

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


