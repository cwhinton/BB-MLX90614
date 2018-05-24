#!/usr/bin/env python
"""
  This file is part of Redeem - 3D Printer control software

  Author: Chad Hinton
  License: GNU GPLv3 http://www.gnu.org/copyleft/gpl.html


  This is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Redeem is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.

"""
import iio

ctx = iio.Context()
mlx = ctx.find_device('mlx90614')
temp_object = int((mlx.find_channel('temp_object')).attrs['raw'].value) / 50 - 273.15
print temp_object
temp_ambient = int((mlx.find_channel('temp_ambient')).attrs['raw'].value) / 50 - 273.15
print temp_ambient
