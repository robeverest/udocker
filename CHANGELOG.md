# udocker (1.1.3)
  * Support for nvidia drivers on ubuntu
    - closes: #162
  * Installation improvements
    - closes: #166
  * Fix issue on Fn mode symlink convertion
    - partially addresses: #160

# udocker (1.1.2)
  * Improve parsing of quotes in the command line
    - closes: #98
  * Fix version command to exit with 0
    - closes: #107
  * Add kill-on-exit to proot on Pn modes
  * Improve download of udocker utils
  * Handle authentication headers when pulling 
    - closes: #110
  * Handle of redirects when pulling
  * Fix registries table
  * Support search quay.io
  * Fix auth header when no standard Docker registry is used
  * Add registry detection on image name
  * Add --version option
  * Force python2 as interpreter
    - closes: #131
  * Fix handling of volumes in metadata
  * Handle empty metadata
  * Fix http proxy functionality
    - closes: #115
  * Ignore --no-trunc and --all in the images command
    - closes: #108
  * Implement verification of layers in manifest
  * Add --nvidia to support GPUs and related drivers
  * Send download messages to stderr
  * Enable override of curl executable
  * Fix building on CentOS 6
    - closes: #157
  * Mitigation for upstream limitation in runC without tty
    - closes: #132
  * Fix detection of executable with symlinks in container
    - closes: #118
  * Updated runC to v1.0.0-rc5
  * Experimental support for Alpine in Fn modes
  * Improve pathname translation in Fn modes for mounted dirs
    - partially addresses: #160

# udocker (1.1.1)

  * New execution engine using singularity
  * Updated documentation with OpenMPI information and examples
  * Additional unit tests
  * Redirect messages to stderr
  * Improved parsing of quotes in the command line
    - closes: #87
  * Allow override of the HOME environment variable
  * Allow override of libfakechroot.so at the container level
  * Automatic selection of libfakechroot.so from container info
  * Improve automatic install
  * Enable resetting prefix paths in Fn modes in remote hosts
  * Do not set AF_UNIX_PATH in Fn modes when the host /tmp is a volume
  * Export containers in both docker and udocker format
  * Import containers docker and udocker format
  * Load, import and export to/from stdin/stdout
  * Clone existing containers
  * Support for TCP/IP port remap in execution modes Pn
  * Fix run with basenames failing
    - closes: #89
  * Allow run as root flag
    - closes: #91

# udocker (1.1.0)

  * Support image names prefixed by registry similarly to docker 
  * Add execution engine selection logic
  * Add fr execution engine based on shared library interception
  * Add rc execution engine based on rootless namespaces
  * Improve proot tmp files cleanup on non ext filesystems
  * Improve search returning empty on Docker repositories
  * Improve runC execution portability 
  * Add environment variable UDOCKER_KEYSTORE
    - closes: #75
  * Prevent creation of .udocker when UDOCKER_KEYSTORE is used
    - closes: #75

# udocker (1.0.4)

  * Documentation fixes

# udocker (1.0.3)

  * Support for import Docker containers in newer metadata structure
  * Improve the command line parsing
  * Improve temporary file handling and removal
  * Support for additional execution engines to be provided in the future
  * Improved parsing of entrypoint and cmd metadata
    - closes: #53
  * Increase name alias length
    - closes: #52
  * Add support for change dir into volume directories
    - closes: #51
  * Fix deletion of files upon container import
    - closes: #50
  * Fix exporting of host environment variables to the containers
    - closes: #48
  * Change misleading behavior of import tarball from move to copy
    - closes: #44
  * Fix validation of volumes specification
    - closes: #43

# udocker (1.0.2)

  * Improve download on repositories that fail authentication on /v2
  * Improve run verification of binaries with recursive symbolic links
  * Improve accelerated seccomp on kernels >= 4.8.0
    - closes: #40

# udocker (1.0.1)

  * Minor bugfixes
  * Executable name changed from udocker.py to udocker
  * Added support for login into docker repositories
  * Added support for private repositories
  * Added support for listing of v2 repositories catalog
  * Added checksum verification for sha256 layers
  * Improved download handling for v1 and v2 repositories
  * Improved installation tarball structure
  * Insecure flag fixed
  * Address seccomp change introduced on kernels >= 4.8.0
  * Utilities for packaging
  * Improved verbose levels, messaging and output
    - closes: #24, #23
  * Fully implement support for registry selection --registry parameter
    - closes: #29
  * Provide support for private repositories e.g. gitlab registries
    - closes: #30
  * Provide --insecure command line parameter for SSL requests
    - closes: #31

# udocker (1.0.0)

  * Initial version
