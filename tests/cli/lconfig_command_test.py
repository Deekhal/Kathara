import os
import sys
from unittest import mock

import pytest

sys.path.insert(0, './')

from src.Kathara.cli.command.LconfigCommand import LconfigCommand
from src.Kathara.model.Machine import Machine
from src.Kathara.model.Link import Link
from src.Kathara.model.Lab import Lab


@pytest.fixture()
def test_lab():
    lab = Lab('test_lab')
    device = Machine(lab, 'pc1')
    link_a = Link(lab, "A")
    link_b = Link(lab, "B")
    lab.machines['pc1'] = device
    lab.links = {'A': link_a, 'B': link_b}
    return lab


@mock.patch("src.Kathara.manager.Kathara.Kathara.connect_machine_to_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_add_link(mock_parse_lab, mock_update_lab_from_api, mock_connect_machine_to_link, test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-n', 'pc1', '--add', 'A'])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_connect_machine_to_link.assert_called_once_with(test_lab.get_or_new_machine('pc1'),
                                                         test_lab.get_or_new_link('A'))


@mock.patch("src.Kathara.manager.Kathara.Kathara.connect_machine_to_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_add_link_with_directory(mock_parse_lab, mock_update_lab_from_api, mock_connect_machine_to_link, test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-d', '/test/path', '-n', 'pc1', '--add', 'A'])
    mock_parse_lab.assert_called_once_with('/test/path')
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_connect_machine_to_link.assert_called_once_with(test_lab.get_or_new_machine('pc1'),
                                                         test_lab.get_or_new_link('A'))


@mock.patch("src.Kathara.manager.Kathara.Kathara.connect_machine_to_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_add_two_links(mock_parse_lab, mock_update_lab_from_api, mock_connect_machine_to_link, test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-n', 'pc1', '--add', 'A', 'B'])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_connect_machine_to_link.assert_any_call(test_lab.get_or_new_machine('pc1'),
                                                 test_lab.get_or_new_link('A'))
    mock_connect_machine_to_link.assert_any_call(test_lab.get_or_new_machine('pc1'),
                                                 test_lab.get_or_new_link('B'))


@mock.patch("src.Kathara.manager.Kathara.Kathara.disconnect_machine_from_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_remove_link(mock_parse_lab, mock_update_lab_from_api, mock_disconnect_machine_from_link, test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-n', 'pc1', '--rm', 'A'])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_disconnect_machine_from_link.assert_called_once_with(test_lab.get_or_new_machine('pc1'),
                                                              test_lab.get_or_new_link('A'))


@mock.patch("src.Kathara.manager.Kathara.Kathara.disconnect_machine_from_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_remove_link_with_directory(mock_parse_lab, mock_update_lab_from_api, mock_disconnect_machine_from_link,
                                        test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-d', '/test/path', '-n', 'pc1', '--rm', 'A'])
    mock_parse_lab.assert_called_once_with('/test/path')
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_disconnect_machine_from_link.assert_called_once_with(test_lab.get_or_new_machine('pc1'),
                                                              test_lab.get_or_new_link('A'))


@mock.patch("src.Kathara.manager.Kathara.Kathara.disconnect_machine_from_link")
@mock.patch("src.Kathara.manager.Kathara.Kathara.update_lab_from_api")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
def test_run_remove_two_links(mock_parse_lab, mock_update_lab_from_api, mock_disconnect_machine_from_link, test_lab):
    mock_parse_lab.return_value = test_lab
    command = LconfigCommand()
    command.run('.', ['-n', 'pc1', '--rm', 'A', 'B'])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_update_lab_from_api.assert_called_once_with(test_lab)
    mock_disconnect_machine_from_link.assert_any_call(test_lab.get_or_new_machine('pc1'),
                                                      test_lab.get_or_new_link('A'))
    mock_disconnect_machine_from_link.assert_any_call(test_lab.get_or_new_machine('pc1'),
                                                      test_lab.get_or_new_link('B'))


def test_run_system_exit_error():
    command = LconfigCommand()
    with pytest.raises(SystemExit):
        command.run('.', ['-n', 'pc1', '--rm', 'A', '--add', 'A'])
