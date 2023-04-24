
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import torch.optim as optim
import torchvision.utils as vutils

from torch_version.GAN import *
from torch_version.dataset import setup_dataset

from IPython.display import HTML

if __name__ == "__main__":
    dataroot = "data"
    n_workers = 2
    batch_size = 32
    epochs = 10
    image_size = 64
    n_channels = 3
    n_dim_generator_inp = 100
    n_dim_generator_fm = 64
    n_dim_discr_fm = 64
    lr = 0.0002
    beta_1 = 0.5    # Beta 1 hyperparameter for Adam optimizers
    n_gpus = 1
    n_imgs = 3200

    # Setup the dataset
    device = torch.device("cuda:0" if (torch.cuda.is_available() and n_gpus > 0) else "cpu")
    dataloader = setup_dataset(
        dataroot=dataroot,
        image_size=image_size,
        batch_size=batch_size,
        n_workers=n_workers,
        n_gpus=n_gpus,
        device=device,
        n_imgs=n_imgs,
        plot_image=True
    )

    # Create and print out the generator
    netG = Generator(
        nz=n_dim_generator_inp,
        ngf=n_dim_generator_fm,
        nc=n_channels,
        n_gpus=n_gpus
    ).to(device)
    netG.apply(weights_init)
    print("Generator:", netG)

    # Create and print out the descriminator
    netD = Discriminator(
        nc=n_channels,
        ndf=n_dim_discr_fm,
        n_gpus=n_gpus
    ).to(device)
    netD.apply(weights_init)
    print("Discriminator:", netD)

    # Loss functions and optimizers
    criterion = nn.BCELoss()
    fixed_noise = torch.randn(64, n_dim_generator_inp, 1, 1, device=device)

    real_label = 1.
    fake_label = 0.

    optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta_1, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta_1, 0.999))

    # Training loop

    # Lists to keep track of progress
    img_list = []
    G_losses = []
    D_losses = []
    iters = 0

    print("Starting Training Loop...")
    # For each epoch
    for epoch in range(epochs):
        for i, data in enumerate(dataloader, 0):
            ############################
            # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
            ############################
            netD.zero_grad()
            # Format batch
            real_cpu: torch.Tensor = data[0].to(device)
            b_size = real_cpu.size(0)
            label = torch.full((b_size, ), real_label, dtype=torch.float, device=device)
            # Forward pass real batch through D
            output = netD(real_cpu).view(-1)
            # Calculate loss on all-real batch
            errD_real = criterion(output, label)
            # Backward pass
            errD_real.backward()
            D_x = output.mean().item()
            
            ## Train with all-fake batch
            # Generate batch of latent vectors
            noise = torch.randn(b_size, n_dim_generator_inp, 1, 1, device=device)
            # Generate fake image bath with G
            fake = netG(noise)
            label = label.fill_(fake_label)
            # Classify all fake batch with D
            output = netD(fake.detach()).view(-1)
            # Calculate D's loss on the all-fake batch
            errD_fake = criterion(output, label)
            errD_fake.backward()
            D_G_z1 = output.mean().item()
            # Compute erroron D as sum over the fake and the real batches
            errD = errD_real + errD_fake
            # Update D
            optimizerD.step()

            ###################################
            # (2) Update G network: maximize log(D(G(z)))
            ###################################
            netG.zero_grad()
            label = label.fill_(real_label)
            output = netD(fake).view(-1)
            errG = criterion(output, label)
            errG.backward()
            D_G_z2 = output.mean().item()
            optimizerG.step()

            # Output training status
            if i % 50 == 0:
                print('[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
                    % (epoch, epochs, i, len(dataloader),
                        errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))
            
            # Save losses for later plotting
            G_losses.append(errG.item())
            D_losses.append(errD.item())

            # Check how the generator is doing by saving G's output on fixed_noise
            if (iters % 100 == 0) or ((epoch == epochs-1) and (i == len(dataloader)-1)):
                with torch.no_grad():
                    fake = netG(fixed_noise).detach().cpu()
                img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

            if iters == 500:
                break
            iters += 1
    plt.figure(figsize=(10,5))
    plt.title("Generator and Discriminator Loss During Training")
    plt.plot(G_losses,label="G")
    plt.plot(D_losses,label="D")
    plt.xlabel("iterations")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

    fig = plt.figure(figsize=(8,8))
    plt.axis("off")
    ims = [[plt.imshow(np.transpose(i,(1,2,0)), animated=True)] for i in img_list]
    ani = animation.ArtistAnimation(fig, ims, interval=1000, repeat_delay=1000, blit=True)

    HTML(ani.to_jshtml())
    plt.show()