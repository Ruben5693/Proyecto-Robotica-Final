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

# Utility rule file for ui_kinectDlg.

# Include the progress variables for this target.
include tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/progress.make

tools/rcmonitor/CMakeFiles/ui_kinectDlg: tools/rcmonitor/ui_kinectDlg.py


tools/rcmonitor/ui_kinectDlg.py: tools/rcmonitor/kinectDlg.ui
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ruben/robocomp/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating ui_kinectDlg.py from kinectDlg.ui"
	cd /home/ruben/robocomp/tools/rcmonitor && pyuic4 /home/ruben/robocomp/tools/rcmonitor/kinectDlg.ui -o ui_kinectDlg.py

ui_kinectDlg: tools/rcmonitor/CMakeFiles/ui_kinectDlg
ui_kinectDlg: tools/rcmonitor/ui_kinectDlg.py
ui_kinectDlg: tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/build.make

.PHONY : ui_kinectDlg

# Rule to build all files generated by this target.
tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/build: ui_kinectDlg

.PHONY : tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/build

tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/clean:
	cd /home/ruben/robocomp/tools/rcmonitor && $(CMAKE_COMMAND) -P CMakeFiles/ui_kinectDlg.dir/cmake_clean.cmake
.PHONY : tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/clean

tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/depend:
	cd /home/ruben/robocomp && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ruben/robocomp /home/ruben/robocomp/tools/rcmonitor /home/ruben/robocomp /home/ruben/robocomp/tools/rcmonitor /home/ruben/robocomp/tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tools/rcmonitor/CMakeFiles/ui_kinectDlg.dir/depend

