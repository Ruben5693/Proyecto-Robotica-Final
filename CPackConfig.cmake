# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


SET(CPACK_BINARY_7Z "")
SET(CPACK_BINARY_BUNDLE "")
SET(CPACK_BINARY_CYGWIN "")
SET(CPACK_BINARY_DEB "")
SET(CPACK_BINARY_DRAGNDROP "")
SET(CPACK_BINARY_IFW "")
SET(CPACK_BINARY_NSIS "")
SET(CPACK_BINARY_OSXX11 "")
SET(CPACK_BINARY_PACKAGEMAKER "")
SET(CPACK_BINARY_RPM "")
SET(CPACK_BINARY_STGZ "")
SET(CPACK_BINARY_TBZ2 "")
SET(CPACK_BINARY_TGZ "")
SET(CPACK_BINARY_TXZ "")
SET(CPACK_BINARY_TZ "")
SET(CPACK_BINARY_WIX "")
SET(CPACK_BINARY_ZIP "")
SET(CPACK_CMAKE_GENERATOR "Unix Makefiles")
SET(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
SET(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
SET(CPACK_DEBIAN_BUILD_DEPENDS "debhelper, cmake, libgsl0-dev, libopenscenegraph-dev, cmake-qt-gui, freeglut3-dev, libboost-system-dev, libboost-thread-dev, openjdk-7-jre, libxt-dev, pyqt4-dev-tools, qt4-designer, qt4-dev-tools, zeroc-ice35, yakuake, python-pip, python-pyparsing, python-numpy, python-pyside, pyside-tools, libqt4-dev, qt4-qmake, libqt4-opengl-dev")
SET(CPACK_DEBIAN_CHANGELOG "  * Latest development version.")
SET(CPACK_DEBIAN_DISTRIBUTION_NAME "ubuntu")
SET(CPACK_DEBIAN_DISTRIBUTION_RELEASES "trusty;vivid")
SET(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "amd64")
SET(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA "/home/ruben/robocomp/debian/postinst;/home/ruben/robocomp/debian/preinst;/home/ruben/robocomp/debian/postrm")
SET(CPACK_DEBIAN_PACKAGE_DEPENDS "g++, libgsl0-dev, libopenscenegraph-dev, cmake-qt-gui, zeroc-ice35, freeglut3-dev, libboost-system-dev, libboost-thread-dev, qt4-dev-tools, yakuake, openjdk-7-jre, python-pip, python-pyparsing, python-numpy, python-pyside, pyside-tools, libxt-dev, pyqt4-dev-tools, qt4-designer, python-argcomplete")
SET(CPACK_DEBIAN_PACKAGE_PRIORITY "optional")
SET(CPACK_DEBIAN_PACKAGE_SECTION "devel")
SET(CPACK_GENERATOR "DEB")
SET(CPACK_INSTALL_CMAKE_PROJECTS "/home/ruben/robocomp;RoboComp;ALL;/")
SET(CPACK_INSTALL_PREFIX "/usr/local")
SET(CPACK_MODULE_PATH "/home/ruben/robocomp/cmake/modules/")
SET(CPACK_NSIS_DISPLAY_NAME "robocomp 1.01")
SET(CPACK_NSIS_INSTALLER_ICON_CODE "")
SET(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
SET(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
SET(CPACK_NSIS_PACKAGE_NAME "robocomp 1.01")
SET(CPACK_OUTPUT_CONFIG_FILE "/home/ruben/robocomp/CPackConfig.cmake")
SET(CPACK_PACKAGE_CONTACT "Luis J. Manso <lmanso@unex.es>")
SET(CPACK_PACKAGE_DEFAULT_LOCATION "/")
SET(CPACK_PACKAGE_DESCRIPTION_FILE "/home/ruben/robocomp/debian/README.Debian")
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Robotics Framework")
SET(CPACK_PACKAGE_FILE_NAME "robocomp-1.01-ubuntu")
SET(CPACK_PACKAGE_INSTALL_DIRECTORY "robocomp 1.01")
SET(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "robocomp 1.01")
SET(CPACK_PACKAGE_NAME "robocomp")
SET(CPACK_PACKAGE_RELOCATABLE "true")
SET(CPACK_PACKAGE_VENDOR "https://github.com/robocomp/robocomp")
SET(CPACK_PACKAGE_VERSION "1.01")
SET(CPACK_PACKAGE_VERSION_MAJOR "0")
SET(CPACK_PACKAGE_VERSION_MINOR "1")
SET(CPACK_PACKAGE_VERSION_PATCH "1")
SET(CPACK_RESOURCE_FILE_LICENSE "/home/ruben/robocomp/debian/copyright")
SET(CPACK_RESOURCE_FILE_README "/usr/share/cmake-3.5/Templates/CPack.GenericDescription.txt")
SET(CPACK_RESOURCE_FILE_WELCOME "/usr/share/cmake-3.5/Templates/CPack.GenericWelcome.txt")
SET(CPACK_SET_DESTDIR "OFF")
SET(CPACK_SOURCE_7Z "")
SET(CPACK_SOURCE_CYGWIN "")
SET(CPACK_SOURCE_GENERATOR "TBZ2;TGZ;TXZ;TZ")
SET(CPACK_SOURCE_IGNORE_FILES ".git")
SET(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/home/ruben/robocomp/CPackSourceConfig.cmake")
SET(CPACK_SOURCE_TBZ2 "ON")
SET(CPACK_SOURCE_TGZ "ON")
SET(CPACK_SOURCE_TXZ "ON")
SET(CPACK_SOURCE_TZ "ON")
SET(CPACK_SOURCE_ZIP "OFF")
SET(CPACK_SYSTEM_NAME "Linux")
SET(CPACK_TOPLEVEL_TAG "Linux")
SET(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "/home/ruben/robocomp/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()
