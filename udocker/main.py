#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
========
udocker
========
Wrapper to execute basic docker containers without using docker.
This tool is a last resort for the execution of docker containers
where docker is unavailable. It only provides a limited set of
functionalities.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])) + '/../')
from udocker.cli import UdockerCLI
from udocker.container.localrepo import LocalRepository
from udocker.config import Config


class Main(object):
    """Implements most of the command line interface.
    These methods correspond directly to the commands that can
    be invoked via the command line interface.
    """

    @staticmethod
    def do_help():
        """
        Print help information
        """

        print(
            """
Syntax:
  udocker  [general_options] <command>  [command_options]  <command_args>

  udocker [-h|--help|help]        :Display this help and exits
  udocker [-V|--version|version]  :Display udocker version and tarball version and exits

Commands:
  search <repo/image:tag>       :Search dockerhub for container images
  pull <repo/image:tag>         :Pull container image from dockerhub
  images                        :List container images
  create <repo/image:tag>       :Create container from a pulled image
  ps                            :List created containers
  rm  <container>               :Delete container
  run <container>               :Execute container
  inspect <container>           :Low level information on container
  name <container_id> <name>    :Give name to container
  rmname <name>                 :Delete name from container

  rmi <repo/image:tag>          :Delete image
  rm <container-id>             :Delete container
  import <tar> <repo/image:tag> :Import tar file (exported by docker)
  import - <repo/image:tag>     :Import from stdin (exported by docker)
  load -i <exported-image>      :Load image from file (saved by docker)
  load                          :Load image from stdin (saved by docker)
  export -o <tar> <container>   :Export container rootfs to file
  export - <container>          :Export container rootfs to stdin
  inspect <repo/image:tag>      :Return low level information on image
  verify <repo/image:tag>       :Verify a pulled image
  clone <container>             :duplicate container

  protect <repo/image:tag>      :Protect repository
  unprotect <repo/image:tag>    :Unprotect repository
  protect <container>           :Protect container
  unprotect <container>         :Unprotect container

  mkrepo <topdir>               :Create repository in another location
  setup                         :Change container execution settings
  login                         :Login into docker repository
  logout                        :Logout from docker repository

  help [command]                :Command specific help

Options common to all commands must appear before the command:
  -D                            :Debug
  --quiet                       :Less verbosity
  --repo=<directory>            :Use repository at directory

Examples:
  udocker search fedora
  udocker pull fedora
  udocker create --name=fed  fedora
  udocker run  fed  cat /etc/redhat-release
  udocker run --hostauth --hostenv --bindhome  fed
  udocker run --user=root  fed  yum install firefox
  udocker run --hostauth --hostenv --bindhome fed   firefox
  udocker run --hostauth --hostenv --bindhome fed   /bin/bash -i
  udocker run --user=root  fed  yum install cheese
  udocker run --hostauth --hostenv --bindhome --dri fed  cheese
  udocker --repo=/home/x/.udocker  images
  udocker -D run --user=1001:5001  fedora
  udocker export -o fedora.tar fedora
  udocker import fedora.tar myfedoraimage
  udocker create --name=myfedoracontainer myfedoraimage
  udocker export -o fedora_all.tar --clone fedora
  udocker import --clone fedora_all.tar

Notes:
  * by default the binaries, images and containers are placed in
       $HOME/.udocker
  * by default the following host directories are mounted in the
    container:
       /dev /proc /sys
       /etc/resolv.conf /etc/host.conf /etc/hostname
  * to prevent the mount of the above directories use:
       run  --nosysdirs  <container>
  * additional host directories to be mounted are specified with:
       run --volume=/data:/mnt --volume=/etc/hosts  <container>
       run --nosysdirs --volume=/dev --volume=/proc  <container>

See: https://github.com/indigo-dc/udocker/blob/master/SUMMARY.md
            """)
        return True
