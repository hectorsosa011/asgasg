# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NuevoNido
                                 A QGIS plugin
 Agrega un nuevo nido de colibri y crea un buffer a su alrededor
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-04
        copyright            : (C) 2021 by Hecctor Sosa
        email                : hososa@unah.hn
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NuevoNido class from file NuevoNido.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .nuevo_nido import NuevoNido
    return NuevoNido(iface)
