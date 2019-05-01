The `` `casm status` `` command is very useful for getting information about the current status of a project. The `` `-n` `` option also gives suggestions for the next steps that you might take for the workflow of a typical CASM project. At this point, the command just indicates that no project has been initialized.

```
$ casm status -n
```
<details><summary markdown="span">See result</summary>

```
$ casm status -n

#################################

CASM status:

1) Project initialized: FALSE


#################################

NEXT STEPS:

Initialize a CASM project
- Create and cd to the directory where you want the project to be located.
  This will be called the 'project root directory' or project's 'location'.
- Add a 'prim.json' file to the directory describing the primitive cell.  
  See 'casm format --prim' for the format of the 'prim.json' file.        
- Execute: 'casm init'                                                    
- Several directories are created: 'symmetry', 'basis_sets',              
  'training_data', and 'cluster_expansions'  
- If necessary, set configuration options for runtime compilation and     
  linking by using the 'casm settings' command or by setting environment  
  variables. 
                                                                          
    'cxx': 
      Specifies compiler to use. In order of priority: 
        1) User specified by 'casm settings --set-cxx' (use '' to clear) 
        2) $CASM_CXX 
        3) $CXX 
        4) "g++" 

    'cxxflags': 
      Compiler flags. In order of priority: 
        1) User specified by 'casm settings --set-cxxflags' 
        2) $CASM_CXXFLAGS 
        3) "-O3 -Wall -fPIC --std=c++11" 

    'soflags': 
      Shared object construction flags. In order of priority: 
        1) User specified by 'casm settings --set-soflags' 
        2) $CASM_SOFLAGS 
        3) "-shared -lboost_system" 

    'casm headers and libraries': 
      CASM header files and shared libraries are expected in the following
      locations.                                                          
      In order of priority: 
        1) User specified by 'casm settings --set-casm-includedir' and 
           'casm settings --set-casm-libdir' 
        2) $CASM_INCLUDEDIR and $CASM_LIBDIR 
        3) $CASM_PREFIX/include and $CASM_PREFIX/lib 
        3) (default search paths) 

    Note: For the 'casm' Python package, $LIBCASM and $LIBCCASM, have 
    highest priority for locating libcasm and libccasm, respectively. 

    'boost headers and libraries': 
      The boost libraries are expected in the following locations.        
      In order of priority: 
        1) User specified by 'casm settings --set-boost-includedir' and 
           'casm settings --set-boost-libdir' and 
        2) $CASM_BOOST_INCLUDEDIR and $CASM_BOOST_LIBDIR 
        3) $CASM_BOOST_PREFIX/include $CASM_BOOST_PREFIX/lib 
        4) (default search paths) 

    Note: If shared libraries are installed in non-standard locations, you 
    may need to set: 
      (Linux) export LD_LIBRARY_PATH=$CASM_PREFIX/lib:$CASM_BOOST_PREFIX/lib:$LD_LIBRARY_PATH 
      (Mac)   export DYLD_FALLBACK_LIBRARY_PATH=$CASM_PREFIX/lib:$CASM_BOOST_PREFIX/lib:$DYLD_FALLBACK_LIBRARY_PATH 

- Subsequently, work on the CASM project can be done by executing 'casm'  
  from the project's root directory or any subdirectory.                  
- See 'casm format --prim' for description and location of the 'prim.json' file.
```
</details>
<br>
