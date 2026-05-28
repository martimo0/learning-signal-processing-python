Learning Basic Signal Processing through Python.

Dedicated time to developing practical signal processing skills using Python alongside my EEE degree whilst awaiting delivery for hardware for more complex projects.

Topics Covered: Signal Generation, Graph Plotting, Fourier Transform Application, Sounding out waves, Nyquist-Shannon Sampling Theorem, White + Gaussian Noise Generation,
Band-Pass Filter (BPF) and Bode Plots.

01 - Signal Generation using numpy to construct a 5 Hz sine wave and plotting it on a graph to visually display the sine wave using matplotlib.

02 - Constructing a composite wave by combining a 10 Hz wave and a 40 Hz wave and then plotting it along with a square and sine wave with scipy.

03 - Fourier Transform Application onto a composite wave using fast fourier transforms which have an o complexity of o(nlog(n)) compared to o(n^2) making it significantly
faster. The result showed the two frequencies that created the composite wave, the 10 and 40 Hz waves originally used in 02 to create the composite wave.

04 - Fourier Transform of a square wave to show the infinite odd harmonics ladder produced from the mathematical operation which I found to be very interesting and inspired
me to research sound analysis, specifically frequency modulation and phase distortion.

05 = Making use of the sounddevice library to actually produce the sound of a sine and square wave to hear them and have a clearer understanding of the infinite harmonies
mentioned in 04 as they are all heard at the same time and cause that "buzzing" sound.

06 - This section focuses on the Nyquist-Shannon Sampling Theorem which states that the sampling rate should be double the highest frequency that is to be represented.
Therefore, a sine wave of 40 Hz was constructed and then sampled as shown in the graphs. The first sample the "good" sampling was at 500 Hz and created a near identical
reconstructed wave as it's well above the 80 Hz sampling rate suggested by the aforementioned therorem. The second sample used a sampling rate of 45 Hz (which is below 80 Hz)
and produced a very poor representation of the original frequency (it looks nothing alike).

07 - For part 07, it begins with the generation of white noise which was then smoothed by a low-pass filter which filters out all of the high frequencies. The cutoff frequency
was at 50 Hz only allowing frequencies below that (in theory). The Fourier transform is nearly the same but with the other frequencies being less prevalent due to the smoothing.

08 - Guassian noise was implemented in this section and the graphs clearly show the effects of the filters when it comes to filtering out unwanted frequencies but I was just
overall curious about Gaussian noise.

09 - For this part, the idea was to recreate the Butterworth Band-Pass filter for which I previously created with frequency cutoffs at 200 Hz and 4800 Hz using KiCad and creating the PCB
schematic.

10 - This is the logarithmic AC Sweep with 10 points per decade. The high-pass filter seems to have a sharper corner than the low-pass filter most likely due to the scaling of
the frequency but still produced the correct form nonetheless. 

Requirements:
pip install -r requirements.txt

How to run:
Clone the repo, install the requirements, run the code using a Python IDE.

What's next:
Construction of a physical and digital Synthesizer, Frequency Modulation, Phase Distortion.

Overall, this was a useful and educational project to further dive into the topic of Signal Processing and see some basic Python applications of it.
