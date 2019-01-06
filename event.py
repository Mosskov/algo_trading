class Event(object):
    """
    Event is a base class providing an interface for all subsequent (inherited) events, that will trigger further events
    in the trading infrastructure.
    """
    pass


class MarketEvent(Event):
    """
    Handles the event of receiving a new market update with corresponding bars.
    """

    def __init__(self):
        """
        Initialises the MarketEvent.
        """
        self.type = 'MARKET'


class SignalEvent(Event):
    """
    Handles the event of sending a Signal from a Strategy object.
    This is received by a Portfolio object and acted upon.
    """

    def __init__(self, symbol, datetime, signal_type):
        """
        Initialises the SignalEvent.

        :param symbol: The ticker symbol, e.g. 'BTCUSD'
        :param datetime - The timestamp at which the signal was generated.
        :param signal_type - 'LONG' or 'SHORT'
        """

        self.type = 'SIGNAL'
        self.symbol = symbol
        self.datetime = datetime
        self.signal_type = signal_type


class OrderEvent(Event):
    """
    Handles the event of sending an Order to an execution system.
    The order contains a symbol (e.g. BTCUSD), a type (market or limit), quantity and a direction
    """

    def __init__(self, symbol, order_type, quantity, direction):
        """
        Initialises the order type, setting whether it is a Market order ('MKT') or a Limit order ('LMT'), has
        a quantity (float) and its direction ('BUY' or 'SELL')

        :param symbol: The instrument to trade.
        :param order_type: 'MKT' or 'LMT' for Market or Limit.
        :param quantity: Float value for quantity.
        :param direction: 'BUY' or 'SELL' for long or short.
        """

        self.type = 'ORDER'
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

    def print_order(self):
        """
        Outputs the values within the Order.
        """

        print("Order: Symbol=%s, Type=%s, Quantity=%s, Direction=%s" %
              (self.symbol, self.order_type, self.quantity, self.direction))


class FillEvent(Event):
    """
    Encapsulates the notion of a Filled Order, as returned from a brokerage. Stores the quantity of an instrument
    actually filled and at what price. In addition, stores the commission of the trade from the brokerage.
    """

    # TODO

    pass
