from . import data, business
from .application import handle
# Interface pública do módulo (outros módulos só usam isto)
init, reservar, repor = data.init, business.reservar, business.repor
