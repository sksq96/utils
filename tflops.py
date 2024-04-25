checkpoint_activations_factor = 4
seq_len = 2048*2
batch_size = 2
elapsed_time_per_iteration = 7
parameters_in_billions_no_embedding = 8
tflops = parameters_in_billions_no_embedding * checkpoint_activations_factor * 2 * seq_len * batch_size / (elapsed_time_per_iteration * 1e3)
tflops
