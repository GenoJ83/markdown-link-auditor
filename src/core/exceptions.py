class AuditError(Exception): pass
class BrokenLinkError(AuditError): pass
class InvalidAnchorError(AuditError): pass
