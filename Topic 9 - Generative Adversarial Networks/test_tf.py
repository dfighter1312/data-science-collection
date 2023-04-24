import glob
import PIL
import os
import imageio
import time
import matplotlib
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow_version.GAN import *
from tensorflow_version.dataset import setup_dataset

from IPython import display

matplotlib.use('TKAgg')


if __name__ == "__main__":
    BUFFER_SIZE = 60000
    BATCH_SIZE = 32
    EPOCHS = 20
    NOISE_DIM = 100
    N_EXAMPLES_TO_GENERATE = 16

    # Setup the dataset
    train_dataset = setup_dataset(BUFFER_SIZE, BATCH_SIZE)

    # Initialize the model
    generator = Generator()
    discriminator = Discriminator()

    # Add checkpoint
    checkpoint_dir = './training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                                    discriminator_optimizer=discriminator_optimizer,
                                    generator=generator,
                                    discriminator=discriminator)

    # Generate samples
    seed = tf.random.normal([N_EXAMPLES_TO_GENERATE, NOISE_DIM])

    @tf.function
    def train_step(images):
        noise = tf.random.normal([BATCH_SIZE, NOISE_DIM])

        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = generator(noise, training=True)

            real_output = discriminator(images, training=True)
            fake_output = discriminator(generated_images, training=True)

            gen_loss = generator_loss(fake_output)
            disc_loss = discriminator_loss(real_output, fake_output)
        
        gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

        generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

    def generate_and_save_images(model, epoch, test_input):
        # Notice `training` is set to False.
        # This is so all layers run in inference mode (batchnorm).
        predictions = model(test_input, training=False)

        fig = plt.figure(figsize=(4, 4))

        for i in range(predictions.shape[0]):
            plt.subplot(4, 4, i+1)
            plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
            plt.axis('off')

        plt.savefig('image_at_epoch_{:04d}.png'.format(epoch))
        plt.show()
    
    def train(dataset, epochs):
        for epoch in range(epochs):
            start = time.time()

            for image_batch in dataset:
                train_step(image_batch)
            
            # Produce images for the GIF
            display.clear_output(wait=True)
            generate_and_save_images(generator, epoch + 1, seed)
        
            # Save the model every 15 epochs
            if (epoch + 1) % 15 == 0:
                checkpoint.save(file_prefix = checkpoint_prefix)

            print('Time for epoch {} is {} sec'.format(epoch + 1, time.time()-start))

            # Generate after the final epoch
        display.clear_output(wait=True)
        generate_and_save_images(generator,
                                epochs,
                                seed)
    train(train_dataset, EPOCHS)

    checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

    # Create GIF
    # Display a single image using the epoch number
    def display_image(epoch_no):
        return PIL.Image.open('image_at_epoch_{:04d}.png'.format(epoch_no))
    display_image(EPOCHS)

    anim_file = 'dcgan.gif'

    with imageio.get_writer(anim_file, mode='I') as writer:
        filenames = glob.glob('image*.png')
        filenames = sorted(filenames)
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
        image = imageio.imread(filename)
        writer.append_data(image)

    import tensorflow_docs.vis.embed as embed
    embed.embed_file(anim_file)