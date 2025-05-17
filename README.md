# Image-Reconstruction
Project Overview
This project implements a Dual-Mode Web-Based Image Processor that performs efficient image translation and reconstruction across multiple modalities — specifically, grayscale image colorization and thermal image reconstruction. It leverages a lightweight encoder and a GAN-based architecture to enable high-quality, cross-modal image synthesis optimized for resource-constrained platforms.

Features
Dual-mode support: Handles both grayscale and thermal images.
GAN-based architecture with multiple generators and discriminators.
Grayscale-to-color and thermal-to-visible spectrum image translation.
Efficient latent vector encoding for data compression.
Evaluation with PSNR, SSIM, and FID for quality assessment.
Lightweight design suitable for edge computing and embedded systems.

Technologies Used
Programming Language: Python
Deep Learning Framework: Custom implementation using Generative Adversarial Networks (GANs)
IDE: Spyder
Operating System: Windows
Image Processing Techniques:
Dual-mode encoder
Reconstruction and colorization generators
Adversarial training (with discriminator networks)
Metrics: PSNR, SSIM, FID

Model Architecture
A shared lightweight encoder compresses grayscale and thermal inputs into latent vectors.
Task-specific generators convert:
Grayscale → Color (RGB)
Thermal → Visible Spectrum
Two discriminators evaluate the realism of generated images.
Training optimized with adversarial, reconstruction, and consistency losses.

Evaluation Metrics
PSNR (Peak Signal-to-Noise Ratio)
SSIM (Structural Similarity Index)
FID (Fréchet Inception Distance)
These metrics ensure the visual fidelity, structural consistency, and realism of generated images.


