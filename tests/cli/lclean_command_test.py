import os
import sys
from unittest import mock

sys.path.insert(0, './')

from src.Kathara.cli.command.LcleanCommand import LcleanCommand


@mock.patch("src.Kathara.manager.Kathara.Kathara.undeploy_lab")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
@mock.patch("src.Kathara.model.Lab.Lab")
def test_run_no_params(mock_lab, mock_parse_lab, mock_undeploy_lab):
    mock_parse_lab.return_value = mock_lab
    command = LcleanCommand()
    command.run('.', [])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_undeploy_lab.assert_called_once_with(lab_hash=mock_lab.hash, selected_machines=None)


@mock.patch("src.Kathara.manager.Kathara.Kathara.undeploy_lab")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
@mock.patch("src.Kathara.model.Lab.Lab")
def test_run_with_directory(mock_lab, mock_parse_lab, mock_undeploy_lab):
    mock_parse_lab.return_value = mock_lab
    command = LcleanCommand()
    command.run('.', ['-d', '/test/path'])
    mock_parse_lab.assert_called_once_with('/test/path')
    mock_undeploy_lab.assert_called_once_with(lab_hash=mock_lab.hash, selected_machines=None)


@mock.patch("src.Kathara.manager.Kathara.Kathara.undeploy_lab")
@mock.patch("src.Kathara.parser.netkit.LabParser.LabParser.parse")
@mock.patch("src.Kathara.model.Lab.Lab")
def test_run_with_selected_machines(mock_lab, mock_parse_lab, mock_undeploy_lab):
    mock_parse_lab.return_value = mock_lab
    command = LcleanCommand()
    command.run('.', ['pc1', 'pc2'])
    mock_parse_lab.assert_called_once_with(os.getcwd())
    mock_undeploy_lab.assert_called_once_with(lab_hash=mock_lab.hash, selected_machines={'pc1', 'pc2'})
