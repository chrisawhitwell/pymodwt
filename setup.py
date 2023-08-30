###########################################################################
#                                                                         #
#    Copyright 2016 Andrea Cimatoribus                                    #
#    ECOL, ENAC, IIE, EPFL                                                #
#    GR A1 435, Station 2, CH-1015 Lausanne, Switzerland                  #
#    andrea.cimatoribus@epfl.ch                                           #
#                                                                         #
#    This file is part of wmtsa toolbox.                                  #
#                                                                         #
#    wmtsa toolbox is free software: you can redistribute it              #
#    and/or modify it under the terms of the GNU General Public           #
#    License as published by the Free Software Foundation, either         #
#    version 3 of the License, or (at your option) any later version.     #
#                                                                         #
#    wmtsa toolbox is distributed in the hope that it will be             #
#    useful, but WITHOUT ANY WARRANTY; without even the implied warranty  #
#    of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
#    GNU General Public License for more details.                         #
#                                                                         #
#    You should have received a copy of the GNU General Public            #
#    License along with wmtsa.                                            #
#    If not, see <http://www.gnu.org/licenses/>.                          #
#                                                                         #
###########################################################################

from setuptools import setup, find_packages
import numpy


setup(	name = "wmtsapy3",
		author = 'Chris Whitwell',
		author_email = 'chris.whitwell@research.uwa.edu.au',
		cmdclass = {},
		packages=find_packages()
		)

