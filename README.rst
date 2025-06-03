.. image:: https://raw.githubusercontent.com/BonnBytes/PyTorch-FWD/refs/heads/master/images/fwd_logo.png
   :width: 25%
   :align: center
   :alt: FWD LOGO

Fréchet Wavelet Distance: A Domain-Agnostic Metric for Image Generation
**************************************************************************

`Lokesh Veeramacheneni <https://lokiv.dev>`__\ :sup:`1`, `Moritz
Wolter <https://www.wolter.tech/>`__\ :sup:`1`, `Hilde
Kuehne <https://hildekuehne.github.io/>`__\ :sup:`2`, and `Juergen
Gall <https://pages.iai.uni-bonn.de/gall_juergen/>`__\ :sup:`1,3`

| 1. *University of Bonn* 
| 2. *University of Tübingen, MIT-IBM Watson AI Lab*
| 3. *Lamarr Institute for Machine Learning and Artificial Intelligence*
|

|Docs| |License| |CodeStyle| |Workflow|  |Arxiv|  |Downloads|  |Project|

**Keywords:** Frechet Distance, Wavelet Packet Transform, FID, Diffusion, GAN, ImageNet, FD-DINOv2, 

**Abstract:** Modern metrics for generative learning like Fréchet Inception Distance (FID) and
DINOv2-Fréchet Distance (FD-DINOv2) demonstrate impressive performance.
However, they suffer from various shortcomings, like a bias towards specific generators and datasets. To address this problem, we propose the Fréchet Wavelet
Distance (FWD) as a domain-agnostic metric based on the Wavelet Packet Transform (:math:`W_p`). FWD provides a sight across a broad spectrum of frequencies in images
with a high resolution, preserving both spatial and textural aspects. Specifically,
we use (:math:`W_p`) to project generated and real images to the packet coefficient space. We
then compute the Fréchet distance with the resultant coefficients to evaluate the
quality of a generator. This metric is general-purpose and dataset-domain agnostic,
as it does not rely on any pre-trained network while being more interpretable due
to its ability to compute Fréchet distance per packet, enhancing transparency. We
conclude with an extensive evaluation of a wide variety of generators across various
datasets that the proposed FWD can generalize and improve robustness to domain
shifts and various corruptions compared to other metrics.


.. image:: https://raw.githubusercontent.com/BonnBytes/PyTorch-FWD/refs/heads/master/images/fwd_computation.png
   :width: 100%
   :alt: Alternative text

Installation
============

Install via pip 

.. code:: bash

   pip install pytorchfwd


Usage
=====

.. code:: bash

    python -m pytorchfwd <path to dataset> <path to generated images>

Here are the other arguments and defaults used.

.. code-block::

   python -m pytorchfwd --help
   
   usage: pytorchfwd.py [-h] [--batch-size BATCH_SIZE] [--num-processes NUM_PROCESSES] [--save-packets] [--wavelet WAVELET] [--max_level MAX_LEVEL] [--log_scale] path path
   
   positional arguments:
     path                  Path to the generated images or path to .npz statistics file.
   
   options:
     -h, --help            show this help message and exit
     --batch-size          Batch size for wavelet packet transform. (default: 128)
     --num-processes       Number of multiprocess. (default: None)
     --save-packets        Save the packets as npz file. (default: False)
     --wavelet             Choice of wavelet. (default: Haar)
     --max_level           wavelet decomposition level (default: 4)
     --log_scale           Use log scaling for wavelets. (default: False)

**We conduct all the experiments with `Haar` wavelet with transformation/decomposition level of `4` for `256x256` image.**
In future, we plan to release the jax-version of this code.

Citation
========
If you use this work, please cite using following bibtex entry

.. code-block::

  @inproceedings{
   veeramacheneni2025fwd,
   title={Fr\'echet Wavelet Distance: A Domain-Agnostic Metric for Image Generation},
   author={Lokesh Veeramacheneni and Moritz Wolter and Hildegard Kuehne and Juergen Gall},
   booktitle={The Thirteenth International Conference on Learning Representations},
   year={2025},
   url={https://openreview.net/forum?id=QinkNNKZ3b}}

Acknowledgments
===============

The code is built with inspiration from
`Pytorch-FID <https://github.com/mseitzer/pytorch-fid>`__. We use
`PyTorch Wavelet
Toolbox <https://github.com/v0lta/PyTorch-Wavelet-Toolbox>`__ for
Wavelet Packet Transform implementation. We recommend to have a look at
these repositories.

Testing
=======
The `tests` folder contains tests to conduct independent verification of FWD. Github workflow executes all these tests.
To run tests on your local system install `nox`, as well as this package via `pip install .`, and run

.. code-block:: sh

   nox -s test


.. |Workflow| image:: https://github.com/BonnBytes/PyTorch-FWD/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/BonnBytes/PyTorch-FWD/actions/workflows/tests.yml
.. |License| image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
.. |CodeStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Docs| image:: https://readthedocs.org/projects/pytorchfwd/badge/?version=latest
    :target: https://pytorchfwd.readthedocs.io/en/latest/index.html
    :alt: Documentation Status
.. |Project| image:: https://img.shields.io/badge/Project-Website-blue
   :target: https://lokiv.dev/frechet_wavelet_distance/
   :alt: Project Page
.. |Arxiv| image:: https://img.shields.io/badge/OpenReview-Paper-blue
   :target: https://openreview.net/pdf?id=QinkNNKZ3b
   :alt: Paper
.. |Downloads| image:: https://static.pepy.tech/badge/pytorchfwd
   :target: https://pepy.tech/projects/pytorchfwd


Funding
=======
This research was supported by the Federal Ministry of Education and Research (BMBF) under grant no.\ 01IS22094A WEST-AI and 6DHBK1022 BNTrAInee, the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) GA 1927/9-1 (KI-FOR 5351) and the ERC Consolidator Grant FORHUE (101044724). Prof. Kuehne is supported by BMBF project STCL - 01IS22067. The authors gratefully acknowledge the Gauss Centre for Supercomputing e.V.\ (www.gauss-centre.eu) for funding this project by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer JUWELS at Jülich Supercomputing Centre (JSC). The authors heartfully thank all the volunteers who participated in the user study. The sole responsibility for the content of this publication lies with the authors.
