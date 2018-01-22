if(NOT EXISTS "/home/ruben/robocomp/install_manifest.txt")
    message(FATAL_ERROR "Cannot find install manifest: \"/home/ruben/robocomp/install_manifest.txt\"")
endif(NOT EXISTS "/home/ruben/robocomp/install_manifest.txt")

file(READ "/home/ruben/robocomp/install_manifest.txt" files)
string(REGEX REPLACE "\n" ";" files "${files}")
foreach(file ${files})
    message(STATUS "Uninstalling \"$ENV{DESTDIR}${file}\"")
    message(STATUS "Uninstalling \"$ENV{DESTDIR}${file}\"")
    if(EXISTS "$ENV{DESTDIR}${file}" OR IS_SYMLINK "$ENV{DESTDIR}${file}")
        exec_program("/usr/bin/cmake" ARGS "-E remove \"$ENV{DESTDIR}${file}\""
            OUTPUT_VARIABLE rm_out RETURN_VALUE rm_retval)
        if(NOT "${rm_retval}" STREQUAL 0)
            message(FATAL_ERROR "Problem when removing \"$ENV{DESTDIR}${file}\"")
        endif(NOT "${rm_retval}" STREQUAL 0)
    else(EXISTS "$ENV{DESTDIR}${file}" OR IS_SYMLINK "$ENV{DESTDIR}${file}")
        message(STATUS "File \"$ENV{DESTDIR}${file}\" does not exist.")
    endif(EXISTS "$ENV{DESTDIR}${file}" OR IS_SYMLINK "$ENV{DESTDIR}${file}")
endforeach(file)

# remove RoboComp install directory include (removes all files in it!)
message(STATUS "Uninstalling \"/opt/robocomp\" and everything on it")
if(EXISTS "/opt/robocomp")
    exec_program("/usr/bin/cmake"
        ARGS "-E remove_directory \"/opt/robocomp\""
        OUTPUT_VARIABLE rm_out RETURN_VALUE rm_retval)
    if(NOT "${rm_retval}" STREQUAL 0)
        message(FATAL_ERROR
            "Problem when removing \"/opt/robocomp\"")
    endif(NOT "${rm_retval}" STREQUAL 0)
else(EXISTS "/opt/robocomp")
    message(STATUS
        "Directory \"/opt/robocomp\" does not exist.")
endif(EXISTS "/opt/robocomp")
