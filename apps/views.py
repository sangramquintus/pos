import json

from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
from power_stock.settings import kite, api_secret, token_cache


def default(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()


def index(request):
    return render(request, "home/index.html")


def dashboard(request):
    return render(request, "dashboard/index.html")


def logout(request):
    return render(request, 'home/index.html')


def place_order():
    try:
        order_id = kite.place_order(tradingsymbol="YESBANK", variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=3,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC)

        print("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        print("Order placement failed: {}".format(e))


def kite_login(request):
    token = token_cache.get("request_token", None)
    if token:
        start_time = datetime.now()
        print(start_time)
        # instruments = kite.instruments()[:5]
        place_order()
        orders = kite.orders()
        order_data = json.dumps(orders, indent=4, sort_keys=True, default=str)
        print(order_data)
        end_time = datetime.now()
        print(end_time)
        return render(request, 'home/zerodha.html', {"orders": orders})

    return redirect(kite.login_url())


def login_redirect(request):
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
