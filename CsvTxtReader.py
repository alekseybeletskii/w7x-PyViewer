# /*
#  * ******************** BEGIN LICENSE BLOCK *********************************
#  *
#  * w7x-dataViewer
#  * Copyright (c) 2017 onward, Aleksey Beletskii  <beletskiial@gmail.com>
#  * All rights reserved
#  *
#  * github: https://github.com/alekseybeletskii
#  *
#  * The w7x-dataViewer software serves for visualization and simple processing
#  * of any data recorded with Analog Digital Converters in binary or text form.
#  *
#  * Commercial support is available. To find out more contact the author directly.
#  *
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  *
#  *     1. Redistributions of source code must retain the above copyright notice, this
#  *          list of conditions and the following disclaimer.
#  *     2. Redistributions in binary form must reproduce the above copyright notice,
#  *         this list of conditions and the following disclaimer in the documentation
#  *         and/or other materials provided with the distribution.
#  *
#  * The software is distributed to You under terms of the GNU General Public
#  * License. This means it is "free software". However, any program, using
#  * ADCDataViewer _MUST_ be the "free software" as well.
#  * See the GNU General Public License for more details
#  * (file ./COPYING in the root of the distribution
#  * or website <http://www.gnu.org/licenses/>)
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  *
#  * ******************** END LICENSE BLOCK ***********************************
#  */
#


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os.path as ospath

from PyQt5 import QtGui, QtWidgets


import sys

import numpy as np

import pandas as pd

import MDSplus as m

import pyqtgraph as pg

from scipy import signal
import matplotlib.pyplot as plt
import pyqtgraph

from scipy.signal import savgol_filter


class CsvTxtReader(QtWidgets.QMainWindow):

   def __init__(self,  *args, **kwargs):
       super().__init__(*args, **kwargs)

   def openCsvTxt(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #        files, _ = QFileDialog.getOpenFileNames(None,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        #         files, _ = QFileDialog.getOpenFileNames(None,"QFileDialog.getOpenFileNames()", "csv files (*.csv)","csv files (*.csv);;All Files (*)", options=options)
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, None, "QFileDialog.getOpenFileNames()", "All Files (*)",
                                                     "All Files (*)", options=options)
        d = []
        t = []
        for i in range(len(files)):
            dataTxt = pd.read_csv(files[i], names=['x', 'y'], header=None)
            d.append(dataTxt['y'])
            t.append(dataTxt['x'])
        return t, d


