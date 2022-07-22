# Generic Exceptions
class ClassNotFoundError(Exception):
    pass


class HTTPConnectionError(Exception):
    pass


# Settings Exceptions
class SettingsError(Exception):
    def __init__(self, message) -> None:
        super().__init__("Settings file is not valid: %s\nFix it or delete it before launching." % message)


class SettingsNotFound(Exception):
    pass


class DockerDaemonConnectionError(Exception):
    pass


class NotSupportedError(Exception):
    def __init__(self, message) -> None:
        super().__init__("Not Supported: %s" % message)


# OS Exceptions
class PrivilegeError(Exception):
    pass


# Lab Exceptions
class LabAlreadyExistsError(Exception):
    pass


# Machine Exceptions
class MountDeniedError(Exception):
    pass


class MachineAlreadyExistsError(Exception):
    pass


class NonSequentialMachineInterfaceError(Exception):
    pass


class MachineOptionError(Exception):
    pass


class MachineCollisionDomainConflictError(Exception):
    pass


# Test Exceptions
class TestError(Exception):
    pass


class MachineSignatureNotFoundError(TestError):
    pass


# Docker Exceptions
class InvalidImageArchitectureError(ValueError):
    __slots__ = ['arch']

    def __init__(self, arch):
        self.arch = arch
