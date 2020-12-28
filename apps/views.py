import json
import logging
import json
from django.shortcuts import render, redirect
from datetime import datetime
from power_stock.settings import kite, api_secret, token_cache
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def default(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()


def index(request):
    return render(request, "home/index.html")


def order_place(request):
    return render(request, 'home/place_order.html')


def dashboard(request):
    return render(request, "dashboard/index.html")


def logout(request):
    return render(request, 'home/index.html')


def place_order(name):
    try:
        try:
            order_id = kite.place_order(tradingsymbol=name, variety=kite.VARIETY_REGULAR,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_CNC)
            return order_id
        except Exception as e:
            logger.warning("Order placement failed: {}".format(e))
    except Exception as e:
        logger.error(e.__cause__)
        logger.error(e)
        return HttpResponse({"message": e.__cause__}, status=500)


def kite_login(request):
    try:
        token = token_cache.get("request_token", None)
        logger.info("Kite Existing Token: {0}".format(token))
        if token:
            start_time = datetime.now()
            name = request.GET.get('trading_symbol')
            logger.info("symbol name:{0}".format(name))
            if name:
                order_id = place_order(name)
                logger.info("order placed with id:{0}".format(order_id))
                orders = kite.orders()
                for order in orders:
                    if order_id == order['order_id']:
                        order_time = order['order_timestamp']
                        diff = order_time - start_time
                        logger.info("Time Difference is: {}".format(str(diff)))
                return render(request, 'home/zerodha.html', {"orders": orders})
        return redirect(kite.login_url())
    except Exception as e:
        logger.error(e.__cause__)
        logger.error(e)
        return HttpResponse({"message": e.__cause__}, status=500)


def position(request):
    position = kite.positions()['net']
    logger.info("position is:{}".format(position))
    return render(request, 'home/position.html', {"positions": position})



def holding(request):
    holding = kite.holdings()
    logger.info("Holding is:{}".format(holding))
    return render(request, 'home/holding.html', {"holdings": holding})


def login_redirect(request):
    try:
        login_status = request.GET.get("status")
        if login_status == 'success':
            request_token = request.GET.get("request_token")
            token_cache['request_token'] = request_token
            data = kite.generate_session(request_token, api_secret=api_secret)
            kite.set_access_token(data["access_token"])
            # Fetch all orders
            orders = kite.orders()
            # store in DB
            # hit kite api
        return render(request, 'home/zerodha.html', {"orders": orders})
    except Exception as e:
        logger.error(e.__cause__)
        logger.error(e)
        return HttpResponse({"message": e.__cause__}, status=500)
