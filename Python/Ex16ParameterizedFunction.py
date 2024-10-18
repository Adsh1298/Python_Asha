# from Ex15Function import add_func
#
#
# def sum_func(v1,v2):
#     return v1+v2
# def sub_func(v1,v2):
#     return v1-v2
# def mul_func(v1,v2):
#     return v1*v2
# def div_func(v1,v2):
#     return v1//v2
# def calculate(v1,v2):
#     sum_value=add_func(v1,v2)
#     sub_value=sub_func(v1,v2)
#     mul_value=mul_func(v1,v2)
#     div_value=div_func(v1,v2)
#     return sum_value + sub_value + mul_value + div_value
# a,s,m,d=calculate(13,12)#internally, the multiple return values will be a
# # TUPLE.
# print(f"The added value is {a},Subtarcted value is {s}, multiplied value is"f"{m}"
# f"and the"
# f"divided value is {d:.2f}")
#  def display_invoice(name,amount,due_date):
#  print(f"Hai Mr.{name}")
#  print(f"An amount of {amount} is pending from your end")
#  print(f"The last date for payment is due on {due_date}")
#  print("Please ignore if already paid")
#  display_invoice("asha",4500,'9/10/2024')
#
 #Default Parameter
def get_net_price(list_price,discount=0,tax=0.05):
 total_price= list_price*(1-discount)+(1+tax)
 return total_price
print(get_net_price(500))

     #Keyword parameters:U can precede a parameter with its identifier anf place
     # them in any order
def greeting(message,title,name):
    print(f"{message}!!! {title}. {name}")
greeting(title="Dr",message="Good Afternoon",name="Ramesh")

def add_numbers(*args):
    total = 0.0
    for arg in args:
        total += arg
        return total
    print(add_numbers(1,2,3,4,5,6))

    def get_address(**kwargs):
        print(f"{kwargs.get('flat_no')} ,{kwargs.get('appartment_name')}")
        print(f"{kwargs.get('city')} ,{kwargs.get('pin')}")

        #** is a wild char that implies keyword arguments.Internally the are
        # dictionary
        get_address(flat_no=326,area="RR Nagar",apartment_name="Vastu HillView-2",
                    city="Bangalore",pin=560098)
