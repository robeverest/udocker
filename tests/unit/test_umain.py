#!/usr/bin/env python
"""
udocker unit tests: UMain
"""

import sys
from unittest import TestCase, main
try:
    from unittest.mock import Mock, patch, MagicMock, mock_open
except ImportError:
    from mock import Mock, patch, MagicMock, mock_open

sys.path.append('.')

from udocker.config import Config
from udocker.umain import UMain


class UMainTestCase(TestCase):
    """Test UMain() class main udocker program."""

    def setUp(self):
        self.conf = Config().getconf()
        self.conf['hostauth_list'] = ("/etc/passwd", "/etc/group")
        self.conf['cmd'] = "/bin/bash"
        self.conf['cpu_affinity_exec_tools'] = (["numactl", "-C", "%s", "--", ],
                                                ["taskset", "-c", "%s", ])
        ## Config.cpu_affinity_exec_tools = ("taskset -c ", "numactl -C ")
        self.conf['valid_host_env'] = "HOME"
        self.conf['username'] = "user"
        self.conf['userhome'] = "/"
        self.conf['oskernel'] = "4.8.13"
        self.conf['location'] = ""
        self.conf['verbose_level'] = 3
        self.conf['http_insecure'] = False
        self.conf['topdir'] = "/.udocker"


    def tearDown(self):
        pass

    @patch('udocker.msg.Msg')
    @patch('udocker.cmdparser.CmdParser.parse')
    def test_01_init(self, mock_parse, mock_msg):
        """Test UMain() constructor."""
        # argv = "--allow-root"
        argv = None
        mock_parse.return_value = False
        with self.assertRaises(SystemExit) as mainexpt:
            UMain(argv)
        self.assertEqual(mainexpt.exception.code, 0)

    # @patch('udocker.container.localrepo.LocalRepository')
    # @patch('udocker.cli.UdockerCLI')
    # @patch('udocker.config.Config.user_init')
    # @patch('udocker.msg.Msg')
    # @patch('udocker.cmdparser.CmdParser')
    # def test_02_init(self, mock_cmdp, mock_msg, mock_conf_init, mock_udocker,
    #                  mock_localrepo):
    #     """Test UMain() constructor."""
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, False,
    #                                               False, False, False, False,
    #                                               False]
    #     UMain()
    #     self.assertEqual(udocker.Config.verbose_level, 3)
    #     # --debug
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, True, False,
    #                                               False, False, False, False,
    #                                               False]
    #     UMain()
    #     self.assertNotEqual(udocker.Config.verbose_level, 3)
    #     # -D
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, True,
    #                                               False, False, False, False,
    #                                               False]
    #     UMain()
    #     self.assertNotEqual(udocker.Config.verbose_level, 3)
    #     # --quiet
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, False,
    #                                               True, False, False, False,
    #                                               False]
    #     UMain()
    #     self.assertNotEqual(udocker.Config.verbose_level, 3)
    #     # -q
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, False,
    #                                               False, True, False, False,
    #                                               False]
    #     UMain()
    #     self.assertNotEqual(udocker.Config.verbose_level, 3)
    #     # --insecure
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, False,
    #                                               False, False, True, False,
    #                                               False, False]
    #     UMain()
    #     self.assertTrue(udocker.Config.http_insecure)
    #     # --repo=
    #     mock_localrepo.return_value.is_repo.return_value = True
    #     mock_cmdp.return_value.parse.return_value = True
    #     mock_cmdp.return_value.get.side_effect = [False, False, False, False,
    #                                               False, False, False, True,
    #                                               "/TOPDIR"]
    #     with self.assertRaises(SystemExit) as mainexpt:
    #         UMain()
    #     self.assertEqual(mainexpt.exception.code, 0)
    #
    #
    # @patch('udocker.UMain.__init__')
    # @patch('udocker.container.localrepo.LocalRepository')
    # @patch('udocker.cli.UdockerCLI')
    # @patch('udocker.msg.Msg')
    # @patch('udocker.cmdparser.CmdParser')
    # def test_03_execute(self, mock_cmdp, mock_msg, mock_udocker,
    #                     mock_localrepo, mock_main_init):
    #     """Test UMain().execute()."""
    #     self._init()
    #     mock_main_init.return_value = None
    #     mock_cmdp.return_value.get.side_effect = [True, False, False, False,
    #                                               False, False, False, False]
    #     umain = UMain()
    #     umain.udocker = mock_udocker
    #     umain.cmdp = mock_cmdp
    #     status = umain._execute()
    #     self.assertEqual(status, 0)
    #     #
    #     mock_main_init.return_value = None
    #     mock_cmdp.return_value.get.side_effect = [False, True, False, False,
    #                                               False, False, False, False]
    #     umain = UMain()
    #     umain.udocker = mock_udocker
    #     umain.cmdp = mock_cmdp
    #     status = umain._execute()
    #     self.assertEqual(status, 0)
    #     #
    #     mock_main_init.return_value = None
    #     mock_cmdp.return_value.get.side_effect = [False, False, "ERR", False,
    #                                               False, False, False, False]
    #     umain = UMain()
    #     umain.udocker = mock_udocker
    #     umain.cmdp = mock_cmdp
    #     umain.cmdp.reset_mock()
    #     status = umain._execute()
    #     self.assertTrue(umain.udocker.do_help.called)
    #     #
    #     mock_main_init.return_value = None
    #     mock_cmdp.return_value.get.side_effect = [False, False, "run", True,
    #                                               False, False, False, False]
    #     umain = UMain()
    #     umain.udocker = mock_udocker
    #     umain.cmdp = mock_cmdp
    #     umain.cmdp.reset_mock()
    #     status = umain.execute()
    #     self.assertTrue(umain.udocker.do_help.called)

    # @patch('udocker.UMain.__init__')
    # @patch('udocker.UMain._execute')
    # @patch('udocker.utils.fileutil.FileUtil')
    # @patch('udocker.msg.Msg')
    # def test_04_start(self, mock_msg, mock_futil, mock_main_execute,
    #                   mock_main_init):
    #     """Test UMain().start()."""
    #     mock_main_init.return_value = None
    #     mock_main_execute.return_value = 2
    #     umain = UMain()
    #     status = umain.start()
    #     self.assertEqual(status, 2)
    #     #
    #     mock_main_init.return_value = None
    #     mock_main_execute.return_value = 2
    #     mock_main_execute.side_effect = KeyboardInterrupt("CTRLC")
    #     umain = UMain()
    #     status = umain.start()
    #     self.assertEqual(status, 1)


if __name__ == '__main__':
    main()
