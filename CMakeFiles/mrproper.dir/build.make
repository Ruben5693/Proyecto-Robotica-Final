# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ruben/robocomp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ruben/robocomp

# Utility rule file for mrproper.

# Include the progress variables for this target.
include CMakeFiles/mrproper.dir/progress.make

CMakeFiles/mrproper:
	/usr/bin/make clean
	find /home/ruben/robocomp -name CMakeFiles -exec rm -rf {} \;
	find /home/ruben/robocomp -name CMakeCache.txt -exec rm {} \;
	find /home/ruben/robocomp -name cmake_install.cmake -exec rm {} \;
	find /home/ruben/robocomp -name Makefile -exec rm {} \;
	find /home/ruben/robocomp -name *.kd* -exec rm {} \;
	find /home/ruben/robocomp -name *_moc* -exec rm {} \;
	find /home/ruben/robocomp -name Makefile -exec rm {} \;

mrproper: CMakeFiles/mrproper
mrproper: CMakeFiles/mrproper.dir/build.make

.PHONY : mrproper

# Rule to build all files generated by this target.
CMakeFiles/mrproper.dir/build: mrproper

.PHONY : CMakeFiles/mrproper.dir/build

CMakeFiles/mrproper.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mrproper.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mrproper.dir/clean

CMakeFiles/mrproper.dir/depend:
	cd /home/ruben/robocomp && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ruben/robocomp /home/ruben/robocomp /home/ruben/robocomp /home/ruben/robocomp /home/ruben/robocomp/CMakeFiles/mrproper.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/mrproper.dir/depend

