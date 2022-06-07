<h1>VAE Experimentation on Stellar Spectra</h1>

🚧 🚧 🚧 Please note: This repository is a work in progress. Apologies for any inconsistencies. 🚧 🚧 🚧


This project involves experimentation with Variational Autoencoders when applied to APOGEE DR16 stellar spectra.

*Project poster as shown at CASCA 2022:*
![poster_v2](https://user-images.githubusercontent.com/35126600/168721754-23a79258-450e-4c64-9975-3ebbbfa6d738.png)
*High level diagram of model architecture:*
![model_diagram_v2](https://user-images.githubusercontent.com/35126600/168725167-fe86723a-a786-4937-a44d-f98a2d923e61.png)
*An example of spectral reconstruction using this model:*
![image](https://user-images.githubusercontent.com/35126600/151688313-0b84ace6-390a-410a-8255-795f42330d1f.png)

---

<h2>Prerequisites</h2>

To run the training and evaluation files, the dataset needs to be in the same directory as the notebooks.

The required data files are:

- allStar-r12-l33.fits
- apogee_astroNN-DR16-v1.fits
- contspec_dr16_err.fits
- contspec_dr16_final.fits
- contspec_dr16_mask.fits

---


<h2>Core Project Files</h2>

The three main notebooks are used for training, tuning and evaluating VAEs.

**vae_1_initial_training.ipynb**

- Use this file to train a VAE from scratch on stellar spectra
- Current model features 7514 -> 28 (actual) + 3 (injected) dimensions at latent layer
    - Data filtering: No stars with bad flags, SNR > 200, 4000 < teff < 5500, logg < 3.5, all errors > 1/200
    - Custom loss with three terms:
        - Reproduction Loss (enforces accurate reconstruction of spectra itself)
        - Structure Loss (enforces Gaussian structure in latent space)
        - Separability Loss (enforces low correlation between latent dimensions)
- Automatically saves best model so far, along with checkpoints
- Normalizes and plots all loss components
- Visualizes reconstructions, residuals, etc.

**vae_2_continue_training.ipynb**

- Use this file to fine-tune a completely trained model 
- Adjust loss function weights (prioritize components) and train for additional epochs

**vae_3_evaluation.ipynb**

- Use this file to test completed models
    - Visualize relationships between latent dimensions
    - Generate corner plots and correlation matrices
- **Note**: The evaluation notebook requires correlation matrix outputs (in .csv form) to be present in the same directory. These can be generated and saved by running the appropriate code (labelled in the notebook).

---

<h2>Previous files for testing</h2>

Other notebooks used for experimentation and development have been moved to the `testing-wip` folder.

Most of these files are out-of-date, but can be useful as reference. Some descriptions below (incomplete):

**data_test.py**
- FITS file loading, basic star info, retrieval of ASPCAP and `AstroNN` parameters
- Useful reference for building a basic data loading script

**vae_test local.ipynb** (*obsolete*)
- Implemented CUDA support for training on local machine (shift from Colab)

**vae_test.ipynb** (*obsolete*)
- Initial experimentation: Build rudimentary MLP encoder/decoder and training loop 

**vae_test_gelu.ipynb** (*obsolete*)
- Switch from sigmoid to GELU, modify from BCE to MSE loss

**vae_test_errors.ipynb** (*obsolete*)
- Current implementation, 7514 -> 28 dimensions at latent layer
- Data cleaning: No stars with bad flags, SNR > 200, 4000 < teff < 5500, logg < 3.5
- GELU activation function
- MSE loss with bad pixels masked 
- Adam optimizer, `amsgrad = True`
- *~800 minutes to run 10k epochs on RTX 3080*

**vae_eval.ipynb** (*obsolete*)
- Post-training evaluation
- Latent space analysis and plotting using `corner.py` 
- Effect of various parameters on latent space (e.g. metallicity, logg, Teff)