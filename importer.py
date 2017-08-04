#!/usr/bin/env python
# coding=utf-8


import cv2
import numpy as np
import operator
import os
import sys
import array
import Words


MIN_CONTOUR_AREA = 15 #20             CHANGE TO 30-45 FOR NOISY IMAGE
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

from class_contour import *
from Height_matters import *
import word_segmenter3
import tnt_0_O6_compound
import SecondPostprocessing

import LevenShtein_Distance
