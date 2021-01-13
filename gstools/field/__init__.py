# -*- coding: utf-8 -*-
"""
GStools subpackage providing tools for spatial random fields.

.. currentmodule:: gstools.field

Subpackages
^^^^^^^^^^^

.. autosummary::
    generator
    upscaling
    base

Spatial Random Field
^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   SRF
   CondSRF

----
"""

from gstools.field.srf import SRF
from gstools.field.cond_srf import CondSRF

__all__ = ["SRF", "CondSRF"]
